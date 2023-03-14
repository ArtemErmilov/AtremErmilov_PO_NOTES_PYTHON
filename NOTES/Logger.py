from datetime import datetime
import File_links as fl


def log_data(text_log):

    folder = fl.file_links('file_logg')


    with open( folder, 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.now()}:  {text_log}\n')
        