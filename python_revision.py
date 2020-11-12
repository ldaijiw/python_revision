# Declare a list with numbers 1 to 5 and add 6 at the end
new_list = [1, 2, 3, 4, 5]
new_list.append(6)

# Create a tuple with numbers 1 to 5 and print up to 3
new_tuple = (1, 2, 3, 4, 5)

for num in new_tuple:
    if num > 3:
        break
    print(num)


# Declare a dictionary of a shopping list with 3 items, find what type of data it is
shopping_dict = {"apple": 0.5, "banana": 0.75, "bread": 1}
print(type(shopping_dict))

# find price for one item
print(shopping_dict["bread"])

# replace price for one of the items
shopping_dict["bread"] = 2
print(shopping_dict["bread"])


# Declare function that takes two arguments to add 2 numbers together
def add(num1, num2):
    return num1 + num2

print(add(2,4))


# Create a class called person with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


new_person = Person("Leo", 21)
print(new_person.name)
print(new_person.age)