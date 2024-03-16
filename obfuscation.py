import random
import os
import subprocess

class notObvs:
    global key
    

    def __init__(self,file):
        self.file = file
        with open("save.txt", "w") as f:
            f.write(self.file)
    
        fileP = open("save.txt","r")
        self.FileN = fileP.read()
        self.key = random.randint(1,10)


    def transfer(self):
        tempWrite = open(self.FileN, "w")
        tempWrite.write('from obfuscation import notObvs\nd1 = notObvs("sample.py")\n\n')
        tempWrite.write('d1.decode("""\n') 
        with open("...txt", "r") as tempRead:
            for i in tempRead.read():
                tempWrite.write(i)
        tempWrite.write('""")')
        tempWrite.write(f"#{self.key}")
        os.remove("...txt")


    def encode(self):   
        with open(self.FileN, "r") as file:
            for i in file.readlines():
                for j in i:
                    if j != " " and j != "\n":
                        ordchr = ord(j)+self.key
                        if ordchr == 32:
                            ordchr+=1
                        strchr = chr(ordchr)
                        with open("...txt", "a") as tempWrite:
                            tempWrite.write(strchr)
                    else:
                        with open("...txt", "a") as tempWrite:
                            tempWrite.write(j)
        self.transfer()


    def getKey(self):
        with open(self.FileN,"r") as read:
            x = read.read()
            x = x[-1]
            return int(x)
    

    def kill(self):
        file_path = "...py"
        if os.path.exists(file_path):
            result = subprocess.run(["python", file_path], capture_output=True, text=True)
            os.remove(file_path)
        else:
            print("Python file does not exist.")

 
    def decode(self,string):   
        key = self.getKey()
        tempWrite = open("...py","w")
        for i in string:
            if i != " " and i != "\n":
                ordchr = ord(i)-key
                strchr = chr(ordchr)
                tempWrite.write(strchr)
            else:
                tempWrite.write(i)
        
        self.kill()



















