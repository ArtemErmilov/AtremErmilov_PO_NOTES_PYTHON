# Определение уникального ID
import Logger as logg
import File_links as fl

def new_id (text_log):
    file=fl.file_links('file_ID')
    while True:
        try:
            data=open(file,'r',encoding='utf-8')
            for line in data:
                id_old=line
            data.close

            new_id=str(int(id_old)+1)

            with open (file,'w',encoding='utf-8') as data:
                data.write(new_id)
            logg.log_data(text_log+new_id)
            return new_id
        except:
             new_id='0'
             with open (file,'w',encoding='utf-8') as data:
                 data.write(new_id)
             continue
        
           
