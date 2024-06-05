import random
from Signup import sign_up
from Login import log_in

# code to create a list of time slots to assign time to contestants
l1 =[]
for i in range(0,300,25):
    l1.append(i)


l2 = []
for i in range(25,301,25):
    l2.append(i)


l_main=[]
 
c = 0
for i in l1:
    c += 1



for i in range(c):
    lis = [l1[i], l2[i]]
    l_main.append(lis)


var = 0

while var == 0:
    ext = 0

    
    print("Choose one of the following options: \n1.Generate Pass (students, faculty, competitor) \n2.Competition \n3.Judging \n4.Exit ")
    ch = int(input("Enter choice: "))
    
    if (ch==1):
        while ext == 0:
            print("Choose one of the following: \n1. Sign up \n2. Login \n3. Exit to Main Menu") 
            ch1 = int(input("Enter chosen field: "))
            fname = 'basedb.txt'
            if (ch1 == 1):
                sign_up(fname)
                
            elif (ch1 == 2):
                log_in(fname)

            elif (ch1 == 3):
                ext = 1

            else:
                print("Incorrect input, kindly re-enter. ")

    elif(ch==2):
        while ext == 0:
            print(" Choose one of the following options: \n1.sign-in(new contestant/entry) \n2.log-in to obtain contestant pass and See set list and event timings \n3. MAIN MENU") 
            ch2 = int(input("Enter your choice: "))
            fname = 'contest.txt'
            if(ch2 == 1):
                sign_up(fname)
                
            elif(ch2==2):
                log_in(fname)
                ctr = 0
                for i in l_main:
                    ctr += 1
                
                r = random.randint(0,ctr) 
                el = l_main.pop(r)
                print('Allocated time slot is: ', el)

                for i in el:
                    hr = i//60
                    min = i%60
                    print("time: ",hr,":",min)
                    
                    
            elif(ch2==3):
                ext = 1
            else:
                print("Invalid input, please re-renter")

            

    elif (ch == 3):
        while ext == 0:
            print("1. Sign-up \n2. Login to see event details \n3. exit to Main Menu " )
            ch3 = int(input("Enter choice: "))
            fname = "judgedb.txt"
            comp = "competition.txt"
            if (ch3 == 1):
                sign_up(fname)

            elif(ch3 == 2):
                log_in(fname)
                while True:
                    print("Choose a task: \n1.Enter scores \n2.Update score \n3.Display scores \n4.Exit to previous menu")
                
                    ch3_ = int(input("Enter choice: "))
                    if (ch3_==1):
                        with open(comp, 'a') as fobj:
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
                    #score function ends
                    
                    elif(ch3_ == 2):
                        with open(comp,'r+') as fobj:
                            x = fobj.readlines()

                        l = []
                        for i in x:
                            spl = i.split()
                            l.append(spl)

                        while True:
                            nme = str(input("Enter name of contestant to update score: "))

                            f = 0    
                            for i in range(len(l)):
                                
                                if l[i][1] == nme:
                                    print('Chosen line: ',l[i])
                                    f = 1
                                    break
                                else:

                                    pass

                            if f == 1:
                                while True:
                                    crt = int(input("Enter criteria to update: "))


                                    if crt <1 or crt> 3:
                                        print("Invalid value, kindly re-enter. ")

                                    else:
                                        l[i][crt + 1] = input("Enter new value: ")
                                        break
                                break
                                        


                            
                            else:
                                print("The value provided doesn't exist in the database, kindly re-enter.")

                        fin = ''
                        for i in l:
                            for j in i:
                                fin += (j + ' ')
                            fin =  fin[:-1] + '\n'
                        

                        with open(comp, 'w') as fobj:
                            fobj.write(fin)
                            print("Data updated. ")
                #update function ends
                            
                    elif (ch3_ == 3):
                        with open(comp,'r') as fobj:
                            x = fobj.read()
                            print(x)
                #Display function ends
                    
                    elif(ch3_ == 4):
                        break
                #exits to previous menu
                
                    else:
                        print("invalid input, kindly re-enter")
                #displays error message and keeps the code repeating
            
            
            elif(ch3 == 3):
                ext = 1
            
            else:
                print("invalid value entered, kindly re-enter. ")
                

    elif(ch==4):
        print("Program exited. ")
        var = 1
        

    else:
        print("Invalid input, please re-enter.")

        
        
        