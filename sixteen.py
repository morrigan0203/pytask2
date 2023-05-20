num: int = int(input("Введите число:  "))
num1 = num
res: str = ' '
while num > 0:
    between = num % 16
    if between > 9:
        match between:
            case 10: between = 'a'
            case 11: between = 'b'
            case 12: between = 'c'
            case 13: between = 'd'
            case 14: between = 'e'
            case 15: between = 'f'

    res = str(between) + res
    num //= 16
print(res)

print(f'{num1:0x}')
