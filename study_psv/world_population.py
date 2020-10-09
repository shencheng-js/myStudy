import json
from pygal_maps_world.i18n import COUNTRIES
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle

filename = 'population_data.json'

with open(filename) as f:
    pop_datas = json.load(f)

cc_population = {}

for pop_data in pop_datas:
    if pop_data['Year'] == '2010':
        country_name = pop_data['Country Name']
        population = int(float(pop_data['Value']))
        code = get_country_code(country_name)

        if code:
            cc_population[code] = population

cc1,cc2,cc3 = {},{},{}
for cc,populat in cc_population.items():
    if populat < 10000000:

        cc1[cc] = populat
    elif populat<1000000000:
        cc2[cc] = populat
    else:
        cc3[cc] = populat

print(len(cc1),len(cc2),len(cc3))

wm_stytle = RotateStyle("#000000")
wm = pygal_maps_world.maps.World(stytle=wm_stytle)
wm._title = "The world map"
wm.add("0-10m",cc1)
wm.add("10m-1bn",cc2)
wm.add(">1bn",cc3)

wm.render_to_file("2010_world_population_map.svg")