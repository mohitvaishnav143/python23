
import os
import shutil

path1="C:/Users/MOHIT VAISHANAV/Downloads/C102_assets-main/C102_assets-main/11/"
path2="C:/Users/MOHIT VAISHANAV/Downloads/C102_assets-main/C102_assets-main/101/"



source = os.listdir(path1)
print(source)


for path3 in source:
  root, extension = os.path.splitext(path3)
  
  if extension == '':
    continue
  if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path4 = path1 + '/' + path3                           
        path5 = path2 + '/' + "Document_Files" + '/' + path3 
        path6 = path2 + '/' + "Document_Files"   


     
        if os.path.exists(path5):
          print("Moving " + path3 + ".....")

          # Move from path1 ---> path3
          shutil.move(path4, path6)

        else:
          os.makedirs(path5)
          print("Moving " + path6 + ".....")
          shutil.move(path4, path6)

        