from lww_implementation import LWW_implementation as LWW

def test_add():
    '''
    Purpose: This function tests if an element has been added successfully to the LWW
    '''
    
    lww = LWW()
    lww.add(1)
    lww.add("test variable")
    
    assert lww.exist(1)
    assert lww.exist("test variable")
    assert not lww.exist("dummy")
    
def test_remove():
    '''
    Purpose: This function tests if an element has been removed successfully from the LWW
    '''
    
    lww = LWW()
    lww.remove(1)
    
    assert not lww.exist(1)
    
    lww.add(1)
    assert lww.exist(1)
    
def test_merge():
    '''
    Purpose: This function tests functionality of merge method
    '''
    
    lww_1 = LWW()
    lww_2 = LWW()
    
    lww_1.add(1)
    lww_1.add(2)
    lww_1.remove(1)
    
    lww_2.add(1)
    lwW_2.add(5)
    
    lww_1.remove(5)
    lww_2.remove(1)
    
    lww = lww_1.merge(lww_2)
    assert lww.add_set[1] == lww2.add_set[1]
    assert lww.add_set[1] > lww1.add_set[1]
    assert lww.add_set[3] < lww1.remove_set[3]
    assert lww.remove_set[1] == lww2.remove_set[1]
    
def test_validate_timestamp():
    '''
    Purpose: This function validates timestamps of the elements
    '''
    
    lww = LWW()

    lww.add(1)
    lww.add(2)
    lww.add(3)
    lww.remove(4)
    lww.remove(2)

    assert lww.remove_set[2] > lww.add_set[2]
    assert lww.add_set[3] > lww.add_set[2]
    assert lww.remove_set[4] > lww.add_set[3]
    assert lww.remove_set[2] > lww.remove_set[4]
    
def test_repeated_add():
    '''
    Purpose: This function checks repeated addition of same element
    '''
    
    lww = LWW()
    
    lww.add(1)
    lww.remove(1)
    lww.add(1)
    lww.remove(1)
    
    assert not lww.exist(1)
    
def test_repeated_remove():
    '''
    Purpose: This function checks repeated removal of same element
    '''

    lww = LWW()

    lww.remove(1)
    lww.add(1)
    lww.remove(1)

    assert not lww.exist(1)
    
def test_remove_add():
    '''
    Purpose: This function checks remove operation followed by addition operation
    '''

    lww = LWW()

    lww.remove(1)
    lww.add(1)

    assert lww.exist(1)
    
