# ---------- Function 1 ----------
def seconds_to_hms(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

seconds = int(input("Function 1 - Enter seconds: "))
print(seconds_to_hms(seconds))
print()


# ---------- Function 2 ----------
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return round(fahrenheit, 2)

celsius = float(input("Function 2 - Enter temperature in Celsius: "))
print(celsius_to_fahrenheit(celsius))
print()


# ---------- Function 3 ----------
def split_evenly(total, people):
    per_person = total // people
    remainder = total % people
    return per_person, remainder

total = int(input("Function 3 - Enter total amount: "))
people = int(input("Function 3 - Enter number of people: "))
print(split_evenly(total, people))
print()


# ---------- Function 4 ----------
def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0
    while i < len(words):
        result += words[i][0].upper()
        i += 1
    return result

full_name = input("Function 4 - Enter your full name: ")
print(initials(full_name))
print()


# ---------- Function 5 ----------
def is_palindrome_word(word):
    clean_word = word.strip().lower()
    return clean_word == clean_word[::-1]

word = input("Function 5 - Enter a word: ")
print(is_palindrome_word(word))
print()


# ---------- Function 6 ----------
def mask_email(email):
    at_index = email.index('@')
    num_stars = at_index - 1
    return email[0] + ("*" * num_stars) + email[at_index:]

email = input("Function 6 - Enter your email: ")
print(mask_email(email))
print()


# ---------- Function 7 ----------
def middle(values):
    length = len(values)
    mid = length // 2
    if length % 2 != 0:
        return values[mid : mid + 1]
    else:
        return values[mid - 1 : mid + 1]

text = input("Function 7 - Enter numbers separated by spaces: ")
values = [int(x) for x in text.split()]
print(middle(values))
print()


# ---------- Function 8 ----------
def rotate_left(values, k):
    if not values:
        return values
    k = k % len(values)
    return values[k:] + values[:k]

text = input("Function 8 - Enter numbers separated by spaces: ")
nums = [int(x) for x in text.split()]
k = int(input("Function 8 - Enter how many steps to rotate: "))
print(rotate_left(nums, k))
print()


# ---------- Function 9 ----------
def fib_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    a, b = 0, 1
    while len(fib) < n:
        a, b = b, a + b
        fib.append(b)
    return fib

n = int(input("Function 9 - How many Fibonacci numbers? "))
print(fib_list(n))
print()


# ---------- Function 10 ----------
def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        steps += 1
    return steps

n = int(input("Function 10 - Enter a positive number: "))
print(collatz_steps(n))