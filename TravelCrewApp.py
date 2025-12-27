
import sys
import os

# Fix dotenv encoding issue before importing crewai
# This prevents UnicodeDecodeError when dotenv tries to read corrupted .env files
try:
    import dotenv.parser
    import io
    
    # Store original Reader class
    original_reader_init = dotenv.parser.Reader.__init__
    
    def safe_reader_init(self, stream):
        try:
            # Try to read the stream safely
            if hasattr(stream, 'read'):
                # Check if it's a text stream or binary
                try:
                    # Try reading as text first
                    content = stream.read()
                    if isinstance(content, bytes):
                        # If bytes, try to decode
                        try:
                            content = content.decode('utf-8')
                        except UnicodeDecodeError:
                            # If decode fails, return empty
                            content = ""
                    # Create a safe text stream
                    safe_stream = io.StringIO(content)
                    original_reader_init(self, safe_stream)
                except (UnicodeDecodeError, UnicodeError, Exception):
                    # If any error, create empty reader
                    self.string = ""
                    self.position = dotenv.parser.Position.start()
                    self.mark = dotenv.parser.Position.start()
            else:
                original_reader_init(self, stream)
        except (UnicodeDecodeError, UnicodeError, Exception):
            # If encoding error, create empty reader
            self.string = ""
            self.position = dotenv.parser.Position.start()
            self.mark = dotenv.parser.Position.start()
    
    # Patch the Reader class
    dotenv.parser.Reader.__init__ = safe_reader_init
except Exception:
    pass

# Also patch load_dotenv to handle errors at multiple levels
try:
    import dotenv.main
    original_load = dotenv.main.load_dotenv
    def safe_load_dotenv(*args, **kwargs):
        try:
            return original_load(*args, **kwargs)
        except (UnicodeDecodeError, UnicodeError, Exception):
            # If any error loading .env, just skip it
            # We're using Streamlit secrets anyway
            return False
    dotenv.main.load_dotenv = safe_load_dotenv
except Exception:
    pass

# Patch the DotEnv class set_as_environment_variables method
try:
    import dotenv.main
    original_set = dotenv.main.DotEnv.set_as_environment_variables
    def safe_set_as_env_vars(self):
        try:
            return original_set(self)
        except (UnicodeDecodeError, UnicodeError, Exception):
            return False
    dotenv.main.DotEnv.set_as_environment_variables = safe_set_as_env_vars
except Exception:
    pass

import streamlit as st
from datetime import datetime, timedelta
import warnings

# Suppress signal handler warnings (they're harmless in Streamlit context)
warnings.filterwarnings("ignore", message=".*signal.*")

# Import crewai with error handling
try:
    from crewai import Crew, Process
except UnicodeDecodeError:
    # If still getting encoding error, try to find and handle corrupted .env
    import glob
    import pathlib
    # Try to find .env files and skip them
    for env_file in ['.env', '.env.local', '.env.*']:
        for file_path in glob.glob(env_file, recursive=False):
            try:
                # Try to read as binary and check encoding
                with open(file_path, 'rb') as f:
                    content = f.read()
                    # If starts with 0xff, it's likely corrupted
                    if content and content[0] == 0xff:
                        # Rename corrupted file
                        os.rename(file_path, file_path + '.corrupted')
            except:
                pass
    # Try importing again
    from crewai import Crew, Process

from TravelAgents import TravelAgents, StreamToExpander
from TravelTasks import TravelTasks

st.set_page_config(page_icon="✈️", page_title="ZeeTravelPlanner", layout="wide")

