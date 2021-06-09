# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
  
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
  
# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]
  

r = [[114, 160, 60, 27],
[74, 97, 73, 14],
[119, 157, 112, 23]];

rez = [[r[j][i] for j in range(len(r))] for i in range(len(r[0]))]
print("\n")
print("The following result is (AB)^T")
print("\n")
for row in rez:
    print(row)



B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

rez = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
print("\n")


rez = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]



X = [[5, 6, 4],
[8, 7, 5],
[1, 3, 9],
[2, 0, 1]]

Y = [[12, 4, 7],
[7, 5, 8],
[3, 6, 9]]

print("The following result shows B^T*B^T")
print("\n")


result = [[sum(x * y for x, y in zip(X_row, Y_col)) 
                        for Y_col in zip(*Y)]
                                for X_row in X]
  
for r in result:
    print(r)
print("\n")
print("Hence proven")