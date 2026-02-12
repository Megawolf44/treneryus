'''
Docstring для example

Важно, не использовать команду print(f'{os.system("tasskill /im autohotkey.exe)}')с
другими процессами, используйте только для завершения процесса AHK. ЭТО МОЖЕТ ПРИВЕЗТИ К ПРОБЛЕМАМ.
'''
from ahk import AHK
import os

def my_callback(): 
    print(f'{os.system("taskkill /im autohotkey.exe")}')

ahk = AHK() 

ahk.add_hotkey('^n', callback=my_callback)
ahk.start_hotkeys()
ahk.block_forever()

'''
Если хотите использовать другие клавиши для завершения:
Чтобы изменить горячую клавишу на "Ctrl + N" в вашем коде, вы должна заменить #n на ^n, где ^ обозначает клавишу
ahk.add_hotkey('^n', callback=my_callback)   



''' 