import random
import os

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
        tempWrite.write(f'from obfuscation import notObvs\nd1 = notObvs("{self.FileN}")\n\n')
        tempWrite.write('d1.decode("""\n') 
        with open("...txt", "r") as tempRead:
            for i in tempRead.read():
                tempWrite.write(i)
        tempWrite.write(f'""",{self.key})\nd1.run()')
        os.remove("...txt")

    def encode(self):  
        print(self.FileN) 
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

    def run(self):
        os.system("python3 ...py") #change to "python ...py" if on windows
        os.remove("...py")
        
    def decode(self,string,key):   
        tempWrite = open("...py","w")
        for i in string:
            if i != " " and i != "\n":
                ordchr = ord(i)-key
                strchr = chr(ordchr)
                tempWrite.write(strchr)
            else:
                tempWrite.write(i)



















