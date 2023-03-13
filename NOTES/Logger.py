from datetime import datetime


def log_data(text_log):

    folder = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\PO\NOTES\LogNotes.txt'


    with open( folder, 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.now()}:  {text_log}\n')
        