# Quick Setup Guide

## 🚀 Quick Start (5 minutes)

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd TravelPlanner-CrewAi-Agents-streamlit
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get API Keys

#### Groq API Key (Free)
1. Go to [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to [API Keys](https://console.groq.com/keys)
4. Create a new API key
5. Copy the key

#### Serper API Key (Free tier available)
1. Go to [Serper.dev](https://serper.dev/)
2. Sign up for a free account
3. Navigate to [API Key](https://serper.dev/api-key)
4. Copy your API key

### Step 4: Configure Secrets
```bash
# Copy the example file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit the file and add your keys
# On Windows: notepad .streamlit\secrets.toml
# On Mac/Linux: nano .streamlit/secrets.toml
```

Your `.streamlit/secrets.toml` should look like:
```toml
GROQ_API = "gsk_your_actual_key_here"
SERPER_API_KEY = "your_actual_serper_key_here"
```

### Step 5: Run the App
```bash
python -m streamlit run TravelCrewApp.py
```

The app will open automatically in your browser at `http://localhost:8501`

## ✅ Verify Setup

1. The app should load without errors
2. You should see the travel planner interface
3. Enter test data:
   - From: Paris, France
   - Destination: London, UK
   - Interests: Culture, Food
   - Select dates
4. Click "Generate The Travel Plan"
5. Wait for the agents to work (may take 1-2 minutes)

## 🐛 Troubleshooting

### "Module not found" errors
- Make sure you installed all dependencies: `pip install -r requirements.txt`
- Check if you're in a virtual environment

### "API key not found" errors
- Verify `.streamlit/secrets.toml` exists
- Check that your API keys are correct (no extra spaces)
- Make sure the file is named exactly `secrets.toml` (not `secrets.toml.example`)

### Rate limit errors
- Wait a few minutes and try again
- Consider using `llama-3.1-8b-instant` model (already configured) for better rate limits
- Upgrade to Groq Dev Tier for higher limits

### Unicode errors
- These should be fixed, but if you see them, check for corrupted `.env` files in parent directories

## 📝 Notes

- Generated reports (`city_report.md`, `guide_report.md`, `travel_plan.md`) are automatically ignored by git
- Your `secrets.toml` file is also ignored for security
- The app uses CrewAI with 3 specialized agents working together

## 🎉 You're Ready!

Start planning your dream trips! 🗺️✈️

