# sample code for what will go on for the judges' part of the program:
'''
1. sign-up
2. Login:
after login:
    1. Enter scores
    2. Display scores
    3. Update scores''' 

def score():
    with open("judge.txt", 'a') as fobj:
        jname = input("Enter name of judge: ")
        cname = input("Enter contestant name: ")

        while True:
            c1 = int(input("Enter scores for criteria 1: "))
            if c1>= 0 and c1<=10:
                break
            else:
                print("Value entered must be between 0 and 10. ")
        while True:
            c2 = int(input("Enter scores for criteria 2: "))
            if c2>=0 and c2<=10:
                break
            else:
                print("Value entered must be between 0 and 10. ")
        while True:
            c3 = int(input("Enter scores for criteria 3: "))
            if c3>=0 and c3<=10:
                break
            else:
                print("Value entered must be between 0 and 10. ")
            
        x = (jname+' '+cname+' '+' '+str(c1)+' '+str(c2)+' '+str(c3)+'\n')
        fobj.write(x)
        print("Score stored. ")

score()
    

def display():
    with open('judge.txt','r') as fobj:
        x = fobj.read()
        print(x)

display()



    


        
            

   
    




