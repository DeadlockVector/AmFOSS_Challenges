'''
Regex version of strip 
'''

import re

def stringStrip(main_String, stripELement='\s'):
    stripped_string = re.compile(f'^({stripELement})*|({stripELement})*$')
    final_string = stripped_string.sub('', main_String)
    print(final_string)

stringStrip('    lmaoooo    ')