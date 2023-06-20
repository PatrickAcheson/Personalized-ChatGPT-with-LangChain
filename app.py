from flask import Flask, request, jsonify , render_template
import os

import constants
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    
    loader = TextLoader('data.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])

    result = index.query(query, llm=ChatOpenAI())
    return jsonify({'result': str(result)})

@app.route('/append', methods=['POST'])
def append_data():
    data = request.form['data']
    with open('data.txt', 'a') as f:
        f.write('\n' + data)
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
