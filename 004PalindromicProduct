maxPalindrome = 0
def checkPalindrome(num):

    string = str(num)
    if len(string) % 2 == 0:
        firstHalf = string[0:int(len(string)/2)]
        secondHalf = string[int(len(string)/2):][::-1]
    else:
        firstHalf = string[0:int(len(string)//2)]
        secondHalf = string[int(len(string)//2)+1:][::-1]
    if firstHalf == secondHalf:
        return num
    else:
        return 0

for i in range(100,1000):
    for j in range(100,1000):
        num = checkPalindrome(i*j)
        if num > maxPalindrome:
            maxPalindrome = num
print(maxPalindrome)

