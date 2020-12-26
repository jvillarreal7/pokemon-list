"""
Script that returns a file containing a specified range of Pokémon (by gen) 
separated by commas. Uses a Bulbapedia table as data source.

Put this together quickly to play "who's that (barely recognizable) Pokémon?"
on skribbl.io with my friends using the generated file.
Got a little carried away making small improvements, since I thought
somewhere, someone would find use in something like this. :)
"""

from bs4 import BeautifulSoup
from ordered_set import OrderedSet
from exceptions import *
import requests

CURRENT_GEN = 8

GEN_STARTS_WITH = {
    1: 'Bulbasaur',
    2: 'Chikorita',
    3: 'Treecko',
    4: 'Turtwig',
    5: 'Victini',
    6: 'Chespin',
    7: 'Rowlet',
    8: 'Grookey',
}

GEN_ENDS_WITH = {
    1: 'Mew',
    2: 'Celebi',
    3: 'Deoxys',
    4: 'Arceus',
    5: 'Genesect',
    6: 'Volcanion',
    7: 'Melmetal',
    8: 'Calyrex',
}

NIDORAN_CASE = {
    '\u2642': 'M',
    '\u2640': 'F'
}

URL = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'


def main():
    """
    Main script method.

    params: None
    returns: None
    """
    try:
        start_gen = int(input("Start with gen (1-8):\n"))
        end_gen = int(input("End with gen (1-8):\n"))

        if start_gen < 1 or end_gen < 1:
            print("What are you trying to do exactly?")
            raise GensLowerThanOneError

        if start_gen > end_gen:
            print("Start gen should be less than end gen.")
            raise StartGenHigherThanEndGenError

        if start_gen > CURRENT_GEN or end_gen > CURRENT_GEN:
            print(f"Gens above {CURRENT_GEN} are not supported.")
            raise UnsupportedGenError

    except ValueError:
        print("That's not a number bruh.")
        return

    data = get_data(URL)
    pkmn_string = parse_table(data, start_gen, end_gen)
    write_formatted_mons(pkmn_string)
    

def get_data(URL):
    """
    Fetch data from Bulbapedia with requests and BeautifulSoup.

    params: URL (string)
    returns: soup (BeautifulSoup object)
    """
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        print(f"Fetching data from '{URL}' was successful.")
        return soup
    except Exception as e:
        print(f'Something went wrong while fetching the page: {e}')
        return


def parse_table(soup, start_gen, end_gen):
    """
    - Finds the PKMN names in the soup object and puts them into a list.
    - Establishes a gen range.
    - Gets rid of repeated entries (formes, e.g. Deoxys) using an OrderedSet.
    - Joins the list with commas.
    - Handles both Nidorans having 'unmappable' characters in their names (u2642 and u2640).

    params: soup (BeautifulSoup object), start_gen (int), end_gen (int)
    returns: pkmn_string (string)
    """
    pokes = []
    for cell in soup.find_all("td", attrs={'style': None}):
        for name in cell.find_all("a"):
            pokes.append(name.string)

    start_index = pokes.index(GEN_STARTS_WITH[start_gen])
    end_index = pokes.index(GEN_ENDS_WITH[end_gen]) + 1

    # Doesn't have to be ordered, just personal taste.
    unique_list = OrderedSet(pokes[start_index:end_index])

    if start_gen != end_gen:
        print(f"{len(unique_list)} Pokémon from gen {start_gen} to {end_gen} were fetched.")
    else:
        print(f"{len(unique_list)} Pokémon from gen {start_gen} were fetched.")

    pkmn_string = ', '.join(unique_list)

    for key, value in NIDORAN_CASE.items():
        # Handling of Nidoran male/female symbols.
        pkmn_string = pkmn_string.replace(key, value)

    return pkmn_string


def write_formatted_mons(pkmn_string):
    """
    Writes string with all Pokémon to txt file.

    params: pkmn_string (string)
    returns: None
    """
    try:
        with open('pokemon_list.txt', 'w', encoding='utf8') as pkfile:
            pkfile.write(pkmn_string)
        pkfile.close()
        print("File saved successfully.")
    except Exception as e:
        print(f"Something went wrong while attempting to create the file: {e}")
        return


if __name__ == '__main__':
    main()
