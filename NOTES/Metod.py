import json
#import User_interface as ui
import ID_definition as id_def
#import Check as ch
import Logger as logg
import File_links as fl
from datetime import datetime


def add_data_notice(): #Создание новой заметки
    """
    Создание новой заметки.
    file_new - путь, где должен быть сохранён json файл
    id - ID заметки
    time - время создание заметки
    name - название заметки
    notice - заметка
    save - выбор, сохранить или нет заметку
    """  
    file_new=fl.file_links('file_json') # путь, где должен быть сохранён json файл
    


    time = datetime.now() # время создание заметки
    time = str(time)

    name = input('Введите название заметки: ') # название заметки
    logg.log_data(f'Название заметки: {name}') # логирование

    notice = input('Введите текст заметки: ') # заметка
    logg.log_data(f'Текст заметки: {notice}') # логирование

       
    
    while(True):
        save = input('Если хотите сохранить заметку введите Y + Enter, Если нет то N + Enter.\n')# выбор, 
        #сохранить или нет заметку
        logg.log_data(f'При сохранение заметки пользователь ввёл: {save}') # логирование

        if (save=='y'):# Сохранение заметки

            logg.log_data('Пользователь выбрал сохранение заметки') # логирование

            id = id_def.new_id('ID заметки: ') # ID заметки
            
            person_dict = {'ID': id, 'Time': time, 'Name': name, 'Notice':notice} # структура json файла
        
            with open(file_new, 'a', encoding='utf8') as file: # запись данных в json файл
                #file.write(json.dumps(person_dict, ensure_ascii=False, indent=4,separators=(', ', ': ')))
                json.dump(person_dict, file, ensure_ascii=False, indent=4,separators=(', ', ': '))
            break
        
        elif (save=='n'): 
            logg.log_data('Пользователь выбрал не сохранять заметку') # логирование
            break # Заметка не сохранена

        else: continue


def output_notes (): # Метод вывода заметок в консоль
    file_json=fl.file_links('file_json') # путь, где должен быть сохранён json файл
    with open(file_json) as file:
        data=json.load(file)
    print(data)
    a = input('Для выхода нажмите Enter')