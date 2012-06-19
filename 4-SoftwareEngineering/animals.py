def ranimals(filename):
    """
    Reads animal count file. 
    Must have 4 columns, no header row.
    Columns are: date, time, animal name, number seen.
    Syntax: d,t,a,n=ranimals('filename.txt')
    """
    #Open the file for reading
    f = open(filename, 'r')
    #Set up the arrays
    date=[]
    time=[]
    animal=[]
    number=[]
    #Iterate over the file one line at a time
    for line in f:
        d,t,a,n=line.split()
        date.append(d)
        time.append(t)
        animal.append(a)
        number.append(int(n))
    return date, time, animal, number

def amean(filename):
    """
    Reads the animal file, and 
    calculates the mean of the number of animals spotted.
    """
    import animals
    d,t,a,n=animals.ranimals(filename)
    meann=sum(n)/float(len(n))
    return meann

def mean(n):
    meann=sum(n)/float(len(n))
    return meann

