from flask import Flask, request, jsonify, render_template
import os
import json

import constants
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

app = Flask(__name__)

loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = json.loads(request.data)
    query = data['query']
    result = index.query(query, llm=ChatOpenAI())
    return jsonify({'result': str(result)})

@app.route('/append', methods=['POST'])
def append_data():
    data = json.loads(request.data)
    data_to_append = data['data']
    with open('data.txt', 'a') as f:
        f.write("\n" + data_to_append)
    global index
    index = VectorstoreIndexCreator().from_loaders([loader])
    return {"success": True}, 200

if __name__ == "__main__":
    app.run(debug=True)
