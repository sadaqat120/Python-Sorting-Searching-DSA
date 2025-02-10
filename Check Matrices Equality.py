def matrices_equality(matrix1, matrix2):
    if len(matrix1)==len(matrix2):
        for k in range(len(matrix1)):
            if len(matrix1[k])!=len(matrix2[k]):
                return False
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j]!=matrix2[i][j]:
                    print(matrix1[i][j])
                    print(matrix2[i][j])
                    return False
        return True
    return False

M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrices_equality(M1, M2))
