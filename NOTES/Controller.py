from bisect import insort
#import User_interface as ui
import Logger as log
#import Metod as met
from os import system



def start_Notes():

    start_text_log = 'Старт приложения заметки'
    log.log_data(start_text_log)
    new_start=True
    

    while True:
        
        # Вывод меню в консоль
        system ('cls')
        welcome_text = '''
                Приложение заметки
        Введите число в соответствие с типом операции
        0 - Вывод заметок в консоль
        1 - Добавить заметку
        2 - Поиск заметки
        3 - Редактировать заметку
        4 - Удалить заметку
        5 - Выход из приложения\n
        Введите число => '''
            
        working_mode=input(welcome_text)
        log.log_data('Пользователь ввёл '+ working_mode)        
            
        

        if working_mode=='0': # Вывод заметок в консоль.
            system ('cls')
            print ('Вывод заметок в консоль')
            log.log_data('Пользователь выбрал пункт меню вывод заметок в консоль')
            #met.output_data_console_menu()
            
        
        elif working_mode=='1': # Добавление заметок 
            system ('cls')
            print ('Добавить заметку')
            log.log_data('Пользователь выбрал пункт меню добавить заметку')
            #met.add_data_menu()
            
        
        elif working_mode=='2': # Поиск заметок
            system ('cls')
            print ('Поиск заметок')
            log.log_data('Пользователь выбрал пункт меню поиск заметки')
            #met.search_data_menu()
            
        
        elif working_mode=='3': # Редактирование заметок
            system ('cls')
            print ('Редактирование заметки')
            log.log_data('Пользователь выбрал пункт меню редактировать заметку')
            #met.del_data_menu()
            

        elif working_mode=='4': # Удаление заметок
            system ('cls')
            print ('удаление заметки')
            log.log_data('Пользователь выбрал пункт меню удалить заметку')
            #met.change_data_menu()
            
        
        elif working_mode=='5': # Выход из приложение 
            system ('cls')
            print ('Выход из приложения заметки')
            log.log_data('Пользователь выбрал меню выход из приложения\n\n')
            break
           
        

        
        else: # Цикличность миню
            continue