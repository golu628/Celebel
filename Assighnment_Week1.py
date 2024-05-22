def lower_triangle(n):
    '''
    Function to print lower triangle
    *  
    * *  
    * * *  
    * * * *
    '''
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()

lower_triangle(5)

print("\n\n")

def upper_triangle(n):
    '''
    function to print upper traingle
    * * * *  
      * * *  
        * *  
          *
    '''
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n - i):
            print("* ", end="")
        print()

upper_triangle(5)

print("\n\n")

def pyramid(n):
    '''
    Function to print pyramid
     *  
    * *  
   * * *  
    * *  
     *
    '''
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "* " * (i + 1))

pyramid(5)
