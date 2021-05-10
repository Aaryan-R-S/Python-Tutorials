def matrixForm(matrix):
    form = input("\nEnter the value of m & n in format -- mxn : ")
    m = int(form.split("x")[0])
    n = int(form.split("x")[1])
    
    matrix = []
    for i in range(m):
        print(f" Enter the elements of Row No.{i+1} separted by spaces : ")
        row = input().split(" ")
        while len(row) != n:
            print(f"Please Enter only {n} entries as specified...")
            row = input().split(" ")
        row = list(map(int, row))
        matrix.append(row)

    return matrix

def mulMatrix(A, B):     # Understand with example A is ixk and B is kxj
    matrixMul = []
    for i in range(len(A)):                                #1  len(A) == i from ixk
        row = []

        for j in range(len(B[i])):                         #2   len(B[i]) == j from kxj
            sumElem = 0

            for k in range(len(A[i])):  # or len(B)        #3  len(A[i]) or len(B) == k from ixk & kxj
                sumElem += A[i][k] * B[k][j]

            row.append(sumElem)

        matrixMul.append(row)

    return matrixMul


if __name__ == "__main__":
    
    matrixA = []
    matrixB = []

    print("")
    print("Matrix A")
    a = matrixForm(matrixA)

    print("")
    print("Matrix B")
    b = matrixForm(matrixB)

    s = mulMatrix(a, b)

    print(f"The multiplication of {a} and {b} Matrices is {s}")