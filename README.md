# 🏝️ Travel Planner Crew AI Agents - Streamlit App 🗺️
Travel Planner Crew AI Agents to Get `Travel Plan`for a specific `City`, `Travel Period`, `Interests` (From Paris to NY) 

## ✈️ Work Flow
- Ai Crew - 3 Agents :
- `Agent Travel` : Get the informations for travel and accomodations
- `Agent Guide` : Get the informations for the destination, focus on user interests
- `Agent Planner` : Plan the final Travel Plan
- LangChain, YF Tools, Groq Inference

![CrewAi App WorkFlow](workflow.png)

## TRAVEL PLANNER : LANGCHAIN & CREW AI
- Travel Planner assitant to help plan your travel and generate a LLM powered financial reports.

![CrewAi App WorkFlow](TravelPlanner_screenshot.png)

## CREW AI AGENT :
- An advanced research assistant by leveraging LangChain-powered tools into a CrewAI-powered multi-agent setup.
- LangChain is a framework enabling developers to easily build LLM-powered applications over their data; it contains production modules for indexing, retrieval, and prompt/agent orchestration.
- A core use case is building a generalized QA interface enabling knowledge synthesis over complex questions.
- Plugging a LangChain RAG pipeline as a tool into a CrewAI agent setup enables even more sophisticated/advanced research flows

## ✈️ Run the App

### Prerequisites
- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/keys))
- Serper API key (get it from [Serper.dev](https://serper.dev/api-key))

### Setup Instructions

1. **Fork or Clone the Repo**
   ```bash
   git clone <your-repo-url>
   cd TravelPlanner-CrewAi-Agents-streamlit
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   - Copy the example secrets file:
     ```bash
     cp .streamlit/secrets.toml.example .streamlit/secrets.toml
     ```
   - Edit `.streamlit/secrets.toml` and add your API keys:
     ```toml
     GROQ_API = "your_groq_api_key_here"
     SERPER_API_KEY = "your_serper_api_key_here"
     ```

4. **Run the App**
   ```bash
   python -m streamlit run TravelCrewApp.py
   ```
   
   Or simply:
   ```bash
   streamlit run TravelCrewApp.py
   ```

5. **Open in Browser**
   - The app will automatically open at `http://localhost:8501`
   - Or manually navigate to the URL shown in the terminal

## 🔒 Security Note
- **Never commit** `.streamlit/secrets.toml` to version control
- The `.gitignore` file is configured to exclude sensitive files
- Use `.streamlit/secrets.toml.example` as a template
