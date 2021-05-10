def matrixForm(matrix):
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

def sumMatrix(A, B):
    matrixSum = []
    for i in range(m):
        row = []
        for j in range(n):
            k = A[i][j] + B[i][j]
            row.append(k)
        matrixSum.append(row)

    return matrixSum


if __name__ == "__main__":
    form = input("\nEnter the value of m & n in format -- mxn : ")
    m = int(form.split("x")[0])
    n = int(form.split("x")[1])

    
    matrixA = []
    matrixB = []

    print("")
    print("Matrix A")
    a = matrixForm(matrixA)

    print("")
    print("Matrix B")
    b = matrixForm(matrixB)

    s = sumMatrix(a, b)

    print(f"The sum of {a} and {b} Matrices is {s}")