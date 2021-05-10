def facTrailZeros(num):
    count = 0
    # 100! = 100//5 + 100//5*5 + ...so on    using fact learnt from Cengage Mathematics!

    i = 1
    while (num//(5**i)) != 0:
        count += num//(5**i)
        i+=1
    
    return count


if __name__ == "__main__":
    print("")
    num = int(input("Enter the number :\n "))
    print(" ")
    print(facTrailZeros(num))
    print("")