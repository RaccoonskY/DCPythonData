def hello_person(p_name=str(), p_age=None, p_greeting="Добро пожаловать"):
    if not p_name.isalpha():
        print("Неверный ввод. Введите имя без цифр")
        return 0
    print(f"Имя: {p_name}\nВозраст: {p_age}\n{p_greeting},{p_name}")


while True:
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    greeting = input("Введите приветствие: ")
    hello_person(name, age, greeting)
    cont = input("Продолжить?")
    if cont.lower() in ["нет","no"]:
        break
