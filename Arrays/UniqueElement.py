def getUnique(inputArr):
    uniqueElement = False
    for i in range(len(inputArr)):
        for j in range(i+1, len(inputArr)):
            if(inputArr[i] == inputArr[j]):
                i +=1
                break
            inputArr[i]

def main():
    inputArr = input()
    print(getUnique(inputArr))

if __name__ == "__main__":
    main()