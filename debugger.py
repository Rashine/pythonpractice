def divide(a,b):
    try:
        return a/b
    except TypeError:
        print ("Please provide two integers or floats")
    except ZeroDivisionError:
        print ("Please do not divide by zero")
        