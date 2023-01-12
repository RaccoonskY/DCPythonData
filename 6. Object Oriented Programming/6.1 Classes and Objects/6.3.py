"""Реализуйте класс Event, который отвечает за событие в календаре. Экземпляр класса имеет два атрибута: описание
события и дату события. Внутри класса реализуйте метод, который конвертирует строку в объект класса Event. Метод
получает на вход строку вида ‘description * dd-mm-yyyy’. """


class Event:
    def __init__(self, desc, date):
        self.description = desc
        self.date = date

    @classmethod
    def from_string(cls, user_input):
        formated_input = str(user_input).split(" * ")
        description = formated_input[0]
        date = formated_input[1]
        return cls(description, date)

    def __str__(self):
        date = str(self.date).split("-")
        return f"Event\n{self.description}\nat day:{date[0]} month:{date[1]} year:{date[2]}"


event = Event.from_string("NEW EVENT * 30-11-2001")
print(event)
