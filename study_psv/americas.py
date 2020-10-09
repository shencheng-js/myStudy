import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm._title = "The world map"

wm.add('North America',{'ca':3412600,'mx':113423000,'us':309349000})
#wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
#wm.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','sr','uy','ve'])

wm.render_to_file("america.svg")