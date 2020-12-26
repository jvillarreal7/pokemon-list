# pokemon-list
Console app that fetches a list of Pokémon from Bulbapedia within a specified generation range.

## Installation and usage
- Download [Python 3](https://www.python.org/downloads/).
- Clone the repo, preferrably create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and run `pip install -r requirements.txt` using a terminal in the root directory.
- To execute the script just run `python generate_pokemon.py` in the terminal while in the root directory, though this may vary slightly depending on how your Python path is configured, just make sure it's Python 3 and you should be fine.
- After this, a `pokemon_list.txt` should be generated in the root directory. Feel free to use that for whatever you need.
- If something doesn't behave as expected, you can execute the unit tests by running `pytest -vv` in the terminal and hopefully see what's wrong. You may create an [issue](https://github.com/jvillarreal7/pokemon-list/issues) if you wish and I'll get back to you when I can.
