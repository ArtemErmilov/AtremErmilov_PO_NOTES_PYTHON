from bisect import insort
import datetime
#import User_interface as ui
import Logger as log
import Metod as met
from os import system



def start_Notes():

    start_text_log = '\n\nСтарт приложения заметки'
    log.log_data(start_text_log)
    new_start=True
    

    while True:
        dat = datetime.tzinfo
        
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
        5 - Выход из приложения
    
        Введите число => '''
            
        working_mode=input(welcome_text)
        log.log_data('Пользователь ввёл '+ working_mode)        
            
        

        if working_mode=='0': # Вывод заметок в консоль.
            system ('cls')
            print ('Вывод всех заметок в консоль\n')
            log.log_data('Пользователь выбрал пункт меню вывод всех заметок в консоль')
            met.output_notes()
            
        
        elif working_mode=='1': # Добавление заметок 
            system ('cls')
            print ('Добавить заметку\n')
            log.log_data('Пользователь выбрал пункт меню добавить заметку')
            met.add_data_notice()
            
        
        elif working_mode=='2': # Поиск заметок
            system ('cls')
            print ('Поиск заметок\n')
            log.log_data('Пользователь выбрал пункт меню поиск заметки')
            met.note_search()
            
        
        elif working_mode=='3': # Редактирование заметок
            system ('cls')
            print ('Редактирование заметки\n')
            log.log_data('Пользователь выбрал пункт меню редактировать заметку')
            met.editing_notes()
            

        elif working_mode=='4': # Удаление заметок
            system ('cls')
            print ('Удаление заметки\n')
            log.log_data('Пользователь выбрал пункт меню удалить заметку')
            met.remove_notes()
            
        
        elif working_mode=='5': # Выход из приложение 
            system ('cls')
            print ('Выход из приложения заметки\n')
            log.log_data('Пользователь выбрал меню выход из приложения\n\n')
            break
           
        

        
        else: # Цикличность миню
            continue