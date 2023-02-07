operators = {
   'Vodafone': 0.66,

   'Kyivstar': 0.45,

   'Lifecell': 0.76,
}
int(input("Введіть вартість розмови: ")), input("Виберіть оператор: "), input("Виберіть другий оператор: ")
if operators1 == operators2:
   print("Вартість розмови: ", cost)
else:
   print("Вартість розмови: ", cost * operators[operator1] + cost * operators[operator2])