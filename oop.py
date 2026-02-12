# 1. Что такое класс(самое базовое)
"""
Docstring для oop
Класс - это чертеж или шаблон для создания объектов.
         Аналогия:
Класс - рецепт пирога
Объект = конкретный испечённый пирог по этому рецепту
"""
class Pie: # ← это класс (чертеж) Пирог
    def __init__(self, filling): # конструктор пfiling(подача)

        self.filling = filling # отрибут объекта

        self.ready = False # ready(готовый)

    def bake(self):   # Метод bake(печь)
        self.ready = True
        print(f"Пирог с {self.filling} испечен!")
# Создаем объекты (пироги)
applesauce = Pie("яблоко")  # объект 1
cherry = Pie("вишня")  # объект 2

applesauce.bake()
print(cherry.ready)
cherry.bake()
"""
2. Основные элементы класса (все до одной мелочи)

Элемент                         что это                              обязателен?            Пример
▬▬▬▬▬▬▬▬                       ▬▬▬▬▬▬▬▬▬                            ▬▬▬▬▬▬▬▬▬▬▬            ▬▬▬▬▬▬▬
class Имя:                  объявление класса                           Да               class Машина:

init(self,...)            конструктор - вызывается при              почти всегда      def init(self,цвет,год):
                          создании объекта

self                     ссылка на текущий объект                      Да             self.цвет = цвет

атрибуты                 переменные, уникальные для                     ▬             self.цвет, self.скорость
экземпляра               каждого объекта

методы                   функции внутри класса                         ▬             def ехать(self):...

атрибуты класса          общие бля всех объектов класса                 нет           калёса = 4

@classmethod            метод класса(работает с классом)                нет          @classmethod def из цвета(cls, c);

@staticmethod          Обычная функция внутри класса                    нет          @saticmethod def сигнал():...
"""

# ▬▬▬ 3. Наследование (подклассы) - самое главное
"""
Подкласс(дочерний класс)наследует все от родительского класса и может:
• использовать его атрибуты и методы
• переопределять (переписывать )их 
• доюовляь свои

▬▬▬▬▬▬ АНАЛОГИЯ ▬☻▬▬☻
Родитель = "Транспортное средство"
Подкласс = "Автомобиль" 
"""

class Transport:  # родительский класс (базовый)
    def __init__(self, speed):
        self.speed = speed
        self.engine_running = False # engine(двигатель) running(работает) 

    def started(self): # started(начатый)
        self.engine_running = True
        print('Двигатель заведён')

    def drive(self):
        if self.engine_running:
            print(f'Едим со скоростью {self.speed} км/ч')
        else:
            print("Сначала заведи двигатель")
class Car(Transport): # подкласс наследует от Транспорт
    def __init__(self, speed, collor, model):
        super().__init__(speed)  # Вызываем конструктор родителя
        self.collor = collor
        self.model = model
        self.door_open = False

        # Переопределяем (override)метод родителя
    def drive(self):
        if self.engine_running:
            print(f"{self.model} {self.collor} цвета едет со скоростью {self.speed} км/ч")

        else:

           print("Завиди двигатель, лентяй! ")
        '''    
    def open_the_dor(self):
        self.engine_running = True
        print("Двери открыты")
        '''
# Использование
'''
lada = Car(180, "Синий", "Lada Vesta")
lada.started()  # от родителя
lada.drive()    # переопределенный метод
lada.open_the_dor()   # свой метод
'''
# 4. Ключевые слова и конструкции наследования(все в одной)

