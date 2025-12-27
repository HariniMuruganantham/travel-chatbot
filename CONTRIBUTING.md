# Contributing to Travel Planner CrewAI Agents

Thank you for your interest in contributing! 🎉

## Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/TravelPlanner-CrewAi-Agents-streamlit.git
   cd TravelPlanner-CrewAi-Agents-streamlit
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your secrets:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   # Edit .streamlit/secrets.toml with your API keys
   ```

## Code Style

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

## Testing

Before submitting a PR, make sure:
- The app runs without errors
- All agents work correctly
- No sensitive data is committed
- The README is updated if needed

## Reporting Issues

When reporting issues, please include:
- Python version
- Operating system
- Error messages (if any)
- Steps to reproduce

## Questions?

Feel free to open an issue for questions or discussions!

