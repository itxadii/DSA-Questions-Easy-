# 4️⃣ Check if a String is a Palindrome

# A string is a palindrome if it reads the same forward and backward.

def ifPalindrome(s):
    if s == s[::-1]:
        return True 
    return False    

print(ifPalindrome("madam"))
