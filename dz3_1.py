def mult_numb(numbers: list[int | str], mult: int = 2) -> list[int]:
    return [x * mult for x in numbers]
MultNumbLamb = lambda numbers, mult=2: list(map(lambda num: num * mult, numbers))
print('Введите числа через пробел:')
numbers1 = input()
try: numbers = list(map(int, numbers1.split()))
except ValueError: numbers = list(map(str, numbers1.split()))
print('Введите множитель(по умолчанию:2):')
mult = input()
try: mult = int(mult)
except ValueError:
    mult = 2
print(mult_numb(numbers, mult))
print(MultNumbLamb(numbers, mult))
