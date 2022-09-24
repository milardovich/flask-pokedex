from flask import Flask, render_template, request, url_for
import requests, random

app = Flask(__name__)

@app.route("/")
def pokedex():
    if not 'pokemon' in request.args:
        pokemon = ''
    else:
        pokemonName = request.args.get("pokemon")

        if pokemonName == 'random':
            urlRandom = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0'
            r = requests.get(urlRandom).json()
            pokemonName = random.choice(list(r['results']))['name']

        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemonName
        r = requests.get(url)
        if r.status_code == 404:
            pokemon = 'error'
        else:
            pokemon = r.json()


    return render_template('index.html', pokemon=pokemon)


if __name__ == "__main__":
    app.run(debug=True)