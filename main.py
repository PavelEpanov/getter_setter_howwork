# class Person:
#     def __init__(self, name):
#         self.__name = name # Имя человека
#         self.__age = 1 # Возраст человека
#
#     def set_age(self, age):
#         if 1 < age < 100:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     def get_age(self):
#         return self.__age
#
#
#     def display_intro(self):
#         print(f"Age is: {self.__age}, Name is {self.__name}")
#
# tom = Person("Tom")
# tom.set_age(101)
# tom.display_intro()

class Person:
    def __init__(self, name):
        self.__name = name # Имя человека
        self.__age = 1 # Возраст человека

    @property # Возвращение
    def age(self):
        return self.__age

    @age.setter # Условие на возврат
    def age(self, age):
        if 1 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_intro(self):
        print(f"Age is: {self.__age}, Name is {self.__name}")

tom = Person("Tom")
tom.age = 45
tom.display_intro()