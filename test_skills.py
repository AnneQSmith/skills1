import skills1

def test_smallest():
    a = range(5)
    out = skills1.smallest(a)
    print out
    assert out == 0

def test_all_odd():
    a = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer']
    out = skills1.all_odd(a)
    assert out == ['1','3',5,7,9] 

def test_all_even():
    a = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer']
    out = skills1.all_even(a)
    assert out == ['2','2',4,6,8] 
    a = range(5)
    out = skills1.all_even(a)
    assert out == [0,2,4]
    


    
