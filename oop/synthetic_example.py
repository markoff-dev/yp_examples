"""Пример реализации наследования"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     def voice(self):
#         print('ИгоГо')
#
# jack = Horse('Jack')
# jack.voice()


"""Пример реализации множественного наследования"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     pass
#
#
# class Donkey(Animal):
#     pass
#
#
# class Mule(Horse, Donkey):
#     pass
#
#
# ia = Mule('Ia')
# ia.voice()
# print(Mule.__mro__)



"""Пример полиморфизм"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     def voice(self):
#         return 1 + 1
#
#
# class Donkey(Animal):
#     def voice(self):
#         print('Иа Иа')
#
#
# jack = Horse('Jack')
# jack.voice()
#
# stefan = Donkey('Stefan')
# stefan.voice()



"""Пример инкапсуляция"""
# class Animal:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def voice(self):
#         print('ИгоГо')
#
#
# class Horse(Animal):
#     def voice(self):
#         self.voice()
#
#     def __get_age(self):
#         print(self.age)
#
#     def _get_weight(self):
#         print(self.weight)
#
#
# jack = Horse('Jack', 6, 220)
# jack.__get_age()
# jack.__get_weight() # Попытка обращения к методу вызовет ошибку.
# jack._Horse__get_weight()  # Обход ограничения private

"""По инкапсуляции было больше всего вопросов, вот пояснение:

Инкапсуляция — ограничение доступа к составляющим объект компонентам
(методам и свойствам). Инкапсуляция делает некоторые из компонент доступными
только внутри класса.

Инкапсуляция в Python работает лишь на уровне соглашения между программистами
о том, какие атрибуты являются общедоступными, а какие — внутренними.

Одиночное подчеркивание (protected) в начале имени атрибута говорит о том, что
переменная или метод не предназначен для использования вне методов класса,
однако атрибут доступен по этому имени.

Двойное подчеркивание (private) в начале имени атрибута даёт большую защиту:
атрибут становится недоступным по этому имени.

В данном примере:
Метод _get_age() является protected, но мы можем к нему обращается через
объект или self. Программист, называя метод или свойство начиная с "_",
хочет сказать "лучше сюда не лезть".

Метод __get_weight() является private, и мы не можем к нему обращается через
объект или self вне класса где он был создан. Программист, называя метод или
свойство начиная с "__" полностью запрещает к нему доступ на уровне
интерпретатора.
jack.__get_weight() # Попытка обращения к методу вызовет ошибку.
Существует способ обойти private ограничение и вызвать __get_weight() так:
jack._Horse__get_weight()  # Но лучше этого не делать.
"""