import os
import shutil
 


"""
###Sort func
Moves files into respective folders according to their extensions
"""


def sort(path):

    list_ = os.listdir(path)
    os.chdir(path)
    crt = os.getcwd()
    print (crt)
	
    #Traverses to every file

    for filename in list_:
        name,ext = os.path.splitext(filename)
        ext = ext[1:]
        if ext == '':
            continue
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        

"""
###Extract
Gets  all the files from all the sub folders to root directory.
"""

def extract(path):
    #Set path as current working directory
    os.chdir(path)
    dest_dir = os.getcwd()
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
     
    rem_dirs = walker
     
    for data in walker:
        for files in data[2]:
            try:
                shutil.move(data[0] + os.sep + files, dest_dir)
                print(data[0] + os.sep + files)
            except shutil.Error:
    # to be on the safer side
                continue
"""
###Delete
Delete any empty folders after extraction or otherwise
"""

def delete(path):
    os.chdir(path)
    path = os.getcwd()
    for (_path, _dirs, _files) in os.walk(path, topdown=False):
		# skip remove
        if _files: continue 
        try:
            os.rmdir(_path)
            print('Remove :', _path)
        except OSError as e:
            print('Error :', e)

"""
####Func calls
"""
path = input("Enter the full path to the folder")
print ("Enter your choice\n\t1: Extract\n\t2: Delete\n\t3: Sort\n\t0: EXIT")
choice = int(input())
while (choice != 0):
    print ("Enter your choice\n\t1: Extract\n\t2: Delete\n\t3: Sort")
    if choice == 1:
        extract(path)
        print("Extracted all files from all subfolders")
    elif choice == 2:
        delete(path)
        print("Deleted all empty folders")
    elif choice == 3:
        sort(path)
        print("sorted all files into respective folders")
    choice = int(input())




