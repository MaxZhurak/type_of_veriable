try:
 begin = int(input('begin->'))
 end = int(input('end->'))
 for item in reversed(range(begin, end+1)):
     print(item, end = " ")

except ValueError as vl_ex:#
 print(f'ValueError: {vl_ex}')
except Exception as ex:
    print(f'Eror: {ex}')
   print(f'Name: {ex.__class__.__name__}')