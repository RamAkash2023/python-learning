# escape character
print('Pluto\'s a planet!')
plant = "Banyan"
print(plant[-3:])
# Strings are immutable
sentence = "Planet is full of Banyan"
print(sentence.endswith(plant))
words = sentence.split()
print(words)
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)
# join takes list as an input
print('/'.join([year, month, day]))

planet = "Pluto"
position = 9
# tough one
planet + ", you'll always be the " + str(position) + "th planet to me."

# format to the rescue
print("{}, you'll always be the {}th planet to me. ".format(plant, position))


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


numbers = {'one': 1, 'two': 2, 'three': 3}

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

# A for loop over a dictionary will loop over its keys
list_of_planets = planet_to_initial.keys()
print(list_of_planets)
print(' '.join(planet_to_initial.values()))
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
x = "LOL"
print(isinstance(x, str))
# //rjust(20)--> right justified, you word will be having 20 letters, if your word length is 10 then 10 would be whitespaces, this is used to make every word ends at same line'

data = {"french": "France", "Spanish": "Spain"}
print(data["french"])
print(data.get("Germany"))
print(data.get("Germany", "??"))
