"""Mega Palindrome
Let's say a positive integer is a megapalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive numbers L and R , return the number of megapalindromes in the inclusive range [L, R].

 

Example 1:

Input: L = 4, R = 1000

Output: 4

Explanation: 4, 9, 121, and 484 are megapalindromes.

Note that 676 is not a megapalindrome: 26 * 26 = 676, but 26 is not a palindrome. 

Note:

1 <= len(L) <= 18

1 <= len(R) <= 18

L and R are strings representing integers in the range [1, 10^18).

int(L) <= int(R)

Input Format:-

L

R

Output format:-

Number of mega palindromes """


import math
L = str(input())
R = str(input())
if 1<=len(L)<=18 and 1<=len(R)<=18 and int(L)<=int(R) and 1<=int(L)<=10**18 and 1<=int(R)<=10**18:
    L=int(L)
    R=int(R)
    l=[]
    count = 0
    for i in range(L,R+1):
        i = str(i)
        if i == i[::-1]:
            i = int(i)
            j = (math.sqrt(i))
            if j - math.floor(j)==0:
                j = "{:.0f}".format(j)
                j = str(j)
                if j == j[::-1]:
                    #print(j)
                    count+=1
print(count)
