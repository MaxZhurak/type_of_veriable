try:
    start = int(input('start->'))
    end = int(input('end->'))
    sum = float(0)
    counter = 0
    for i in range(start, end+1):
        sum += i
        counter += 1
        print(counter)
    print(f'sum + {sum}, Avg = {sum} /  {counter} = {sum/counter}')
except Exception as es:
    print(f'Eror [{ex.__class__.__name__}]: {ex}')