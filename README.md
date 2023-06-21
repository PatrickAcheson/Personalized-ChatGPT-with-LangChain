# GPT-SELF

GPT-SELF is a dynamic web-based chat application, leveraging the capabilities of OpenAI's GPT-3.5 Turbo model. This application allows you to engage in interactive dialogues and gives you the flexibility to append custom data, thus creating a personalized dataset for the AI. The line `result = index.query(query, llm=ChatOpenAI())` uses a split band functionality, querying based on both your `data.txt` file and OpenAI's general dataset.

Possible applications include:
- Creating reminders for events
- Consolidating notes for various subjects
- Building a unique dataset of self

Prerequisites:
- A valid OpenAI API key
- A Conda environment (recommended for ease of setup)
- Visual Studio Build Tools (if needed)

**IMPORTANT**: Please append only the data you are comfortable sharing with OpenAI, in accordance with their [data usage policy](https://openai.com/policies/api-data-usage-policies).

## Getting Started

1. Clone this repo: `git clone <repo-link>`
2. Install Python 3.9.13 (tested on) and, if needed, Visual Studio Build Tools.
3. Install the required packages using: `pip install -r requirements.txt`
4. Set your OpenAI API Key in `constants.py`
5. Start the application with: `python3 app.py`
6. Access the application at `http://localhost:5000` and start interacting with the AI!

## Contributing

Your contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a PR.

