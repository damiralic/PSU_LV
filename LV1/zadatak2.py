ocjena = input("Unesi ocjenu izmedju 0.0 i 1.0: ")

if float(ocjena)<1.0 and float(ocjena)>=0.0:
    try:
        if float(ocjena)>=0.9:
            print("A")
        elif float(ocjena)>=0.8:
            print("B")
        elif float(ocjena)>=0.7:
            print("C")
        elif float(ocjena)>=0.6:
            print("D")
        elif float(ocjena)<0.6:
            print("F")
    except:
        print("Broj nije bio izmedju zadanih intervala")
        exit()
