from pathlib import Path
import os

def Create_Folder():
    try: 
       name = input("Enter the folder name you want to create: ")
       path = Path(name)
       path.mkdir()
    except Exception as err:
        print(f"Sorry an error occurred: {err}")

def read_filefolder():
    path = Path("")
    items =list(path.rglob("*"))
    for i,item in enumerate(items):
        print(f"{i+1}. {item}")

def update_Folder():
    read_filefolder()
    old_name = input("Enter the folder name you want to update: ")
    path = Path(old_name)
    try:
        if path.exists() and path.is_dir():
            new_name = input("Enter the new folder name: ")
            new_path = path.parent / new_name
            path.rename(new_path)
        else:
            print("The specified folder does not exist.")
    except Exception as err:
        print(f"Sorry an error occurred: {err}")
        
def Delete_folder():
    read_filefolder()
    name = input("Enter the folder name you want to delete: ")
    path = Path(name)
    try:
        if path.exists() and path.is_dir():
            os.rmdir(path)
        else:
            print("The specified folder does not exist.")
    except Exception as err:
        print(f"Sorry an error occurred: {err}")

print("Options :-")

print("1. Create a folder")
print("2. Read a file or Folder")
print("3. Update a folder")
print("4. Delete a folder")

choice =int(input("Choose an option from the above menu: "))

if choice == 1: 
    Create_Folder()
elif choice == 2:
    read_filefolder()
elif choice == 3:
    update_Folder()
else:
    Delete_folder()
