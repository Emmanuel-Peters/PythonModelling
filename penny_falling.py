# originally done in Jupyter Notebook, decided to do it in a plain
# Python file instead

# Stephen Peters April 2024

import numpy
from pint import UnitRegistry
from numpy import pi, sin, cos

units = UnitRegistry()

metre = units.meter
second = units.second

g = 9.8 * metre / second ** 2 # Gravitational Acceleration

# How far penny would fall after 5 seconds ignoring air resistance
t = 5 * second

x = g * t ** 2 / 2

print('After 5 seconds, the penny would fall ' + str(x) + ' metres')

# Time it takes penny to fall 381 metres

h = 381 * metre

t = numpy.sqrt(2*h/g)
print('It would take the penny ' + str(t) + ' seconds to fall 381 metres')
print('The velocity at impact would be ' + str(g*t) + ' metres/second')

# Assuming Terminal Velocity is at 29 m/s, how long would it take to fall 381 metres

# If we know the acceleration and velocity we're looking for, we can find 
# how long it takes to reach that terminal velocity

terminal_velocity = 29 * metre / second

t = terminal_velocity / g

# Thus we can calculate how much distance was covered

x1 = g * t ** 2 / 2

# The remaining distance is at a constant velocity...

x2 = h - x1
t2 = x2 / terminal_velocity 

total_time = t + t2
print('It would take ' + str(total_time) + ' to fall 381 metres')

# Finally, in an unrelated exercise lets check a fundemental trig identity.
print(sin(pi/4)**2 + cos(pi/4)**2)