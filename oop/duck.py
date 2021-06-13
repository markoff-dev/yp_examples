# Абстрактная утка
class Duck:
    def __init__(self, color, sex, age):
        # Привет, мы свойства класса.
        self.color = color
        self.sex = sex
        self.age = age  # Months.

    # Привет, мы методы класса.
    def say(self):
        # Обратите внимание на параметр self, который является ссылкой на
        # текущий объект (после его создания).
        print('Кря-Кря')

    def swim(self):
        print('Я плыву')

    def fly(self):
        if self.age > 10:
            print('Я лечу')
        else:
            print('Я ещё не умею летать')


# Создаём нашего Дональда == инстанцируем объект класса Утка.
donald = Duck('yellow', 'male', 2)
# Теперь через точку '.' мы можем обратиться к методам и свойствам нашего класса.
donald.swim()
donald.say()
donald.fly()
print(donald.color)
