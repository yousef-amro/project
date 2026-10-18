
# Function 1: Classify Triangle

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("These sides cannot make a triangle")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"


print("Function 1")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


print(classify_triangle(a, b, c))

print()


# Function 2: Course Result

def course_result(coursework, final, attendance):
    if coursework < 0 or coursework > 40:
        raise ValueError("Coursework must be between 0 and 40")

    if final < 0 or final > 60:
        raise ValueError("Final must be between 0 and 60")

    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance must be between 0 and 100")

    if attendance < 75:
        return "Fail (low attendance)"

    total = coursework + final

    if total >= 50:
        return "Pass"
    else:
        return "Fail"


print("Function 2")
coursework = float(input("Enter coursework mark (0-40): "))
final = float(input("Enter final mark (0-60): "))
attendance = float(input("Enter attendance % (0-100): "))


print(course_result(coursework, final, attendance))
print()


# Function 3: FizzBuzz لو الرقم بيقبل القسمه على ٥ و ٣ يبقا الكلمتين لو ٣ اول كلمه لو ٥ تاني كلمه

def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0: #  if i % 5 == 0 and  if i % 3 == 0: ممكن كدا برضو
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


print("Function 3")
n = int(input("Enter n: "))
print(fizzbuzz(n))

print()


# Function 4: Check Prime Number

def is_prime(n):
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


print("Function 4")
n = int(input("Enter a number: "))
print(is_prime(n))

print()


# Function 5: Primes Below n

def primes_below(n):
    result = []

    for i in range(2, n):
        if is_prime(i):
            result.append(i)

    return result


print("Function 5")
n = int(input("Enter n: "))
print(primes_below(n))

print()


# Function 6: First Repeated Value

def first_repeated(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return values[i]

    return None


print("Function 6")
text = input("Enter numbers separated by spaces: ")
values = [int(x) for x in text.split()]

print(first_repeated(values))

print()


# Function 7: Count Pairs

def count_pairs(n):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            count += 1

    return count


print("Function 7")
n = int(input("Enter n: "))

print("Nested loop:", count_pairs(n))
print("Formula:", n * (n - 1) // 2)

print()


# Function 8: Calculator

def calculator(command):
    match command.split():
        case ["add", a, b]:
            return float(a) + float(b)

        case ["sub", a, b]:
            return float(a) - float(b)

        case ["mul", a, b]:
            return float(a) * float(b)

        case ["div", a, b]:
            return float(a) / float(b)

        case _:
            return "Unknown command"


print("Function 8")
command = input("Enter a command (example: add 2 3): ")
print(calculator(command))

print()


# Function 9: Parse Integer

def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default


print("Function 9")
text = input("Enter something: ")
print(parse_int(text))

print()


# Function 10: Statistics (Smallest and Biggest)

def stats(*numbers):
    if len(numbers) == 0:
        return None

    smallest = numbers[0]
    biggest = numbers[0]

    for x in numbers:
        if x < smallest:
            smallest = x

        if x > biggest:
            biggest = x

    return smallest, biggest


print("Function 10")
text = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in text.split()]

print(stats(*numbers))

print()


# Function 11: Append to List

def append_to(item, target=None):
    if target is None:
        target = []

    target.append(item)

    return target


print("Function 11")
item1 = input("Enter first item: ")
item2 = input("Enter second item: ")

print(append_to(item1))
print(append_to(item2))

print()


# Function 12: Make Multiplier

def make_multiplier(k):
    def multiply(x):
        return x * k

    return multiply


print("Function 12")
k = int(input("Enter k: "))
x = int(input("Enter x: "))

times_k = make_multiplier(k)

print(times_k(x))

print()


# Function 13: Apply Function n Times

def apply_n(f, x, n):
    for i in range(n):
        x = f(x)

    return x


print("Function 13")
x = int(input("Enter x: "))
n = int(input("Enter n (how many times): "))

double = make_multiplier(2)

print(apply_n(double, x, n))
