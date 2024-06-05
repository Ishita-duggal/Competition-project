#Edit to make for out of college people.

from password import getpass
#using sample file as student.txt
#required argument: filename...
def sign_up_oth(filename):
    with open(filename,'a') as fobj:
#taking input of student particulars: 
        name = str(input("Enter name: "))
        #parameters: name, phone, email, designation
        #program deleted
        #semester deleted
        while True:
            phone = str(input("Enter phone number: "))
            if(len(phone) <10 or len(phone)>10):
                print("Invalid value, please re-renter.")
            else:
                break
        email = str(input("Enter email id before @: "))
        print("What is your designation? \n1.Performer \n2.Judge \n3.Financier \n4.Food stall manager ")
        ch = int(input("Enter chosen field: "))
        while True:
            if ch == 1:
                des = "Performer"
                break
            elif ch == 2:
                des = "Judge"
                break
            else:
                print("Incorrect value, please re-enter!")

            '''other particulars for pass:'''
        prog = "--"
        sem = "--"
        sap = "--"

#Generating username and password:
        print("Your username is: ", email)
        pswd = getpass()
        print("Your password is: ", pswd)
        fobj.write(des+' '+name+' '+prog+' '+sem+' '+phone+' '+email+' '+sap+' '+pswd+ "\n" )
        print("Information stored.")






#sample call, delete in final project.
#sign_up_oth()