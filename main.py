x=float(input("x->"))
print('#>----------------<Menu>------------------#')
print(f'|mile: Show mile for {x} and {0.6}       |')
print(f'|inches: Show inches for {x} and {35.37} |')
print(f'|yards: Show yards for {x} and {0.9}     |')
print('#>----------------<Menu>------------------#')
action = input('action->')
if action == 'mile':
    print(f'{x} * {0.6}= {x * 0.6}')
elif action == 'inches':
    print(f'{x} * {35.37}= {x * 35.37}')
elif action == 'yards':
    print(f'{x} * {0.9}= {x*0.9}')