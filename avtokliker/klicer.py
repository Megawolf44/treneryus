# Первая команда pip install ahk  
# Вторая команда в терменале pip install "ahk[binary]"
# Врасширение установить AutoHotkey Plus
# скрипт которырй управляет нашей мышкой  
from ahk import AHK # Импорт класса из библиотеки AHK

ahk = AHK() # Создаем экземпляр класса

ahk.mouse_move(x=150, y=150, blocking=True) # координаты 100/100 передвигают мыш
ahk.mouse_move(x=300, y=300, speed=100, blocking=True)
print(ahk.mouse_position) # Вывод координат мыши в терминал



























