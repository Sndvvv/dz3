import math
def summ(s1: int, s2: int) -> int:
        return int(s1)+int(s2)
def sub(s1: int, s2: int) -> int:
        return int(s1)-int(s2)
def mul(s1: int, s2: int) -> int:
        return int(s1)*int(s2)
def div(s1: int, s2: int) -> int:
        return int(s1)/int(s2)
def mod(s1: int, s2: int) -> int:
        return int(s1)%int(s2)
def pow(s1: int, s2: int) -> int:
        return int(s1)**int(s2)
def fact(s1: int) -> int:
        if int(s1) == 0 or int(s1) ==1:
            return 1
        else: return int(s1)*fact(int(s1)-1)
def root(s1: int) ->float:
         return math.sqrt(int(s1))
def tan(s1) -> float:
        return math.tan(float(s1)-1)
print('Доступные операции:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Возведение в степень')
print('6. Факториал')
print('7. Квадратный корень')
print('8. Тангенс угла')
print('(exit для выхода)')
print('---------------------------')
while True:
    opt = input('Операция:')
    if opt != 'exit':
        if opt == '1':
            s1 = (input('Слогаемое 1:'))
            s2 = (input('Слогаемое 2:'))
            if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                print(f'>>>{summ(s1,s2)}')
                print('---------------------------')
            else: raise ValueError('Значения должны быть целочисленными')
        elif opt == '2':
            s1 = (input('Уменьшаемое:'))
            s2 = ((input('Вычитаемое:')))
            if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                print(f'>>>{sub(s1,s2)}')
                print('---------------------------')
            else:
                raise ValueError('Значения должны быть целочисленными')
        elif opt == '3':
            s1 = (input('Множитель 1:'))
            s2 = (input('Множитель 2:'))
            if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                print(f'>>>{mul(s1, s2)}')
                print('---------------------------')
            else:
                raise ValueError('Значения должны быть целочисленными')
        elif opt == '4':
            print('1. Целочисленное деление:')
            print('2. Остаточное деление:')
            div_opt = input('Выберите действие')
            if div_opt == '1':
                s1 = (input('Делимое:'))
                s2 = (input('Делитель:'))
                if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                    if s2 != 0:
                        print(f'>>>{div(s1,s2)}')
                        print('---------------------------')
                    else: raise ZeroDivisionError('Делить на ноль нельзя')
                else:
                    raise ValueError('Значения должны быть целочисленными')
            elif div_opt == '2':
                s1 = (input('Делимое:'))
                s2 = (input('Делитель:'))
                if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                    if s2 != 0:
                        print(f'>>>{mod(s1,s2)}')
                        print('---------------------------')
                    else: raise ZeroDivisionError('Делить на ноль нельзя')
                else:
                    raise ValueError('Значения должны быть целочисленными')
        elif opt == '5':
            s1 = (input('Число:'))
            s2 = (input('Степень:'))
            if s1.lstrip('-').isdigit() and s2.lstrip('-').isdigit():
                print(f'>>>{pow(s1,s2)}')
                print('---------------------------')
            else:
                raise ValueError('Значения должны быть целочисленными')
        elif opt == '6':
            s1 = (input('Число:'))
            if s1.lstrip('-').isdigit():
                print(f'>>>{fact(s1)}')
                print('---------------------------')
            else:
                raise ValueError('Значения должны быть целочисленными')
        elif opt == '7':
            s1 = (input('Число:'))
            if s1.lstrip('-').isdigit():
                if int(s1) >= 0:
                    print(f'>>>{root(s1)}')
                    print('---------------------------')
                else: raise ValueError("Число не может быть отрицательным")
            else:
                raise ValueError('Значения должны быть целочисленными')
        elif opt == '8':
            s1 = (input('Угол::'))
            if s1.lstrip('-').isdigit():
                print(f'>>>{tan(s1)}')
                print('---------------------------')
            else:
                raise ValueError('Значения должны быть целочисленными')
        else: print('Выберите действие из списка')
    else: break



