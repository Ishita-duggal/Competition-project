def log_in(filename):
    # Code to verify username and password:
    with open(filename, 'r') as fobj:
        x = fobj.readlines()
        
    while True:
        usnm = input("Enter username: ")
        fl1 = 0
        for i in x:
            xspl = i.split()
            if xspl[5] == usnm:
                fl1 = 1
                break
            else:
                pass

        if fl1 == 1:
            print("Username matched! ")
            break
        else:
            print("Username does not exist, please re-enter.")

    while True:
        pswd = input("Enter password: ")
        fl2 = 0
        for j in x:
            jspl = j.split()
            if jspl[-1] == pswd:
                fl2 = 1
                break
            else:
                pass

        if fl2 == 1:
            print("Password matched! ")
            break
        else:
            print("Incorrect password, please re-enter.")
        
# Code to generate pass
    from prettytable import PrettyTable
    tbl = PrettyTable() #creates an empty table.

    #adding field names:
    tbl.field_names = ['DESIGNATION','NAME','PROGRAM','SEMESTER','PHONE NO.','SAP ID']

    with open(filename,'r') as fobj:
        x = fobj.readlines()

    l_main = []    
    for i in x:
        ispl = i.split()
        l_main.append(ispl)

    #identify row:
    for k in l_main:
        if k[5]==usnm:
            row = k
            break
        else:
            pass

    new_row = row[:5]
    new_row.append(row[6])
    
    tbl.add_row(new_row)
    
    print('\n\n',tbl,'\n\n')
    print("PASS GENERATED!\n")



        

           




            

