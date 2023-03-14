import Logger as logg

def input_number (text_out:str, text_alarm:str = 'Число введено неправильно, введите его заново'):
    """
    Метод проверки на правильность ввода числа.
    text_out - текст, для вывода в консоль при запросе числа
    text_alarm - текст для для вывода при неправильном вводе.
    """
    
    while (True):
        try:
            number = int(input(text_out))
            return number
        except:
            logg.log_data(f'Число {number} введено не правильно, будет повторёна ввод')
            print (text_alarm)
            continue

def input_number_exit (text_out:str, text_alarm:str = 'Число введено неправильно, введите его заново'):
    """
    Метод проверки на правильность ввода числа.
    text_out - текст, для вывода в консоль при запросе числа.
    text_alarm - текст для для вывода при неправильном вводе.
    Если пользователь ввёл 'e' то нет проверки на правильность ввода чисел

    """
    number = input(text_out)

    if (number=='e'): # Если пользователь ввёл e то нет проверки на правильность ввода чисел
        return number, True
    
    else:    
        while (True):
            try:
                number = int(number)
                return number, False
            except:
                logg.log_data(f'Число {number} введено не правильно, будет повторёна ввод')
                print (text_alarm)
                continue