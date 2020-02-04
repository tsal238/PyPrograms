#author: Taahir Saloojee

import glob
import os
import shutil


class Filescraper:
    def __init__(self,path):
        self.path= path

    #Gives list of everything in directory
    def listDirectory(self):
      print("**** These are your files/folders in path (%s)  **** \n"% self.path)
      list1 = os.listdir(self.path)
      for i in range(0,len(list1)):
        print("%d. %s"% (i, list1[i]))
    
    # check if directory exists
    def exists(self):
      bool1=os.path.exists(self.path)
      if bool1== True :
        pass
      else: 
        raise FileNotFoundError

    #Gives list of specific files within directory with specific file extention
    def list_files_ext(self):
        fileType=input("enter file type: ")
        listOffiles = glob.glob(self.path+"\*"+fileType)
        if len(listOffiles)== 0 :
          print("there are no files of type %s"% fileType)
        else:
            print("**** These are your files in path (%s) of type %s **** \n"% (self.path,fileType))
            for i in listOffiles:
               print(i)

    #move specific file    
    def moveFile(self):
        source=input("file path: ")
        destination = input("destination path: ")
        shutil.move(source , destination)
        print("your file %s has been moved to %s"%(source,destination))

    #order files alphabetically and group together based on filetypes and store in folder
    def group_files_based_ext(self):
        fileType= input("enter file extension: ")
        newFolder= input("enter new directory name: ")
        list1=glob.glob(self.path+"\*"+fileType) 
        length = len(self.path)
        newList= []
        for i in list1:
            newList+=[i[length+1:]]
        newList=sorted(newList)
        newPath = self.path+"\\"+newFolder
        os.mkdir(newPath)
        for i in  newList:
            path1 = self.path + "\\" + i
            path2 = newPath +"\\"+ i
            shutil.move(path1,path2)
        print("Files have been moved to %s"%newFolder)
    
    #order all files and folders in alphabetical order and store in folder
    def order(self):
      directory = self.path
      files = os.listdir(directory)
      ext_files = []
      folders = []
      for i in files:
        if "." in i and i.find(".")!=0:
          ext_files.append((i.lower(),i))
        elif i.find(".")==0:
          ext_files.append((i[1:].lower(),i))
        else:
          folders.append((i.lower(),i))
      sorted_dir = sorted(folders) + sorted(ext_files)
      newPath= self.path+"\\"+ "temp"
      os.mkdir(newPath)
      for i in sorted_dir:
            path1 = self.path + "\\" + i[1]
            path2 = newPath +"\\"+ i[1]
            shutil.move(path1,path2)
      
    #group files with same name but different extension in to a new folder
    def group_files_dif_ext(self):
      fileName = input("enter file name: ")
      folderName = input("enter new folder name: ")
      newPath = self.path+"\\"+folderName
      list1 = os.listdir(self.path)
      os.mkdir(newPath)
      for i in list1:
        if "." in i:
          k=i.find(".")
          if fileName == i[:k]:
            path1 = self.path + "\\" + i
            path2 = newPath +"\\"+ i
            shutil.move(path1,path2)
            
def validOperations():
    print("\n**** operations you can perform on files **** \n\n-help gives all operations \n-go (order files and group them based on file extention) \n-lsdir (list all files and folders in directory)\n-lsf (list all files of same file type)\n-m (move file)\n-order (orders all files and folders in alphabetical order)\n-exit (close application)")         

#create filescraper object
def create():
  path=input("enter path: ")
  file1= Filescraper(path)  
  return(file1) 

def func(op,file1):
  try:
          if op == "lsf":
            file1.list_files_ext()

          elif op == "order":
            file1.order()
          
          elif op == "lsdir":
            file1.listDirectory()
          
          elif op == "group":
            file1.group_files_dif_ext()
    
          elif op == "m":
            file1.moveFile()

          elif op == "help":
            validOperations()

          elif op == "go":
            file1.group_files_based_ext()

          elif op =="exit":
             n = False
             return n
          else:
              print("operation was not recognised!")
  except FileNotFoundError:
            print("A FileNotFoundError has occured, No such file or directory ")
            func(op,file1)

def functions(file1):

    n=True
    try:
       file1.exists()
       while (n):
          funcUsed =input("enter operation: -")
          if func(funcUsed,file1) == False:
            n = False

    except FileNotFoundError:
            print("A FileNotFoundError has occured, No such file or directory ")
            k=create()
            functions(k)
    except Exception as ex:
            print(ex)
            functions(file1)

def main():
    file1=create()
    validOperations()
    functions(file1)
main()