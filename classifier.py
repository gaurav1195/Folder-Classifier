#************Folder Clssifier**********************************************#
#********author: Gaurav Agarwal gauravagarwal.110695@gmail.com*************#                                                                     #
#                                                                          #
#**************************************************************************#
import os
import shutil
dir = 'C:/Users/gaurav/Downloads'
print(os.listdir(dir))
for file in os.listdir(dir):
        if '.py' in file:
                if not os.path.exists('E:/python'):
                        os.makedirs('E:/python')
                        shutil.move(dir + '/' + file, 'E:/python')
                else:
                        shutil.move(dir + '/' + file, 'E:/python')
              #  print('Helllo')
for file in os.listdir(dir):
        if '.pdf' in file or '.doc' in file or '.csv' in file or '.ppt' in file:
                if not os.path.exists('E:/docs'):
                        os.makedirs('E:/docs')
                        shutil.move(dir + '/' + file, 'E:/docs')
                else:
                        shutil.move(dir + '/' + file, 'E:/docs')

for file in os.listdir(dir):
        if '.exe' in file or '.msi' in file:
                if not os.path.exists('E:/Setups'):
                        os.makedirs('E:/Setups')
                        shutil.move(dir + '/' + file, 'E:/Setups')
                else:
                        shutil.move(dir + '/' + file, 'E:/Setups')
 