# class TravelCrew
class TravelCrew:

  def __init__(self, from_city, destination_city, interests, date_from, date_to):
      self.destination_city = destination_city
      self.from_city = from_city
      self.interests = interests
      self.date_from = date_from
      self.date_to = date_to
      self.output_placeholder = st.empty()
  
  def run(self):
      agents = TravelAgents()
      tasks = TravelTasks()
  
      location_expert = agents.location_expert()
      guide_expert = agents.guide_expert()
      planner_expert = agents.planner_expert()

      location_task = tasks.location_task(
          location_expert,
          self.from_city,
          self.destination_city,
          self.date_from,
          self.date_to
        )

      guide_task = tasks.guide_task(
          guide_expert,
          self.destination_city,
          self.interests,
          self.date_from,
          self.date_to
        )

      planner_task = tasks.planner_task(
          [location_task, guide_task],
          planner_expert,
          self.destination_city,
          self.interests,
          self.date_from,
          self.date_to,
        )
  
      crew = Crew(
        agents=[location_expert, guide_expert, planner_expert],
        tasks=[location_task, guide_task, planner_task],
        process=Process.sequential,
        full_output=True,
        share_crew=False,
        #llm=llm_groq,
        verbose=True
        )
  
      result = crew.kickoff()
      self.output_placeholder.markdown(result)
  
      return result
  
st.header("✈️ 🎫 Travel Planner :orange[Ai]gent 🏝️ 🗺️", divider="orange" )

# sidebar
with st.sidebar:
  st.caption("Travel Planner Agent")
  st.markdown(
    """
    # 🏝️ Travel Planner 🗺️
        1. Pick your dream destination
        2. give us your interests
        3. Set your travel dates
        4. Bon voyage !!
    """
  )

st.session_state.plan_pressed = False
# User Inputs
today = datetime.now()
one_year_from_now = today + timedelta(days=365)
seven_days_from_now = today + timedelta(days=7)

st.caption("🗺️ Let's plan your Travel")


# User Details container
C = st.container(border=True)
X1, X2 = C.columns(2)
from_city = X1.text_input("📍 From :", placeholder="Paris, France")
destination_city = X2.text_input("🏝️ Your Destination :", placeholder="London, UK")

interests = C.text_input("🍹🛍️ Your interests :",  placeholder="Cultural, hotspots, Food, Shopping..")

Y1, Y2 = C.columns(2)

date_from = Y1.date_input(
  "📅 Vacation Start ✈️",
  today,
  format="DD/MM/YYYY",
)
date_to = Y2.date_input(
  "📅 Vacation End 🧳",
  seven_days_from_now,
  format="DD/MM/YYYY",
)
travel_period = (date_to - date_from).days
if from_city and destination_city and date_from and date_to and interests:
  st.caption("👌 Let's recap you Travel Plan :")
  st.write(f":sparkles: Your 🎫 :blue[{travel_period}-Days] Voyage from 📍 :blue[{from_city}] is starting the ✈️ {date_from} to 🧳 {date_to}. 🗺️ Your are heading to 🏝️ :orange[{destination_city}], to Enjoy 🍹 :orange[{interests}] 📸.")
  if plan := st.button("💫 Sounds Good ! 🗺️ Generate The Travel Plan", use_container_width=True, key="plan"):
    with st.spinner(text="🤖 Agents working for the best Travel Plan 🔍 ..."):
      # RUN
      try:
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
          with st.container(height=200, border=False):
              sys.stdout = StreamToExpander(st)
              travel_crew = TravelCrew(from_city, destination_city, interests, date_from, date_to)
              result = travel_crew.run()
          status.update(label="✅ Trip Plan Ready!",
                        state="complete", expanded=False)

        st.subheader("🗺️ Here is your Trip Plan 🎫 🏝️", anchor=False, divider="rainbow")
        st.markdown(result)
      except Exception as e:
        error_msg = str(e)
        if "rate_limit" in error_msg.lower() or "ratelimit" in error_msg.lower():
          st.error("⚠️ **Rate Limit Reached**\n\nYou've hit Groq's rate limit. Please:\n- Wait a few minutes and try again\n- Or upgrade to Groq Dev Tier at https://console.groq.com/settings/billing\n\nTip: The app is using `llama-3.1-8b-instant` for better rate limits.")
        else:
          st.error(f"❌ **Error occurred**: {error_msg}\n\nPlease check your API keys and try again.")
        st.exception(e)
      

  








