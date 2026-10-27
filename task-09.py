def dashain_banner(func):
    def wrapper(*args, **kwargs):
        print("*** Happy Dashain ***")
        result = func(*args, **kwargs)
        print("*********************")
        return result
    return wrapper
@dashain_banner
def greet(name, gift="tika"):
    print(f"{name} gets a {gift}!")
greet("Sita")
greet("Ram", gift="kite")
def countdown(n):
    if n == 0:
        print("Tika day!")
        return
    print(f"{n} days left")
    countdown(n - 1)

countdown(3)
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(f"Digit sum: {sum_digits(2026)}")
def token_machine(start):
    n = start
    while True:
        yield f"T-{n}"
        n += 1
tokens = token_machine(101)
print(f"{next(tokens)} {next(tokens)} {next(tokens)}")
squares_sum = sum(i**2 for i in range(1, 6))
print(f"Sum of squares: {squares_sum}")