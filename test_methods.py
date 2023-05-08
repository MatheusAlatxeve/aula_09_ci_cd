import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sub():
    #given two numbers 
    number1 = 5
    number2 = 2
 
    #when we subtract the two numbers
    output = methods.sub_of_values(number1, number2)

    #then the subtraction must be
    assert output == 3

def test_sum():
    #given two numbers 
    number1 = 8
    number2 = 2
 
    #when we add the two numbers
    output = methods.sum_of_values(number1, number2)

    #then the sum must be
    assert output == 10

def test_div():
    #given two numbers 
    number1 = 4
    number2 = 2
 
    #when we divide the two numbers
    output = methods.div_of_values(number1, number2)

    #then the division must be
    assert output == 2

def test_mult():
    #given two numbers 
    number1 = 5
    number2 = 3
 
    #when we multiply the two numbers
    output = methods.mult_of_values(number1, number2)

    #then the multiplication must be
    assert output == 15
