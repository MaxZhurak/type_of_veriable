try:
    number = 0
    sum = 0
    min = 0
    max = 0
    triger = True
    while True:
        number = int(input('number->'))
        if number == 7:
            break
        else:
            if triger:
                min_ = max_ = number
                triger = False
            else:
                sum += number
                if max < number:
                    max = number
                if min > number:
                    min = number
    print(f'Sum = {sum}')
    print(f'Min = {min}')
    print(f'Max = {max}')
except Exception as es:
    print(f'Error [{ex.__class__.__name__}]: {ex}')