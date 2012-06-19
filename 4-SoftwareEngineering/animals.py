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
#If you just do data=ranimals(filename) then it returns a tuple of those 4 variables.


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
    """
    Returns the mean value of the given input list.
    """
    meann=sum(n)/float(len(n))
    return meann

def getanimal(date, time, animal, number, animal_name):
    """
    Counts the mean number of a given animal.
    data input is (date,time,animal,number)
    """
    tot=0.
    obs=0.
    for i in range(0,len(date)):
    #for d,t,a,n in zip(date,time,animal,number):    
        if animal[i] == animal_name:
            tot=tot+number[i]
            obs=obs+1
    meann=tot/obs
    return meann


def mooat(filename,antype):
    """
    Gives the mean number of a given animal atype from the file input.
    """
    import animals
    d,t,a,n=animals.ranimals(filename)
    meann=animals.getanimal(d,t,a,n,antype)
    return meann
