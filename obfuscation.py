import os
from Rules import Gen

global gen1
gen1 = Gen()

class notObvs:
        
    def __init__(self,file):
        self.file = file
        self.rule = gen1.id_generator()
        self.key = gen1.alg(self.rule)
        with open("save.txt","w") as x:
            x.write(f"key:{self.rule}")

    def transfer(self):
        tempWrite = open(self.file, "w")
        tempWrite.write(f'from obfuscation import notObvs\nd1 = notObvs("{self.file}")\nd1.decode("""') 
        
        with open("...txt", "r") as tempRead:
            for i in tempRead.read():
                tempWrite.write(i)
        tempWrite.write(f'""",)\nd1.run()')


        os.remove("...txt")



    def encode(self): 
        with open(self.file, "r") as file:
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

    def decode(self,string,rule="None"):
        if rule == "None" :
            rule = input("please enter a key: ")  

        ordchra = 0
        for i in rule:
            ordchra +=ord(i)
        key = round(ordchra//len(str(ordchra/3))/10)

        tempWrite = open("...py","w")
        for i in string:
            if i != " " and i != "\n":
                ordchr = ord(i)-key
                strchr = chr(ordchr)
                tempWrite.write(strchr)
            else:
                tempWrite.write(i)
