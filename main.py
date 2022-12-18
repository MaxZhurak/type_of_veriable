try:
    start = int(input('start->'))
    end = int(input('end->'))
    counter = 0
    for i in range(start, end+1):
        if i % 5 ==0:
            print(i,end=' ')
            counter+=1
    print()
    print(counter)
except Exception as es:
    print(f'Eror: {ex}')
    print(f'Name: {ex.__class__.__name__}')