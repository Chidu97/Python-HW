
# 1 - 
my_list = ["The","quick","brown","fox", "jumps", "over", "the", "lazy", "dog"]

# returned (my_list) as a new string list seperated by space
my_list1 = " ".join(my_list)
print(my_list1)


# 2 - 
new_list = ["this", "brown", 55, "oxen", True, 0.85]

# changed the value of the 4th item in (new_list) to false
new_list[4] = False
print(new_list)

# 3 - 
sample_list = ['Red','Green', 'White', 'Black', 'Pink', 'Yellow']

# removed the first and last two elements of a list and return the new updated list.
sample_list1 = sample_list[1:-2]

print(sample_list1)

# 4 -
color_list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# input_string = input("Enter a new color:")
# color_list = input_string.split(",")
# print("Printing new colors")
# for color in color_list:
#  print(color)

# created an input that takes in any amount of colors
input_string = input("Enter Color:")

# assigned the number of colors inputed a keyword (color)
color = input_string

# used the append function to join the new inputed colors to the end of the (color_list)
color_list.append(color)
print(color_list)



