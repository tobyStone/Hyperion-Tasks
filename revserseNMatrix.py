
def identity_matrix(size):
#  print()
#  print("Identity matrix") 
    for row in range(0, size):
        for col in range(0, size):
                       
          # Here end is used to stay in same line
            if (((size-1)-row) == col):
              print("1 ", end=" ")
          #    print()  
            else:
              print("0 ", end=" ")
        print()
        
identity_matrix(10)    