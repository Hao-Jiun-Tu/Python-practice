# MODULE

import sys as system
print(system.platform) # OS
print(system.maxsize)  # integer size
print(system.path)     # python-modules search path
print("----------------------------------------------------------------------")

system.path.append("./modules")
print(system.path)
print("----------------------------------------------------------------------")
import geometry 
print(geometry.distance(1, 1, 5, 5))
print(geometry.slope(1, 2, 4, 5))

