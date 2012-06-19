import animals

def test_read_animals():
    filename = 'animals.txt'
    date,time,animal,number=animals.ranimals(filename)
    ref_time=['21:06','14:12','10:24','20:08','18:46']
    ref_number=[36,25,26,31,20]
    assert time == ref_time, "Times don't match!"
    if time != ref_time:
        print 'Times do not match!'
    else:
        print 'Times ok!'
    if number != ref_number:
        print 'Numbers do not match!'
    else:
        print 'Animal numbers ok!'

#This line calls the function that we defined.
test_read_animals()

from numpy import testing

def test_mean():
    assert animals.mean([5]) == 5
    assert animals.mean([3,5]) == 4
    assert animals.mean([1,2,3,4]) == 2.5
    testing.assert_almost_equal(animals.mean([1,2,3,4]),2.5)

test_mean()

def test_read_and_mean():
    filename = 'animals.txt'
    mean=animals.amean(filename)
    ref_mean = 27.6
    assert mean == ref_mean, 'Mean does not match!'

test_read_and_mean()


