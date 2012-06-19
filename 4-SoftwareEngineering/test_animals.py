import animals

def test_read_animals():
    filename = 'animals.txt'
    date,time,animal,number=animals.ranimals(filename)
    ref_time=['21:06','14:12','10:24','20:08','18:46']
    ref_number=[36,25,26,31,20]
    if time != ref_time:
        print 'Times do not match!1'
    if number != ref_number:
        print 'Numbers do not match!1'


def test_mean(filename):
    d,t,a,number=animals.ranimals(filename)
    
