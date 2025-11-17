file_name = input("enter your file nameL:")
context = input("enter your context file :")

if not (file := open(r"./bin.txt", "w")): print("file not found")
print("File open successFully !")
file.write(f"file name : {file_name}\n context file: {context}\n")
print("Data written successfully !")
file.close()

