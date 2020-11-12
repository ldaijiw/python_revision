# Declare a list with numbers 1 to 5 and add 6 at the end
new_list = [1, 2, 3, 4, 5]
new_list.append(6)

# Create a tuple with numbers 1 to 5 and print up to 3
new_tuple = (1, 2, 3, 4, 5)

for num in new_tuple:
    if num > 3:
        break
    print(num)