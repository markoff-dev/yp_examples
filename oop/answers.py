"""Константы в Python?
В отличие от некоторых других языков, в Питоне нет возможности объявить
неизменяему переменную. Для обозначения переменных, значения которых не должны 
меняться существует договорённость именовать их прописными буквами.
"""
# MY_CONSTANT = 'моя «константа»'
# print(MY_CONSTANT)
# # > моя «константа»
# MY_CONSTANT = 'беспрепятственно изменяем значение константы'
# print(MY_CONSTANT)
# > беспрепятственно изменяем значение константы


"""Область видимости. Что такое локальные и глобальные переменные?
В Python, переменные, на которые только ссылаются внутри функции/метода, 
считаются глобальными. Если переменной присваивается новое значение где-либо в 
теле функции/метода, считается, что она локальная, и, если вам нужно, то нужно явно 
указывать её глобальной.
"""
# y = 1
# def my_func():
#     print(y)
#     x = y
#     print(x)
#     # y = 5
#     print(y)
#     global z
#     z = 10
#
# my_func()
# print(z)


"""Что такое self и для чего он нужен?
Параметр self в данном случае это ссылка на конкретный экземпляр класса и 
нужен для того, чтобы объект мог обратиться к собственным методам или 
свойствам: self.имя_свойства. 
__dict__ в данном случае выведит все локальные свойства и методы относящиеся к
объекту в отношении которого он вызывается.
"""
# class Point:
#     def setCoords(self):
#         # Выведем список локальных переменных self
#         print(self.__dict__)
#         print(self.x, self.y)
#
#
# # Создаём (инстанцируем) экземпляр (объект) класса Point
# object_point = Point()
# object_point1 = Point()
# object_point3 = Point()
# # Создаём локальные переменные.
# object_point.x = 5
# object_point.y = 10
#
# Point.setCoords(object_point)
#
# # Обращаемся к методу через созданный объект object_point, в данном случае в
# # self ссылка на объект object_point попадёт автоматически.
# object_point.setCoords()
# # Обращаемся к методу через имя класса,
# # в данном случае в self ссылка на объект object_point попадёт в явном виде.
# Point.setCoords(object_point)


"""Для чего нужен super()? 
Функция super используется если мы переопределяем 
у ребёнка метод, который был у родителя, но хотим чтобы логика родителя 
осталась, мы вызываем super, тем самым говоря интерпретатору питона: возьми 
у родителя следующий метод (или атрибут). В примере, функцией super() мы  
вызываем родительский конструктор внутри дочернего класса тем самым получая 
доступ к его свойствам. Делается это для того чтобы не укаказывать 
(переписывать свойства). Через super() таким образом можно обратится к любому 
методу или свойству родителя, за исключением приватных (__)"""
class Computer:
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

    def __del__(self):
        print(1)

x = Computer('PC', '256', '100')


#
#
# class Laptop(Computer):
#     def __init__(self, computer, ram, ssd, model):
#         super().__init__(computer, ram, ssd)
#         self.model = model
#
#
# lenovo = Laptop('lenovo', 2, 512, 'l420')
# print('This computer is:', lenovo.computer)
# print('This computer has ram of', lenovo.ram)
# print('This computer has ssd of', lenovo.ssd)
# print('This computer has this model:', lenovo.model)


"""Зчем нужна конструкция if __name__ == '__main__':?
Её основное назначение — разделение кода, который будет выполнятся при 
вызове кода как модуля (при импортировании его в другой скрипт) — и при 
запуске самого модуля, как отдельного файла. Для того чтобы убедится что 
func1() выполнится а func() не выполнится при импорте запустите # Script 2 из 
файла import_script.py
"""
# print('Script 1. My name is: %s' % __name__)
# print('This is simple code from script 1')
#
#
# def func():
#     print('This is code from function from script 1 using construction '
#           'if __name__ == "__main__"')
#
#
# def func1():
#     print('This is code from function from script 1 NOT using construction '
#           'if __name__ == "__main__"')
#
#
# func1()
#
# if __name__ == "__main__":
#     func()


"""Разница между атрибутами класса, атрибутами экземпляра?
Атрибуты класса одинаковы для всех экземпляров класса, тогда как атрибуты
экземпляров являются особыми для каждого экземпляра. Атрибуты экземпляра
предназначены для данных, специфичных для каждого экземпляра и атрибутов
класса, которые должны использоваться всеми экземплярами класса.
"Методы экземпляра" - это специфические атрибуты класса, которые принимают
экземпляр класса как первый атрибут и предполагают манипулировать этим экземпляром.
"Методы класса" - это методы, определенные в классе, которые принимают
класс как первый атрибут не экземпляр (поэтому методы класса).
Вы можете легко увидеть атрибуты класса, обратившись к A.__ dict__:.
"""
# class A:
#     class_attribute = 10
#
#     def class_method(self):
#         self.instance_attribute = 'I am instance attribute'
#
#
# print(A.__dict__)
# # {'__module__': '__main__', 'class_attribute': 10,
# # 'class_method': <function A.class_method at 0x00000267C0A7A160>,
# # '__dict__': <attribute '__dict__' of 'A' objects>,
# # '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
#
# a = A()
# a.class_method()
# a.class_attribute = 11
# print(a.__dict__)
# # {'instance_attribute': 'I am instance attribute', 'class_attribute': 11}


# Полезные ссылки
"""
Что такое классы в Python:
https://python-scripts.com/python-class

Как работают классы в Python:
https://medium.com/@melevir/%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%8E%D1%82-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B-%D0%B2-python-f8ba90fe2f8e

Вот тут с примерами можно почитать что такое self и для чего он нужен 
https://pyneng.readthedocs.io/ru/latest/book/25_oop_basics/parameter_self.html
"""
record1 = Record(amount=145, comment='кофе')
cash_calculator.add_record("record1")


