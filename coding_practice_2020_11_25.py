################Python Workbok

#Exercise 34: Even or Odd?
# interger = int(input("Please enter interger: "))

# if interger % 2 == 0:
#     print(f"{interger} is even.")
# else:
#     print(f"{interger} is odd.")



#Exercise 35: Dog Years
# human = int(input("Input a dog's age in human years: "))
# if human < 0:
# 	print("Age must be positive number.")
# 	exit()
# elif human <= 2:
# 	dog = human * 10.5
# else:
# 	dog = 21 + (human - 2)*4

# print("The dog's age in dog's years is", dog)



#Exercise 36: Vowel or Consonant
# vowels = "a e i o o"
# letter = input("Please enter a letter from the alphabet: ").lower()
# if letter in vowels:
#     print("The entered letter is a vowel.")
# elif letter == "y":
#     print("Sometimes y is a vowel.")
# else:
#     print("The letter is a constant")



#Exercise 37: Name that shape
# possible_sides = "3 4 5 6 7 8 9 10"
# sides = input("Please enter number of sides: ")
# if sides not in possible_sides:
#     print("Invalid number of sides.")
# elif sides == "3":
#     print("The shape is a triangle.")
# elif sides == "4":
#     print("The shape is a square.")
# elif sides == "5":
#     print("The shape is a pentagon.")
# elif sides == "6":
#     print("The shape is a hexagon.")
# elif sides == "7":
#     print("The shape is a heptagon.")
# elif sides == "8":
#     print("The shape is a octagon.")
# elif sides == "9":
#     print("The shape is a enneagon.")
# elif sides == "10":
#     print("The shape is a decagon.")



#Exercise 38: Month Name to Number of Days
# month = input("Enter a month: ").lower()
# if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
#     print("31 days")
# elif month == "april" or month == "june" or month == "september" or month == "november":
#     print("30 days")
# elif month == "febuary":
#     print("28 or 29 days")
# else:
#     print("INVALID MONTH")



#Exercise 39: Sound Levels
# decibels = float(input("Enter the number of decibels: "))
# if decibels > 0 and decibels < 40:
#     print('quieter than a quiet room.')
# elif decibels == 40:
#     print('about the same as a quiet room.')
# elif decibels > 40 and decibels < 70:
#     print('quieter than an alarm clock.')
# elif decibels == 70:
#     print('about the same as an alarm clock.')
# elif decibels > 70 and decibels < 106:
#     print('quieter than a lawn mower.')
# elif decibels == 106:
#     ('about the same as a lawn mower.')
# elif decibels > 106 and decibels < 130:
#     print(" quieter than a jackhammer.")
# elif decibels == 130:
#     print('about the same as a jackhammer.')
# elif decibels > 130:
#     print('way too loud.')
# else:
#     print('Please enter a correct data value.')
#     print('Your sound level is')



#Exercise 40: Name that Triangle
# print("Input lengths of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
# if x == y == z:
# 	print("Equilateral triangle")
# elif x==y or y==z or z==x:
# 	print("isosceles triangle")
# else:
# 	print("Scalene triangle")



#Exercise 43: Faces on Money
# valid_names = "George Washington Thomas Jefferson Abraham Lincoln Alexander Hamilton Andrew Jackson Ulysses S. Grant Benjamin Franklin".lower()
# name = input("Please enter name: ")
# if name not in valid_names:
#     print("Not on a bill.")
# elif name == "george washington":
#     print("George Washington is on the $1 bill")
# elif name == "thomas jefferson":
#     print("Thomas Jefferson is on the $2 bill.")
# elif name == "abraham lincoln":
#     print("Abraham Lincoln is on the $5 bill")
# elif name == "alexander hamilton":
#     print("Alexander Hamilton is on the $10 bill")
# elif name == "andrew jackson":
#     print("Andrew Jackson is on the $20 bill.")
# elif name == "ulysses s. grant":
#     print("Ulysses S. Grant is on the $50 bill.")
# elif name == "benjamin franklin":
#     print("Benjamin Franklin is on the $100 bill.")



#Exersise 44: Date to holiday Name
# valid_months = "january febuary march april".split(" ")
# month = input("Enter a month: ").lower()
# if month not in valid_months:
#     print("INVALID MONTH")
# day = int(input("Enter a day: "))
# if month == "january" and day == 1:
#     print("New year's day is that day.")
# elif month == "july" and day == 1:
#     print("That day is Canada Day!")
# elif month == "december" and day == 25:
#     print("That is Christmas Day!")
# else:
#     print("There is no holiday that day.")



# Exersise 46: Seasons from Month and Day
# month = input("Input the month (e.g. January, February etc.): ")
# day = int(input("Input the day: "))
# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'
# if (month == 'March') and (day > 19):
# 	season = 'spring'
# elif (month == 'June') and (day > 20):
# 	season = 'summer'
# elif (month == 'September') and (day > 21):
# 	season = 'autumn'
# elif (month == 'December') and (day > 20):
# 	season = 'winter'
# print("Season is",season)



################Coding bat

# hello_name:
# name = str(input("Please enter name: "))
# print("Hello " + str(name))

# make_abba:
# def make_abba(a: str, b: str) -> str:
#   return a + b + b + a

# result = make_abba("What", "Up")
# print(result)

# make_tags:
# def make_tags(tag: str, word: str) -> str:
#   return "<" + tag + ">" + word + "</" + tag + ">"

# result = make_tags('i', 'Yay')
# print(result)

# make_out_word:
# def make_out_word(out: str, word: str) -> str:
#     return out[:2] + word + out[2:]


# result = make_out_word('<<>>', 'Yay')
# print(result)

# extra_end:
# def extra_end(string: str) -> str:
#     return out[-2:] * 3

# result = extra_end('Hello')
# print(result)


# first_two:
# def first_two(string: str) -> str:
#     if len(str) <= 2:
#         return str
#         return str[:2]


# result = first_two('Hello')
# print(result)

# first_half:
# def first_half(string: str) -> str:
#     return str[:len(str)/2]


# result = first_half('WooHoo')
# print(result)


# without_end:
# def without_end(string: str) -> str:
#     return str[1:-1]


# result = without_end('Hello')
# print(result)


# combo_string:
# def combo_string(a: str, b: str) -> str:
#     if len(a) > len(b):
#        return b + a + b
#        return a + b + a


# result = combo_string('Hello', 'hi')
# print(result)

# non_start:
# def non_start(a: str, b: str) -> str:
#     return a[1:] + b[1:]

# left2:
#     def left2(str):
#         return str[2:] + str[:2]


# result = non_start('Hello', 'There')
# print(result)
