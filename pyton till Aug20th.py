def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print(fizz_buzz(5))


def num_of_sublists(lst):
    return str(lst).count('[') - 1


print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))


def adds_n(n):
    return lambda x: n + x


adds1 = adds_n(1)

print(adds1(3.5))

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}


def greeting(name):
    if name in GUEST_LIST:
        return "Hi! I'm " + name + ", and I'm from " + GUEST_LIST[name] + "."
    else:
        return "Hi! I'm a guest."


print(greeting("Randy"))


def harmonic(n):
    return round(sum([1/i for i in range(1, n+1)]), 3)


print(harmonic(5))


def progress_days(runs):
    return sum([1 for i in range(len(runs)-1) if runs[i+1] > runs[i]])


print(progress_days([10, 11, 12, 9, 10]))