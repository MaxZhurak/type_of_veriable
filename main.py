x=float(input("x->"))
y=float(input("y->"))
z=float(input("z->"))
print('#>-----------<Menu>--------------------#')
print(f'|+: Show   + for {x} and {y} and {z} |')
print(f'|*: Show  * for {x} and {y}  and {z} |')
print(f'|/: Show avg for {x} and {y}  and {z} |')
print('#>-----------<Menu>--------------------#')
action = input('action->')
if action == '+':
    print(f'{x} + {y} + {z}= (x + y + z')
elif action == '*':
    print(f'{x} * {y} * {z}= {x * y * z}')
elif action == '/':
    print(f'{x}+{y}+{z}/{2}= {x+y+z/2}')