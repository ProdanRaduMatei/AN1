def FilterMul(score_list, value): # this function gets the scores multiples of a value
    new_score_list = []
    for i in score_list: # goes through the list
        if i % value == 0: # checks if the score is multiple of the value
            new_score_list.append(i) # puts the score in a new list
    return new_score_list # returns the list

def TestFilterMul():
    score_list = [2]
    FilterMul(score_list, 2)
    assert score_list == [2]
    
    try:
        FilterMul(score_list, 2)
        assert True
    except ValueError:
        assert False
    
    try:
        FilterMul(score_list, 3)
        assert False
    except ValueError:
        assert True
    
    try:
        FilterMul(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestFilterMul()