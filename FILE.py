#FILE HANDLING
#TYPES OF FILES->IMAGE,TEXT,AUDIO,EXECUTABLE
#TYPES OF FILES IN PYTHON->BINARY(WHICH IS NOT TEXT),TEXT
#OPERATIONS->CRUD(CREATION,READING,UPDATION,DELETING)
#CREATE->OPEN->UPDATE->CLOSE

#OPEN() FUNCTION->OPEN(FILENAME,MODE)
#MODES->DEFAULT MODE:READ ;
#READ("r")-OPENS A FILE FOR READING.ERROR IF THE FILE DOESNT EXIST
#APPEND("a")-OPENS A FILE FOR APPENDING,CREATES A FILE IF IT DOESNT EXIST
#WRITE("w")-OPENS A FILE FOR WRITING,CREATES A FILE IF DOESNT EXIST
#CREATE("x")-CREATES THE SPECIFIED FILE,RETURNS ERROR IF THE FILE EXISTS
# USED WITH MODES:-
# "t"->text file
# "b"->binary file


#READ() FUNCTION
import os
file=open("C:/Users/jasmi/Desktop/NOTES PROGRAMMING/Machine Learning AI/ROADMAP/Difference between AI Engineer and Data Scienctist.txt","r")
print(file.read())
file.close()



file=open("C:/Users/jasmi/Desktop/NOTES PROGRAMMING/Machine Learning AI/ROADMAP/Difference between AI Engineer and Data Scienctist.txt","r")
print(file.read(5))
file.close()
# file1=open("files/understanding_files.txt","x")
# file1.close()
import os
file1=open("files/understanding_files.txt", "r")
# print(file1.readline())
# print(file1.readline())#line by line output
# print(file1.readline(3)) #reads only line 3
# print(file1.readlines()) #read lines seperately
file1.close()

"""LOOPING OVER A FILE OBJECT"""
file1=open("files/understanding_files.txt", "r")
for line in file1:
    print(line)
file.close()

"""WRITING TO A FILE"""
f=open("files/understanding_files2.txt", "w")
f.write("hey new file\n")
f.write("jas")
f.close()

f1=open("files/understanding_files2.txt", "a")
f1.write("appended")
f1.close()



"""DELETING A FILE"""
# os.remove("files/understanding_files2.txt") #to remove files
# import shutil
# shutil.rmtree("files")     #removing folders
# os.rmdir("files")           #removes directory only when empty
# # Checking if the file exists
# if os.path.exists("files/understanding_files.txt"):
#     os.remove("files/understanding_files.txt")
# else:
#     print("file does not exist")
#




"""LIBRARY,MODULE,PACKAGES"""#->library->packages->modules(modules are files)