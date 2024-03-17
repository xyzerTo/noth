import string
import secrets
import random

class Gen:
      
     def id_generator(self,rule=False):
            N = random.randint(4,15)
            x = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(N))
            return x
     
     def alg(self,rule):
            ordchr = 0
            for i in rule:
                  ordchr+=ord(i)
            return round(ordchr//len(str(ordchr/3))/10)
