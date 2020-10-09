from pygal_maps_world.i18n import COUNTRIES

#print(COUNTRIES)

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        #print(code+"  "+name)
        if name == country_name:
            return code

    return None

#print(get_country_code('Zambia'))