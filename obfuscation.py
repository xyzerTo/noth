import os
from Rules import Gen

global gen1
gen1 = Gen()

#d1.id_generate() Creates a random string with a random length(rule)
#d1.alg() uses that "rule" to get a number(key)

# current cases: "txt", "py"

class notObvs:

    def transfer(self,fileN,case):
        if case == "py":
            tempWrite = open(fileN, "w")
            tempWrite.write(f'from obfuscation import notObvs\nd1 = notObvs()\nd1.decode("""') 
            with open("...txt", "r") as tempRead:
                for char in tempRead.read(): #Gets all the contents from the temporary file
                    tempWrite.write(char)    #writes and structures the content, in the main file based on the case
            tempWrite.write(f'""")\nd1.run()')
            os.remove("...txt")

        elif case == "txt":
            tempWriteT = open(fileN, "w")
            with open("...txt", "r") as tempRead:
                for char in tempRead.read():
                    tempWriteT.write(char)
           os.remove("...txt")
    
    def encode(self,fileN,case): 

        rule = gen1.rule_generator()
        key = gen1.alg(rule) 
        with open("save.txt","w") as x:
            x.write(f"{fileN} key:{rule}")

        with open(fileN, "r") as file:
            for line in file.readlines():   #iterate through each line in the file
                for char in line:            #iterate through each character in the line
                    if char != " " and char != "\n":
                        ordchr = ord(char)+key   #uses the key to obfuscate each character
                        if ordchr == 32:
                            ordchr+=1
                        strchr = chr(ordchr)
                        with open("...txt", "a") as tempWrite:
                            tempWrite.write(strchr)
                    else:
                        with open("...txt", "a") as tempWrite:
                            tempWrite.write(char)
        self.transfer(fileN,case)



    def run(self):
        os.system("python3 ...py") #change to "python ...py" if on windows
        os.remove("...py")

    def decode(self,string,case="py",rule="None",):
        if case == "py":
            tempWrite = open("...py","w")
            if rule == "None":
                rule = input("please enter a key: ")
            key = gen1.alg(rule)
            for char in string:
                if char != " " and char != "\n":
                    ordchr = ord(char)-key
                    strchr = chr(ordchr)
                    tempWrite.write(strchr)
                else:
                    tempWrite.write(char)

        if case == "txt":   
            if rule == "None":
                rule = input("please enter a key: ")
            key = gen1.alg(rule)
            tempRead = open(string,"r")
            with open("...txt","w") as tempWrite:
                for lines in tempRead.readlines():
                    for char in lines:
                        if char != " " and char != "\n":
                            ordchr = ord(char)-key
                            strchr = chr(ordchr)
                            tempWrite.write(strchr)
                        else:
                            tempWrite.write(char)
            self.transfer(string,case="txt")



