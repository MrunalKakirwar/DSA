def checkIfUnique(inputString):
    hashArr = [False]*10
    flag = True

    for i in range (len(inputString)):
        hashCode = ord(inputString[i]) % 10
        print(hashCode)
        if(hashArr[hashCode] == True):
            hashArr[hashCode] = False
            flag = False
            return flag
        else:
            hashArr[hashCode] = True
            flag = True
    return flag



def main():
    inputString = input()
    # print(checkIfUnique(inputString))
    print(checkIfUnique(inputString))

if __name__ == "__main__":
    main()