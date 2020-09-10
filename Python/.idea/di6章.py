'''alien_0={}
alien_0['color']='green'
alien_0['points']=5
alien_0['x-position']=0
alien_0['y_position']=25
alien_0['speed']='medium'

print(alien_0)
del alien_0['points']
print(alien_0)

alien_0={'color':'red','point':'15'}
alien_1={'color':'blue','point':'10'}
alien_2={'color':'yellow','point':'5'}

aliens=[alien_0,alien_1,alien_2]
print(aliens)

aliens=[]
for alien_number in range(30):
    new_alien={'color':'yellow','point':'5'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
'''
favourite_languages={
    'mao':['python','rudy'],
    'zhu':['c'],
    'zhou':['ruby','go'],
    'he':['python','haskell'],
    }

for name,languages in favourite_languages.items():
    if len(languages)==1:
        print("\n" + name.title() + "'s favourite languages is:")
    else:
        print("\n"+name.title()+"'s favourite languages are:")
    for language in languages:
        print("\t"+language.title())







