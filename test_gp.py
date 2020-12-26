"""
Unit tests for the generated Pokémon script.
"""

import generate_pokemon as gp
import requests, pytest
from bs4 import BeautifulSoup

@pytest.fixture
def URL():
    return gp.URL

@pytest.fixture
def soup():
    page = requests.get(gp.URL)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

@pytest.fixture
def start_gen():
    return 1

@pytest.fixture
def end_gen():
    return 1

@pytest.fixture
def pokemon_string():
    return "Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok, Pikachu, Raichu, Sandshrew, Sandslash, NidoranF, Nidorina, Nidoqueen, NidoranM, Nidorino, Nidoking, Clefairy, Clefable, Vulpix, Ninetales, Jigglypuff, Wigglytuff, Zubat, Golbat, Oddish, Gloom, Vileplume, Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian, Psyduck, Golduck, Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Abra, Kadabra, Alakazam, Machop, Machoke, Machamp, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Geodude, Graveler, Golem, Ponyta, Rapidash, Slowpoke, Slowbro, Magnemite, Magneton, Farfetch'd, Doduo, Dodrio, Seel, Dewgong, Grimer, Muk, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee, Hypno, Krabby, Kingler, Voltorb, Electrode, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee, Hitmonchan, Lickitung, Koffing, Weezing, Rhyhorn, Rhydon, Chansey, Tangela, Kangaskhan, Horsea, Seadra, Goldeen, Seaking, Staryu, Starmie, Mr. Mime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros, Magikarp, Gyarados, Lapras, Ditto, Eevee, Vaporeon, Jolteon, Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew"

@pytest.fixture
def file_path():
    return "./pokemon_list.txt"

class GeneratePokemonTests:
    def test_current_gen_is_valid(self):
        assert gp.CURRENT_GEN == len(gp.GEN_STARTS_WITH)
        assert gp.CURRENT_GEN == len(gp.GEN_ENDS_WITH)

    def test_request_is_successful(self, URL):
        assert requests.get(URL).status_code == 200

    def test_parsed_table_still_contains_pokemon(self, soup, start_gen, end_gen, pokemon_string):
        assert gp.parse_table(soup, start_gen, end_gen) == pokemon_string
