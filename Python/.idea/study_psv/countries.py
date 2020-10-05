from pygal_maps_world.i18n import COUNTRIES
filename = 'population_data.json'

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])