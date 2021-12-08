import os,shutil 
folders = {
    'videos':['.mp4'],
    'audios':['.wav','.mp3'],
    'images':['.JPEG','.png'],
    'documents':['.docx','.xlsx','.xls','.pdf',".zip",".rar",".TIF"],
}

def rename_folder():
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder)) == True:
            os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))

def create_move(ext,file_name):
    find = False
    for folder_name in folders:  
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
            find = True
            break 
    if find != True:
        if other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,other_name))

directry = 'C:\\Users\\Deepak vengatesan\\Desktop\\python\\sort_files\\data_files'
other_name = input("Enter the other name of the unknown file : ")
rename_folder()
#input("Enter the locaiton :")
all_files = os.listdir(directry)
lenght = len(all_files)
count = 1
# print(all_files)

    # if os.path.isfile(directry+"\\"+i) == True:
for i in all_files:
    if os.path.isfile(os.path.join(directry,i)) == True:
        create_move(i.split(".")[-1],i)
    print(f"Total Files: {lenght}| Done: {count} | Left: {lenght-count}")
        # print("yes")
    count+=1 