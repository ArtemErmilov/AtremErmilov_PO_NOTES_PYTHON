import json
#import User_interface as ui
import ID_definition as id_def
import Check as ch
import Logger as logg
import File_links as fl
from datetime import datetime



def write_json (data_write, path_file_json): 
    """
    Чтение и запись данных в файл формата json
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


def wr_json (data, path_file_json): 
    """
    Только запись данных в файл формата json
    data_write - данные, которые необходимо записать в json.
    path_file_json - путь к файлу json
    """
    
    with open(path_file_json, 'w', encoding='utf8') as file: # запись данных в json файл
        json.dump(data, file, ensure_ascii=False, indent=4,separators=(', ', ': '))




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

            id = id_def.s_new_id('ID заметки: ') # ID заметки
            
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

        working_mode = str(input ('\nПоиск заметки по:\n1 - По ID\n2 - По названию\n3-Выход из подменю поиск\nВведите число => '))

        logg.log_data(f'Пользователь ввёл: {working_mode}') # логирование


        temp_bool = False # Временная переменная

        if (working_mode == '1'): # Поиск по ID

            logg.log_data(f'Пользователь выбрал поиск по ID') # логирование

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

            logg.log_data(f'Пользователь выбрал поиск по имени заметки') # логирование

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
        elif (working_mode == '3'): # Выход из подменю поиск
            logg.log_data(f'Пользователь выбрал выход из подменю поиск') # логирование

        else: continue

def editing_notes():
    """
    Метод редактирование заметки в базе данных.
    """

    file_json=fl.file_links('file_json') # путь к файлу json

    text_in_ID = 'Введите ID заметки для редактирования.\nДля выхода из подменю редактирования введите "e" и Enter.\nВедите данные: '

    editing_ID,editing_notes_exit = ch.input_number_exit(text_in_ID) # ID заметки для редактирования 

    editing_ID = str(editing_ID)

    logg.log_data(f'Пользователь ввёл ID заметки для редактирования: {editing_ID}') # логирование

    data = reading_json(file_json) # Получение данных из json
    
    temp_bool = False

    if (editing_notes_exit==False):
        for d in data:
            if (d['ID']==editing_ID):
                temp_bool = True
                
                while (True):
                    print(d)
                    text_working_mode ='Выберите действия:\n1 - Редактирование названия заметки\n2 - Редактирование заметки\n3 - Выход из меню редактирования\nВведите число:'
                    working_mode = input(text_working_mode)# Выбор что будет редактироваться имя заметки или заметка
                    logg.log_data(f'Пользователь ввёл : {working_mode}') # логирование

                    if (working_mode=='1'): # Изменение названия заметки
                        logg.log_data(f'Пользователь выбрал изменить название заметки') # логирование
                        change_name = input('Введите новое название заметки: ') # Ввод нового имени заметки
                        logg.log_data(f'Пользователь ввёл новое название заметки: {change_name}') # логирование
                        
                        entry = input ('Для сохранения изменённых данных введите Y + Enter. Если нет N и Enter.\n')
                        if (entry == 'y' or entry == 'Y'):
                            logg.log_data(f'Пользователь сохранил изменение названия заметки') # логирование
                            d['Name'] = change_name
                            time = str(datetime.now()) # время изменения заметки
                            d['Time'] = time  # время создание заметки
                            wr_json (data, file_json)
                           
                        else:
                            logg.log_data(f'Пользователь не сохранил изменение названия заметки') # логирование
                        continue
                        

                    elif (working_mode=='2' ): # Изменение самой заметки
                        logg.log_data(f'Пользователь выбрал изменить заметку') # логирование
                        change_notice = input('Введите новую заметку: ') # Ввод новой заметки
                        logg.log_data(f'Пользователь ввёл новую заметку заметки: {change_notice}') # логирование
                        
                        entry = input ('Для сохранения изменённых данных введите Y + Enter. Если нет N и Enter.\n')
                        if (entry == 'y' or entry == 'Y'):
                            logg.log_data(f'Пользователь сохранил изменение в заметки') # логирование
                            d['Notice'] = change_notice # Новая заметка
                            time = str(datetime.now()) # время изменения заметки
                            d['Time'] = time # время изменения заметки
                            wr_json (data, file_json)
                            
                        else:
                            logg.log_data(f'Пользователь не сохранил изменение в заметки') # логирование
                        continue

                    elif (working_mode=='3' ): # Выход из подменю редактирования
                        break

                    else : continue
        if (temp_bool==False): # Вывод предупредительных сообщений, если ID не существует 
            print (f'Заметки с ID {editing_ID} не найдена')
            logg.log_data(f'Заметки с ID {editing_ID} не найдена') # логирование
            a = input ('Для продолжения нажмите Enter')
                

    logg.log_data(f'Пользователь выбрал выход из подменю редактирования') # логирование

def remove_notes ():
    """
    Метод удаления заметки из базы данных.
    """
    file_json=fl.file_links('file_json') # путь к файлу json

    text_in_ID = 'Введите ID заметки, которую необходимо удалить.\nДля выхода из подменю редактирования введите "e" и Enter.\nВедите данные: '
    
    editing_ID,editing_notes_exit = ch.input_number_exit(text_in_ID) # ID заметки для удаления                     

    editing_ID = str(editing_ID) # Преобразование введёны данных в формат str

    logg.log_data(f'Пользователь ввёл ID заметки для удаления: {editing_ID}') # логирование

    data = reading_json(file_json) # Получение данных из json

    new_data = [] # Новый словарь, куда будут записываться данные из старого без удаляемого словаря

    temp_bool = False

    if (editing_notes_exit == False): # Удаление заметки
        logg.log_data(f'Пользователь выбрал удаление заметки') # логирование

        for d in data: # Поиск заметки по ID
            if (d['ID']==editing_ID): # Нахождение заметки и вывод её в консоль
                
                temp_bool = True

                print(d) # Вывод удаляемой заметки в консоль
                
            else: new_data.append(d)
        
        if ( temp_bool == True): # Если ID существует, то выполняются действия подтверждения и удаления
        
            del_notes_EN = input ('Для подтверждения удаления введите Y + Enter. Для отмены любой символ и, или Enter.\n')
            
            if (del_notes_EN == 'y' or del_notes_EN=='Y'): # Удаление заметки

                logg.log_data(f'Пользователь подтвердил удаление заметки') # логирование

                wr_json(new_data,file_json) # Запись изменённого журнала в json файл

            else : logg.log_data(f'Пользователь отменил удаление заметки') # логирование
        
        else:
            print (f'Заметки с ID = {editing_ID} не найдена')
            logg.log_data(f'Заметки с ID = {editing_ID} не найдена') # логирование
            a = input ('Для продолжения нажмите Enter')
        
    else: logg.log_data(f'Пользователь вышел из подменю удалить заметку') # логирование

                