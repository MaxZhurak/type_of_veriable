num = int(input("Введіть число: "))
st = int(input("Введіть степінь от 1 до 7:"))
if st > 7 or st < 0:
   print("Степінь повинен бути от 1 до 7")
else:
   print(num**st)