import os
import shutil

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
                if file.endswith('.csv') and not os.path.exists(os.path.join(path, 'CSV FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'CSV FILES', file))
                    
                elif file.endswith(('.jpeg', '.jpg', '.png', '.gif')) and not os.path.exists(os.path.join(path, 'IMAGE FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'IMAGE FILES', file))
                    
                elif file.endswith('.txt') and not os.path.exists(os.path.join(path, 'TEXT FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'TEXT FILES', file))
                    
                elif file.endswith(('.xlsx', '.xls')) and not os.path.exists(os.path.join(path, 'EXCEL FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'EXCEL FILES', file))
                    
                elif file.endswith(('.doc', '.docx')) and not os.path.exists(os.path.join(path, 'WORD FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'WORD FILES', file))
                    
                elif file.endswith(('.ppt', '.pptx')) and not os.path.exists(os.path.join(path, 'PPT FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'PPT FILES', file))
                    
                elif file.endswith('.py') and not os.path.exists(os.path.join(path, 'PYTHON FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'PYTHON FILES', file))
                    
                elif file.endswith('.pdf') and not os.path.exists(os.path.join(path, 'PDF FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'PDF FILES', file))
                    
                elif file.endswith('.mp3') and not os.path.exists(os.path.join(path, 'AUDIO FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'AUDIO FILES', file))
                    
                elif file.endswith('.mp4') and not os.path.exists(os.path.join(path, 'VIDEO FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'VIDEO FILES', file))
                    
                elif file.endswith('.html') and not os.path.exists(os.path.join(path, 'WEB FILES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'WEB FILES', file))
                    
                elif file.endswith(('.zip', '.tar', '.gz', '.rar')) and not os.path.exists(os.path.join(path, 'ARCHIVES', file)):
                    shutil.move(os.path.join(path, file), os.path.join(path, 'ARCHIVES', file))
                    
            flag = False
        else:
            print(' \t The path provided doesn\'t exist.')
            print('\n \t Please enter a valid file path (e.g., "/Users/YourName/Documents/file.txt") \n ')
            path = input('Please enter the path where your files are stored: ')

    print(' \n \t File sorting is complete. All files have been organized into their respective folders. \n ')

except Exception as e:
    print('Error ->', e)
