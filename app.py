from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def pokemon_page(query):
    url = "http://pokeapi.co/api/v2/pokemon/"+ query
    response  = requests.get(url) #Get response
    json_data = json.loads(response.text); #Extract dictionary from json

    if query.isdigit():
        return 'Pokemon with id %s is %s'%(query, json_data['name'])
    else:
        return '%s has id %s'%(query, json_data['id'])

if __name__ == '__main__':
    app.run()
