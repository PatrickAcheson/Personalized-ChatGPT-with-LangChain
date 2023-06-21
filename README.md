# GPT-SELF

I've created a quick spin up of a web-based chat application I am calling GPT-SELF, that leverages the capabilities of OpenAI's GPT-3.5 Turbo model using LangChain. This application allows you to engage in interactive dialogues and gives you the flexibility to append custom data to (`data.txt`), thus creating a personalized dataset for the AI.

The line `result = index.query(query, llm=ChatOpenAI())` uses a split band functionality, querying based on both your `data.txt` file and OpenAI's general dataset. Directory loading can be achived by uncommenting this command `loader = DirectoryLoader(".", glob="*.txt")` if an more expansive dataset needs to be read.


Possible applications include:
- Creating reminders for events
- Consolidating notes for various subjects
- Building a unique dataset of self

Prerequisites:
- A valid OpenAI API key
- A Conda environment (recommended for ease of setup)
- Visual Studio Build Tools (if needed)
- data.txt needs atleast some data in it or error

**IMPORTANT**: Please append only the data you are comfortable sharing with OpenAI, in accordance with their [data usage policy](https://openai.com/policies/api-data-usage-policies).

## Getting Started

1. Clone this repo: `git clone https://github.com/PatrickAcheson/organise-me`
2. Install Python (tested on 3.9.13) conda and, if needed, Visual Studio Build Tools.
3. Install the required packages using: `pip install -r requirements.txt`
4. Set your OpenAI API Key in `constants.py`
5. Start the application with: `python3 app.py`
6. Access the application at `http://localhost:5000` and start interacting with the AI!

## Contributing

Your contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a PR.

## Screenshot

![image](https://github.com/PatrickAcheson/organise-me/assets/90014630/a83c2118-abba-47af-8ef1-c73bb0907179)
