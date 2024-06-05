def update():
    with open('judge.txt','r+') as fobj:
        x = fobj.readlines()
        print('main list: ',x)
        for i in x:
            xspl = i.split()
            print('sub list: ',xspl)
            

update()
