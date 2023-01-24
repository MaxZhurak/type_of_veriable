try:
    number = int(input('number->'))
    for i in range(1, 10+1):
        for j in range(1, 10+1):
                print(f'{i} * {j} = {i*j}', end="\t\t")
        print()
        for j in range(1, 161):
                print(f'-', end="")
        print()
    print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name}]:{ex}')