text = input("Введіть текст: ")
num_sentences = text.count('.') + text.count('!') + text.count('?')
print(f"Кількість пропозицій у тексті: {num_sentences}")