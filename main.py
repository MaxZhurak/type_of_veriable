try:
    lenght = int(input('length->'))
    sign = input('sign->')
    for i in range(0, lenght):
        print(sign, end='')
except Exception as es:
    print(f'Eror: {ex}')
    print(f'Name: {ex.__class__.__name__}')