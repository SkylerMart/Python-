import shutil
import os
#Part 1
#set where the source files are
source = 'C:/Users/Skyler/Desktop/Folder A/'

#set the destination path
destination = 'C:/Users/Skyler/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
        #we are saying move the files represented by 'i' to their destination
        shutil.move(source+i,destination)


    
