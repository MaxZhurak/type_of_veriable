x=float(input("x->"))
y=float(input("y->"))
print('#>-----------<Menu>------------#')
print(f'|+ : Show  sum for {x} and {y} |')
print(f'|- : Show  dif for {x} and {y} |')
print(f'|*: Show  mul for {x} and {y}  |')
print(f'|/ : Show dif for {x} and {y}  |')
print(f'|avg : Show avg for {x} and {y}|')
print('#>-----------<Menu>------------#')
action = input('action->')
if action == '+':
    print(f'{x} + {y} = {x + y}')
elif action == '*':
    print(f'{x} - {y} = {x * y}')
elif action == '/':
 if x == 0 or y == 0:
    print(f"Error! {x} or {y} is zero!")
else:
    print(f'{x}/ {y} = {x/y}')
    print(f'Avg = {(x+y)/2}')