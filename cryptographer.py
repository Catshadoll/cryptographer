ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"

language = input("Выберите язык - RU/EN: ").upper()
if language == "RU":
    alphabet = ALPHABET_RU
elif language == "EN":
    alphabet = ALPHABET_EN
else:
    print("Ошибка: язык должен быть RU или EN")
    exit()

message = input("Введите сообщение: ").lower()
step = int(input("Введите шаг сдвига: "))
result = ""

chipher = [alphabet.find(symbol) + step for symbol in message]
print(chipher)

decrypted = "".join([alphabet[number - step] for number in chipher])
print(f"Вы отправили: {decrypted}")