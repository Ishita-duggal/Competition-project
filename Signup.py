from password import getpass

#Defining class:
class details:

    des = ""
    prog = ''
    sem = 0
    phone = ""
    email = ''
    sap = ''
    pswd = ''


    def __init__(self,name):
        self.name = name


    def writedets(self, fobj):
        fobj.write(self.des+' '+self.name+' '+self.prog+' '+str(self.sem)+' '+self.phone+' '+self.email+' '+self.sap+' '+self.pswd+ "\n" )

def sign_up(filename):
    with open(filename,'a') as fobj:
#taking input of student particulars:
        n = input("Enter name: ")
        obj = details(n)
        print("What is your program? \n1.Bachelors \n2.Masters \n3.PHD")
        ch0 = int(input("Enter choice: "))
        while True:
            if ch0 == 1:
                obj.prog = "Bachelors"
                break
            elif ch0 == 2:
                obj.prog = "Masters"
                break
            elif ch0 == 3:
                obj.prog = "PHD"
                break
            else:
                print("Incorrect input, please re-enter!")
        while True:
            obj.sem = int(input("Enter semester of study (Enter 8 if not from university): "))
            if (obj.sem<1 or obj.sem>8):
                print("Invalid value, please re-enter.")
            else:
                break
        while True:
            obj.phone = str(input("Enter phone number: "))
            if(len(obj.phone) <10 or len(obj.phone)>10):
                print("Invalid value, please re-renter.")
            else:
                break
        obj.email = str(input("Enter email id before @: "))
        obj.sap = str(input("Enter SAP ID (Enter 0000 if not from university): "))
        print("What is your designation? \n1.Student \n2.Faculty \n3.Competitor \n4.Judge")
        ch = int(input("Enter chosen field: "))
        while True:
            if ch == 1:
                obj.des = "Student"
                break
            elif ch == 2:
                objdes = "Faculty"
                break
            elif ch == 3:
                obj.des = "Competitor"
                break
            elif ch == 4:
                obj.des = "Judge"
                obj.prog = "--"
                obj.sap = "--"
                obj.sem = "--"
                break
            else:
                print("Incorrect value, please re-enter!")
#Generating username and password:
        print("Your username is: ", obj.email)
        obj.pswd = getpass()
        print("Your password is: ", obj.pswd)
        obj.writedets(fobj)
        #fobj.write(obj.des+' '+obj.name+' '+obj.prog+' '+str(obj.sem)+' '+obj.phone+' '+obj.email+' '+obj.sap+' '+obj.pswd+ "\n" )

        print("Information stored.")
        


        
