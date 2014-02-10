import skills1


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


def test_long_words():
    c = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were"]
    out = skills1.long_words(c)
    assert out == ["qowieur","qiwer","were"]

def test_smallest():

    c = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE",.93939]
    out = skills1.smallest(c)
    assert out == -999
    out = skills1.smallest(cc)
    assert out == None
    a = range(5)
    out = skills1.smallest(a)
    assert out == 0

def test_largest():
    c =  ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE",.99]
    d = range(9)
    out = skills1.largest(c)
    assert out == 9
    out = skills1.largest(cc)
    assert out == None
    out = skills1.largest(d)
    assert out == 8

def test_halvesies():
    c =  ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE",.99]
    d = range(9)
    out = skills1.halvesies(d)
    assert out == [0/2.0,1/2.0,2/2.0,3/2.0,4/2.0,5/2.0,6/2.0,7/2.0,8/2.0]
    out = skills1.halvesies(c)
    assert out == [4/2.0,5/2.0,6/2.0,7/2.0,8/2.0,9/2.0,-999/2.0]


def test_word_lengths():
    c =  ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE",.99]
    out = skills1.word_lengths(c)
    assert out == [1,1,1,1,7,5,3,4]
    out = skills1.word_lengths(cc)
    assert out == [1,4]
    d = range(9)
    out = skills1.word_lengths(d)
    assert out == []

def test_sum_numbers():
    c =  ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE", 0.99]
    out = skills1.sum_numbers(c)
    assert out == 4+5+6+7+8+9-999
    out = skills1.sum_numbers(cc)
    assert out == 0.99

def test_mult_numbers():
    c =  ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE", 0.99]
    out = skills1.mult_numbers(c)
    assert out ==  4*5*6*7*8*9*-999
    out = skills1.mult_numbers(cc)
    assert out == 0.99

def test_join_strings():  
    c = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer',"wer","were",-999]
    cc = [ "1","WERE", 0.99]
    out = skills1.join_strings(c)
    assert out == '1223qowieurqiwerwerwere'
    out = skills1.join_strings(cc)
    assert out == '1WERE'




def averages():

    c = range(9)
    out = skills1.average(c)
    assert out == 4.5
    cc = [1.0,2.0]
    out = skills.average(cc)
    assert out == 1.5
    ccc = ['were','owieure','woeirue']
    out = skills1.average(ccc)
    assert out == None









    




    