'''
Конструкция                     Что делает                                           Когда используется
▬▬▬▬▬▬▬▬▬▬▬                     ▬▬▬▬▬▬▬▬▬▬▬                                          ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
class                      Дочерний наследует всё от Родитель                     всегда при наследовании
Дочерний(Родитель) 

super().init(...)          вызывает конструктор родителя                         почти всегда в init дочернего

super().метод()           вызывает метод родителя(если переопределили)          когда нужно дополнить, а не заменить

isinstance(obj, Класс)    проверяет,является ли obj экземпляром                 isinstance(lada,Транспорт)→ True
                               Класса или его потомком

issubclass(Доч, Род)      проверяет, является ли Доч подклассом Род             issubclass(Автомобиль,Транспорт)→ True

'''
# 5. Множественное наследование (очень важное понимание)
'''

class flying: # летающий
    def fly(self): # лететь
        print('Лечу!')
class floating:    # Плавающий
    def to_sail(self): # Плыть
        print('Плыву')     

class amphibian(flying, floating): # Амфибия наследует от двух родителей
    pass
    
amfibia = amphibian()
amfibia.fly()     # Лечу
amfibia.to_sail() # Плыву

# ▬▬▬▬▬▬▬☻ Порядок наследования важен (MRO-Method Resolution Order)

print(amphibian.mro()) # [<class '__main__.amphibian'>, <class '__main__.flying'>, <class '__main__.floating'>, <class 'object'>]
'''

# 6. Полиморфизм(один из столпов ООП)

# Один и тот же метод у разных классов делает разные вещи

def make_them_go(vehcle): # Заставить ехать
    vehcle.drive()   #один вызов - разные реализации

lada = Car(180, "синий", "Lada")
truck = Transport(90)

lada.started()  # Заводим двигатель
truck.started()

make_them_go(lada)     # Lada синий цвет едет...
make_them_go(truck)    # Едем со скоростью 90км/ч



# 7. Инкапсуляция (защита данных)
# В Python нет строгой приватности, но есть договоренности

class bank:
    def __init__(self):
        self.balanc = 1000   # Публичный
        self._pin = 1234    # защищенный (по договоренности)
        self.__sikret = 'пороль'  # приватный (имя меняется на _Банк__секрет)
    def get_a_secret(self):
        return self.__sikret 

# 8. Абстрактные классы(если хочешь запретить создание экземпляров)

from abc import ABC, abstractclassmethod
class figure(ABC):
    @abstractclassmethod
    def square(self):
        pass
class a_circle(figure):
    def __init__(self, r):
        
        self.r = r
    def square(self):
        return 3.14 * self.r ** 2



class Car:
    def __init__(self, collor, speed, model):
        self.collor = collor
        self.speed = speed
        self.madel = model
    
    def drive(self):
        print(f"{self.madel} {self.collor} цвета едит со скоростью {self.speed} км/ч")
        # Теперь создаем машину 

ferrari = Car("Красная", 300, "Фиррари")
bmw = Car("Синяя", 250, "BMW")

ferrari.drive()
bmw.drive()
'''
Что мы получили:

• Один раз написали шаблон (класс Машинка)
• Много раз создали машинки (объекты)
• Каждая машинка знает свой цвет, скорость, марку
• Каждая умеет ехать (метод поехать)

Самые важные 5 предложений, которые нужно запомнить

• Класс — это рецепт / чертёж / шаблон.
• Объект — это конкретная вещь, сделанная по этому чертежу.
• self — это слово, которое значит «я сам» (эта конкретная машинка).
• __init__ — это то, что происходит, когда мы создаём новую машинку (задаём ей свойства).
• Метод — это действие, которое умеет делать каждая машинка (поехать, затормозить, посигналить).
'''

# Самый маленький код, который ты можешь запустить прямо сейчас

class Cat:
    def __init__(self, name, collor, years, sleep):
        self.name = name 
        self.collor = collor
        self.years = years
        self.sleep = sleep
    def meow(self):
        print(f'{self.name} ({self.collor})ему {self.years} лет говорит: Мяу-Мяу! {self.sleep}' )

myrzik = Cat('Мурзик', 'серый', 5, 'любит спать')
barsik = Cat('Барсик', 'рыжий', 4 , 'ложится спать') 

myrzik.meow()
barsik.meow()
'''

class Car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color


    def print_info(self):
        return print (f"{self.name} is {self.color}")


niva = Car('Хантер', 'Мокрый асвальт')
lamba = Car('Авентодор', 'Оранжевый')        
    
niva.print_info()
'''