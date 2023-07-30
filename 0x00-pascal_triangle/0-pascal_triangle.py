def printPascal(n:int):
  
 
    arr = [[0 for x in range(n)] 
              for y in range(n)] 
  
 
    for line in range (0, n):
  
        # Every line has number of 
        # integers equal to line number
        for i in range (0, line + 1):
  
            # First and last values 
            # in every row are 1
            if(i is 0 or i is line):
                arr[line][i] = 1
                print(arr[line][i], end = " ") 
  
            # Other values are sum of values
            # just above and left of above 
            else:
                arr[line][i] = (arr[line - 1][i - 1] + 
                                arr[line - 1][i])
                print(arr[line][i], end = " ")             
        print("\n", end = "")
  
# Driver Code
n = 5
printPascal(n)
