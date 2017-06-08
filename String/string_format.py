drink = "coffee"
drinkAmount = 4

string = "Today I had {0} cups of {1}!".format(drinkAmount, drink)
print(string)

string = "Bananas: {b}, Apples: {a}, Pears: {p}".format(a = 3, p = 31, b = 12)
print(string)

string = "A {animal} has {0} arms and {1} legs!".format(2, 2, animal = "human")
print(string)

align_string = "Alignment!"
#Right Alignment, 20 chars
string = "{:>20}".format(align_string)
print(string)

#Left Alignment, 20 chars
string = "{:<20}".format(align_string)
print(string)

number = 74
#Base N output
#Base 2, binary
print("Binary {:b}".format(number))

#Base 16, hexadecimal
print("Hexadecimal {:x}".format(number))

#Base 8, octal
print("Octal {:o}".format(number))
