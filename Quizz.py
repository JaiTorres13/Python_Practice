"""
    This is a class of exercises from the project manager of my investigation group.
    The purpose is to test our knowledge of the programming language
"""


# 1
"""  Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal in alphabetical order , such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!  """

print("Exercise 1:\n")
animals = ["dog", "cat", "hamster"]
animals.sort()
for x in animals:
    print("A", x, ", makes a great pet!")


print("\nThese animals has four legs!\n")

# 2
""" Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder. """

print("Exercise 2:\n")
age = 25

if age < 2:
    print("The person is a baby!\n")
elif 2 <= age < 4:
    print("The person is a Toddler!\n")
elif 4 <= age < 13:
    print("The person is a kid!")
elif 13 <= age < 20:
    print("The person is a Teenager!\n")
elif 20 <= age < 65:
    print("The person is an Adult!\n")
else:
    print("The person is an Elder!\n")

# 3
"""  Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of three  programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.  """

print("Exercise 3:\n")
glossary = {'for': 'it is a loop', 'if': 'it is a condition', 'constructor': 'has the same name of a class'}


for key in glossary.keys():
    value = glossary[key]
    print(key, "=", value)


# 4
""" Linear regressor : Create a class called linear regression with 2 attributes for weights and 
one for a feature(all default 0), make a method called hypothesis that receives as parameters the weights and
 features and returns the estimated value of the hypothesis
Create an instance of this class and test your method with some 
values for weights and feature. h(x) = theta + theta*x  """

print("\nExercise 4:\n")
class  LinearRegression:

    __weight1 = ""
    __weight2 = ""
    __feature = ""

    def __init__(self, __weight1, __weight2, __feature):
        self.__weight1 = 0
        self.__weight2 = 0
        self.__feature = 0

    def set_weight1(self, __weight1):
        self.__weight1 = __weight1

    def get_weight1(self):
        return self.__weight1

    def set_weight2(self, __weight2):
        self.__weight2 = __weight2

    def get_weight2(self):
        return self.__weight2

    def set_feature(self, __feature):
        self.__feature = __feature

    def get_feature(self):
        return self.__feature

    def hypothesis(self, __weight1, __weight2, __feature):
        return __weight1 + (__weight2 * __feature)


lin = LinearRegression(1, 2, 3)
print(lin.hypothesis(1, 2, 3))
