try:
    for i in range(1, 6):
        for j in range(1, 6):
            print('+', end=" ")
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name}]:{ex}')