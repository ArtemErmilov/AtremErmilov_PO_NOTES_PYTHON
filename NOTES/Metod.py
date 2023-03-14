import json
#import User_interface as ui
import ID_definition as id_def
import Check as ch
import Logger as logg
import File_links as fl
from datetime import datetime



def write_json (data_write, path_file_json): 
    """
    Запись данных в файл формата json
    data_write - данные, которые необходимо записать в json.
    path_file_json - путь к файлу json
    """
    try:
        data = json.load(open(path_file_json, encoding='utf8')) # Чтение файла json
    except:
        data = [] # Если файла не существует, то запись пустого массива

    data.append(data_write) # Добавление новых данных в конец файла

    with open(path_file_json, 'w', encoding='utf8') as file: # запись данных в json файл
        json.dump(data, file, ensure_ascii=False, indent=4,separators=(', ', ': '))

def reading_json(path_file_json):
    """
    Чтение файла json.
    path_file_json - путь к файлу json
    data - данные, прочитанные с файла json
    """
    try: # Чтение файла
        with open(path_file_json, encoding='utf8') as file:
            data=json.load(file)
    except: # Вывод предупреждения если файл отсутствует 
        print('Файла не существует')
        data = []
    return data




def add_data_notice(): #Создание новой заметки
    """
    Создание новой заметки.
    file_json - путь, где должен быть сохранён json файл
    id - ID заметки
    time - время создание заметки
    name - название заметки
    notice - заметка
    save - выбор, сохранить или нет заметку
    """  
    file_json=fl.file_links('file_json') # путь, где должен быть сохранён json файл
    


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
        
            # with open(file_new, 'w', encoding='utf8') as file: # запись данных в json файл
            #     #file.write(json.dumps(person_dict, ensure_ascii=False, indent=4,separators=(', ', ': ')))
            #     json.dump(person_dict, file, ensure_ascii=False, indent=4,separators=(', ', ': '))
            write_json(person_dict,file_json)
            break
        
        elif (save=='n'): 
            logg.log_data('Пользователь выбрал не сохранять заметку') # логирование
            break # Заметка не сохранена

        else: continue


def output_notes (): 
    """
    Метод вывода заметок в консоль.
    file_json - путь к файлу json.
    data - данные которые необходимо вывести в консоль.
    """

    file_json=fl.file_links('file_json') # путь к файлу json
    
    
    data = reading_json(file_json) # Получение данных из json

    for d in data:# Вывод данных в консоль
        print(d)

    a = input('Для выхода нажмите Enter')


def note_search():
    """
    Метод поиска по ID или названию заметки и 
    вывод найденного в консоль.
    """

    file_json=fl.file_links('file_json') # путь к файлу json
    
    data = reading_json(file_json) # Получение данных из json

        
    while(True):

        working_mode = str(input ('\nПоиск заметки по:\n1 - По ID\n2 - По названию\nВведите число => '))

        logg.log_data(f'Пользователь ввёл: {working_mode}') # логирование

        data = reading_json (file_json) # Чтение данных из json файла

        temp_bool = False # Временная переменная

        if (working_mode == '1'): # Поиск по ID
            
            search_ID = str(ch.input_number('Введите ID для поиска: ')) # Ввод ID для поиска

            logg.log_data(f'Пользователь ввёл ID: {search_ID}') # логирование

            for dat in data: # Поиск
                if (dat['ID'] == search_ID): 
                    print(dat)
                    temp_bool = True
                    break

            if (temp_bool==False): # Если ID не найден, то выводиться предупреждение.
                print(f'Запись с ID = {search_ID} ненайдена!')
                logg.log_data(f'Запись с ID = {search_ID} ненайдена!') # логирование
            
            a = input ('Для выхода нажмите Enter') # Выход из подменю в основное меню
            
            break

        elif (working_mode == '2'): # Поиск по названию заметки

            search_name = str(input ('Введите название заметки для поиска: ')) # Ввод название заметки для поиска

            logg.log_data(f'Пользователь ввёл название заметки: {search_name}') # логирование

            for dat in data: # Поиск 
                if (dat['Name'] == search_name): 
                    print(dat)
                    temp_bool = True

            if (temp_bool==False): # Если название заметки не найден, то выводиться предупреждение.
                print(f'Заметка с название {search_name} ненайдена!')
                logg.log_data(f'Заметка с название {search_name} ненайдена!') # логирование
            
            a = input ('Для выхода нажмите Enter') # Выход из подменю в основное меню

            break

        else: continue