A = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1]
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
def max_subarry(A):
  max_sum =float('-inf')
  first_row=0
  last_row =0
  first_col=0
  last_col=0
  rows =le(A)
  cols =len(A[0])

  for i in range(rows):
    for j in range(cols):
      for k in range(i,rows):
         for l in range(j,cols):
             current_sum =0
             for s in range(i, k+1):
                for o in range(j,l+1):
                    current_sum += A[s][o]

             if current_sum > max_sum :
                max_sum = current_sum
                first_row, last_row, first_col, last_col = i, k , j , l

  return max_sum, first_row, last_row, first_col, last_col 
  result = max_subarry(A)
  print("sum:", results[0])
  print("indeces({},{},{},{})".format(result[1], result[2], result[3],result[4]))
------------------------------------------------------------------------------
#1.1.2 Constrained Formulation :
A = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1]
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
def max_subarry(A, K, L):
  max_sum =float('-inf')
  first_row=0
  last_row =0
  first_col=0
  last_col=0
  rows =le(A)
  cols =len(A[0]) 
  for i in range(rows):
    for j in range(cols):
      for k in range(i,rows):
         for l in range(j,cols):
             current_sum =0
               if (K - i +1) * (L - j +1) == K *L :
                     for s in range(i, k+1):
                         for o in range(j,l+1):
                             current_sum += A[s][o] 

                     if current_sum > max_sum :
                        max_sum = current_sum
                        first_row, last_row, first_col, last_col = i, k , j , l
 
  return max_sum, first_row, last_row, first_col, last_col 
K = 2
L= 3      
result = max_subarry(A, K, L)
print("sum:", results[0])
print("indeces({},{},{},{})".format(result[1], result[2], result[3],result[4]))
                    
