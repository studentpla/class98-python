def countW():
    filename = input("enter the file name")
    numberofW = 0
    file = open("test.txt",'r')
    for line in file : 
        words = line.split()
        numberofW = numberofW+len(words)

    print("number of words are:")
    print (numberofW)

    numberofl =  0 
    file = open("test.txt", 'r')
    for sen in file: 
        line = sen.split(".")
        numberofl = numberofl+len(line)

    print("Number of lines = ")
    print(numberofl)
    
countW()