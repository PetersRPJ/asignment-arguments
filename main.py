# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1 greeting template
def greet(name, greeting_template='Hello, <name>!'):
    return print(greeting_template.replace('<name>', name))
greet('Bob')

# Part 2 Force

def force(mass, body='earth'):
    planets = {'earth': 9.8, 'sun': 274, 'jupiter': 24.9, 'neptune': 11.2, 'saturn': 10.4, 'uranus': 8.9, 'venus': 8.9, 'mars': 3.7, 'mercury': 3.7, 'moon': 1.6, 'pluto': 0.6}
    a = float(mass)
    return print (a*planets[body])

force(2, 'jupiter')

# part 3 

def pull(m1, m2, d):
    a = float(m1)
    b = float(m2)
    c = float(d)
    gravity = (6.674 * 10 ** -11) * ((a*b)/c**2)
    return gravity 

print (pull(800,1500,3))