#module to generate password:
import random
def getpass():
    s = ''
    for i in range(8):
        x = random.randint(33,90)
        s += chr(x)
    return(s)

getpass()


    