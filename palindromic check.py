def isPalindrome(string):
    leftIDX = 0
    rightIDX = len(string)-1
    while leftIDX < rightIDX:
        if string[leftIDX] != string[rightIDX]:
            return False
        leftIDX += 1
        rightIDX -= 1
    return True

print(isPalindrome("abcdcba"))