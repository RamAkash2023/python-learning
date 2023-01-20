sample_list = ["nNorth West", "West", "West Bengal", "Bangladesh"]
isWest = ['Yes' if 'West' in location else 'No' for location in sample_list]
print(isWest)
myString = "Akash"
print(myString[::-1])
currentYear = 2021

print(f'My name is {myString} and my age is {currentYear - 1997}')

sentence = "This is a normal sentenance looking to get capitaized"
print(sentence.title())

myname = int(121)
print('Yes' if str(myname) == str(myname)[::-1] else 'No')
print(myString.count("a"))
word = "Sita ram"
print(word[-3:])  # last three character
print(word[3:])  # all char except first three

print(word.capitalize())

print(word.center(90))

print(" ".join(myString))

print(myString.isalpha())
