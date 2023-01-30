# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#part1
def greet(name, greeting_template = "Hello, <name>!"):
  greet = greeting_template.replace("<name>", name)
  print(greet)
  return greet

greet("Bob")

#part2

def force(mass, body ='earth'):
    bodys={
       'sun':  274,
       'jupiter':  24.92,
       'neptune':  11.15,
       'saturn':  10.44,
       'earth':  9.798,
       'uranus':  8.87,
       'venus':  8.87,
       'mars':  3.71,
       'mercury':  3.7,
       'moon':  1.62,
       'pluto':  0.58
      }
    force = float(mass) * round(bodys[body], 1)
    print(force)
    return force

force(1.45,)

#part3

def pull(m1, m2, d):
    g = 6.674 * 10 ** -11
    gravitional_pull = g * ((m1 * m2) /d ** 2)
    print(gravitional_pull)
    return gravitional_pull


pull (800, 1500, 3)