#python program to sum the scores of each participant and create a new column in each list for the same.
def scores(filename):
    with open(filename,'r+') as fobj:
        x = fobj.readlines()
        print('readlines x: ',x)

        

        for i in x:
            s = 0
            spl = i.split()
            print("splitting each list element: ", spl)
            for j in spl[2:]:
                print("jth element: ", j)
                s += int(j)
            print("sum: ", s)








scores('judge.txt')



