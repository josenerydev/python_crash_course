import pizza_03
from pizza_03 import make_pizza
from pizza_03 import make_pizza as mp
import pizza_03 as p
from pizza_03 import *

pizza_03.make_pizza(16, 'pepperoni')
pizza_03.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')