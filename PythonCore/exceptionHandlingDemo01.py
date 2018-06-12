import functionDemo01 as LOGGER

(a, b) = (5, 0)

try:  # simple use of try-except block for handling errors
    g = a/b
except ZeroDivisionError as exception:
    LOGGER.logError("This is a DIVIDED BY ZERO error !")
    print ("This is a DIVIDED BY ZERO error: ", exception)