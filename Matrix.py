import numpy as np


def arrayMaker(assumedfile):
    """ 
        This is all a skeleton for a txt file to turn data into an array :)
    """
    try:
        file = open(assumedfile, 'r')
        assumedtext = file.readlines()
        list = []
        index = 0

        for info in assumedtext:
            list.append([])
            ninfo = info.split()

            for item in ninfo:
                numinfo = int(item)
                list[index].append(numinfo)
            
            index += 1

        file.close()
        
        nparray = np.array(list)

        return nparray

    except:
        return "Error, either String or Dimensions"


if "__main__" == __name__:
    # A lot of these functions have form;
    # function(shape, dtype=float, order='C') 
    # with only the shape requiring definition

    # Creates array of [1 2 3]
    array1 = np.array([1, 2, 3])
    print(type(array1))
    print(array1)
    print(" ")

    # Creates 2 by 3 matrix
    array2 = np.array([[2, 3, 5], [1, 3, 2]])
    print(array2)
    print(" ")

    # Changes matrix to a 3 by 2
    array2.shape = (3, 2)
    print(array2)
    print("")

    # Creates Matrix 3 by 3 of zeros
    zero = np.zeros((3,3), int)
    print(zero)
    print(" ")

    # Creates a matrix 3 by 4 full of 9's sized 
    full = np.full((3,4), 9)
    print(full)
    print(" ")

    # this is one dimensional array 
    a = np.arange(24) 
    a.ndim  

    # Reshapes the array/matrix to 2 matrices of 4 by 3
    b = a.reshape(2,4,3) 
    print(b) 
    print()

    # Creates an empty array of 3 by 2, prints random numbers until asigned values
    emptyarray = np.empty([3, 2], int)
    print(emptyarray)
    print(" ")

    # Creates a matrix 2 by 3 of ones
    ones = np.ones([2, 3])
    print(ones)
    print("")

    # Creates an array of the data in the file
    print(arrayMaker("assumedfile.txt"))

