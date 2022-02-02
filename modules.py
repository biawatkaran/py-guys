# Modules are nothing but python files and package are like folder that contains similar modules

import converters
from converters import first_method as short_way_first_method

converters.first_method()
converters.second_method()

print("\nCalling in short way")
short_way_first_method()
