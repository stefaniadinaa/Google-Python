# Exercitiul 1
def my_function(*arg):
    sum = 0
    for item in arg:
        if isinstance(item, int) or isinstance(item, float):
            sum = sum + item

    return sum

# Exercitiul 2 a

def suma_nr(n):
    if n == 0:
        return 0

    return n + suma_nr(n - 1)
# Exercitiul 2 b
def suma_nr_pare(n):
    if n == 0:
        return 0

    if n % 2 == 0:
        return n + suma_nr_pare(n - 1)
    else:
        return suma_nr_pare(n - 1)
# Exercitiul 2 c
def suma_nr_impare(n):
    if n == 0:
        return 0

    if n % 2 != 0:
        return n + suma_nr_impare(n - 1)
    else:
        return suma_nr_impare(n - 1)

def readf():
    input1 = input("Scrie ceva: ")
    while input1 is not int:
        try:
            input1 = int(input("Scrie un numar: "))
            break
        except ValueError:
            print('0')

print(readf())
