def test_equal(a,b):
    assert a==b, "{0} and {1} aren't equal".format(a,b)
    
def test_not_equal(a,b):
    assert a!=b, "Did not expect {0} but got {1}".format(a,b)

def test_is_in(collection,item):
    assert item in collection, "{0} does not contain {1}".format(collection,item)

def test_not_in(collection,item):
    assert item not in collection, "{0} does contain {1}".format(collection,item)

def test_between(value,low, high):
    assert value in range(low,high+1),"{0} is not between {1} and {2}".format(value, low, high)


# Test to fail the test_not_equal function
test_equal(1,2)

# Test to fail the test_not_equal function
test_not_equal(2,2)

# Test to fail the test_is_in function
test_is_in([1,2,3],5)

# Test to fail the test_not_in function
test_not_in([1,2,3,5],5)

# Test to fail the test_between function
test_between(7,3,6)