def update():
    with open("judge.txt",'r+') as fobj:
        x = fobj.readlines()
        print('x: ',x)

    l = []
    for i in x:
        spl = i.split()
        #print("i.spl: ", spl)
        l.append(spl)

    #print("list: ", l)

    while True:
        #input value: if j == value, then, pick out i's value? 
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

    #print ("New list: ", l)

    fin = ''
    for i in l:
        for j in i:
            fin += (j + ' ')
        fin =  fin[:-1] + '\n'
    fin = fin[:-1]
    #print(fin)
    

    with open("judge.txt", 'w') as fobj:
        fobj.write(fin)
        print("Data updated. ")












                







            



    



        
        


        


update()
