def containsDuplicate(nums):
        
        nums_d = {}
        for n in nums:
            if n in nums_d:
                return True
            else:
                nums_d[n] = 1
        return False

def main():
        inputArr = input().split(' ')
        print(containsDuplicate(inputArr))
    
if __name__ == "__main__":
        main()