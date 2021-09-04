pi = 3.14
radius = 2
area = pi * (radius ** 2)
print(area)

area = pi * (radius ** 2)
print(area)
radius = radius + 1
area = pi * (radius ** 2)
print(area)

radius = radius + 1
print(area)  # area doesn't change
area = pi * (radius ** 2)
print(area)

a_very_long_variable_name_dont_name_them_this_long_pls = 0

cube = 27
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)

cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

cube = 27
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

cube = 27
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Cube root of", cube, "is", guess)

hi = "hello there"
name = "ana"
greet = hi + name
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name) * 3
print(silly)

cube = 27
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)

cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

cube = 27
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

cube = 27
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Cube root of", cube, "is", guess)

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

s = "demo loops"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


def is_even(i):
    """
    input i positive int
    Returns true if i is even, otherwise false
    """
    print("inside is even")
    return i%2 == 0

print(is_even(5))