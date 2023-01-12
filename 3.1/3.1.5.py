beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
beatles_map['Ringo'] = 'Drums'
jhon_instrument = beatles_map['John']
beatles_map.pop('John')

print((beatles_map),'\n',jhon_instrument)