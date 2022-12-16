try:
 begin = int(input('begin->'))
 end = int(input('end->'))
 for item in range(begin, end+1):
    if item % 2 != 0:
     print(item, end = " ")
