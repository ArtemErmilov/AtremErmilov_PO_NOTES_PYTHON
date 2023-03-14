

def file_links(text_file):
    path =r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\PO\NOTES'
    if text_file=='file_json':
        file =path+r'\DB_NOTES.json'
        #file =r'DB_NOTES.json'
        return file
    elif text_file=='file_ID':
        file =path+r'\ID_definiton.txt'
        #file =r'\ID_definiton.txt'
        return file
    elif text_file=='file_logg':
        file =path +r'\LogNotes.txt'
        #file =r'\LogNotes.txt'
        return file
   
    