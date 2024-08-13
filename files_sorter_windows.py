# AUTOMATIC FILE SORTER PROGRAM

import os, shutil

def pathcheck(path):  # TO CHECK IF FILE PATH EXISTS OR NOT.
    return os.path.exists(path)

############## MAIN PROGRAM ##############

flag = True

try:
    path = input('Please enter the path where your files are stored: ')
    
    while flag:
        if pathcheck(path):
            folder_names = ['CSV FILES', 'IMAGE FILES', 'TEXT FILES', 'EXCEL FILES', 'WORD FILES', 'PPT FILES',
                'PYTHON FILES', 'PDF FILES', 'ARCHIVES', 'AUDIO FILES', 'VIDEO FILES', 'WEB FILES']
            
            file_names = os.listdir(path)
            
            # CREATING FOLDERS IF THEY DO NOT EXIST
            for folder_name in folder_names:
                folder_path = os.path.join(path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
            
            # MOVING FILES TO RESPECTIVE FOLDERS

            for file in file_names:
                if '.csv' in file and not os.path.exists(path + '\\' + 'CSV FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'CSV FILES' + '\\' + file)
                    
                elif '.jpeg' in file or '.jpg' in file or '.png' in file or '.gif' in file and not os.path.exists(path + '\\' + 'IMAGE FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'IMAGE FILES' + '\\' + file)
                    
                elif '.txt' in file and not os.path.exists(path + '\\' + 'TEXT FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'TEXT FILES' + '\\' + file)
                    
                elif '.xlsx' in file or '.xls' in file and not os.path.exists(path + '\\' + 'EXCEL FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'EXCEL FILES' + '\\' + file)
                    
                elif '.doc' in file or '.docx' in file and not os.path.exists(path + '\\' + 'WORD FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'WORD FILES' + '\\' + file)
                    
                elif '.ppt' in file or '.pptx' in file and not os.path.exists(path + '\\' + 'PPT FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'PPT FILES' + '\\' + file)
                    
                elif '.py' in file and not os.path.exists(path + '\\' + 'PYTHON FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'PYTHON FILES' + '\\' + file)
                    
                elif '.pdf' in file and not os.path.exists(path + '\\' + 'PDF FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'PDF FILES' + '\\' + file)
                    
                elif '.mp3' in file and not os.path.exists(path + '\\' + 'AUDIO FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'AUDIO FILES' + '\\' + file)
                    
                elif '.mp4' in file and not os.path.exists(path + '\\' + 'VIDEO FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'VIDEO FILES' + '\\' + file)
                    
                elif '.html' in file and not os.path.exists(path + '\\' + 'WEB FILES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'WEB FILES' + '\\' + file)
                    
                elif '.zip' in file or '.tar' in file or '.gz' in file or '.rar' in file and not os.path.exists(path + '\\' + 'ARCHIVES' + '\\' + file):
                    shutil.move(path + '\\' + file, path + '\\' + 'ARCHIVES' + '\\' + file)
                    
            flag = False
        else:
            print(' \t The path provided doesn\'t exist.')
            print('\n \t Please enter a valid file path (e.g., "C:\\Users\\YourName\\Documents\\file.txt") \n ')
            path = input('Please enter the path where your files are stored: ')

    print(' \n \t File sorting is complete. All files have been organized into their respective folders. \n ')

except Exception as e:
    print('Error ->', e)