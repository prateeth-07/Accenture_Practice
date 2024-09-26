#  reverse the string
# n=input().split()
# n.reverse()
# print(*n)


# reverse the array
# a=list(input())
# e=[]
# o=[]
# a.reverse()
# for i in range(len(a)):
#     if i%2==0:
#         e.append(str(a[i]))
#     else:
#         o.append(str(a[i]))
# print("even:",",".join(e))
# print("odd:",",".join(o))


# ip: abc,adss,sdsdsd   op:6(longest sub string)
# s=input().split(",")
# m=0
# for i in s:
#     if len(i)>m:
#         m=len(i)
# print(m)



# find dividend and check whether its in array
# def dd(a,div,r,q):
#     for i in range(len(a)):
#         if d==a[i]:
#             return i
#     return -1
# a=list(map(int,input().split()))
# div=int(input())
# r=int(input())
# q=int(input())
# d=div*q+r
# print(dd(a,div,r,q))
    



# reverse array and get sum of even position elements
# a=list(map(int,input().split()))
# e=[]
# a.sort(reverse=True)
# for i in range(len(a)):
#     if (i+1)%2==0:     #1 index based
#         e.append((a[i]))
# print(sum(e))





# mid element except -ve number
# def m(a,n):
#     g=[]
#     for i in range(n):
#         if a[i]>0:
#             g.append(a[i])
#     if g:
#         mid=int((len(g)-1)/2)
#         return g[mid]
#     else:
#         return -1
# n=int(input())
# a=list(map(int,input().split()))
# print(m(a,n))




# examination=e9n
# s=input()
# c=0
# a=[]
# for i in s:
#     a.append(s[0])
#     break
# for i in range(1,len(s)-1):
#     c+=1
# a.append(str(c))
# p=s[::-1]
# for i in s:
#     a.append(p[0])
#     break
# print("".join(a))




# sum of even and odd elements in array
# a=list(map(int,input().split()))
# e=[]
# o=[]
# for i in range(len(a)):
#     if a[i]%2==0:
#         e.append(a[i])
#     else:
#         o.append(a[i])
# print(sum(e))
# print(sum(o))



# Floydes pattern
# n=int(input())
# start=1
# for i in range(n):
#     for j in range(n):
#         if j<=i:
#             print(start,end=" ")
#             start+=1
#         else:
#             print(" ",end=" ")
#     print()



# leap year
# year=int(input())
# if(year%400==0) or (year%4==0 and year%100!=0):
#     print("leap")
# else:
#     print("not leap")




# hallowen candies
# a=list(map(int,input().split()))
# m=int(input())
# c=0
# a.sort()
# for i in a:
#     if i%5==0:
#         c+=1
#     elif m>=i:
#         c+=1
#         m-=i
#     else:
#         break
# print(c)



# total sum od cases
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# t=0
# if a<0:
#     t+=a
# if b<0:
#     t+=b
# if c<0:
#     t+=c
# if d<0:
#     t+=d
# print(t)




# if '0' then replace '5'
# n=input()
# ans=[]
# for i in n:
#     if i =='0':
#         ans.append('5')
#     else:
#         ans.append(i)
# print(''.join(ans))


# reverse number
# n=int(input())
# s=str(n)
# q=s[::-1]
# print(q)



# index of target in array
# a=list(map(int,input().split()))
# t=int(input())
# for i in range(len(a)):
#     if a[i]==t:
#         print(i)


# MadaaM=madam or MADam=MADAM
# s=input()
# s_l=sum(c.islower() for c in s)
# s_u=sum(c.isupper() for c in s)
# if s_l>s_u:
#     print(s.lower())
# elif s_u>s_l:
#     print(s.upper())
# else:
#     print(s)




# product if num is odd else sum
# N = input().strip()
# if int(N) % 2 == 1:
#     product = 1
#     for i in N:
#         product *= int(i)
#     print(product)
# else:
#     total_sum = sum(int(digit) for digit in N)
#     print(total_sum)




# # prime
# n=int(input())
# s=0
# for i in range(2,n):
#     is_p=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             is_p=False
#             break
#     if is_p:
#         s+=i
# print(s)




# # googly prime
# def check(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# def is_p(num):
#     digits=sum(int(digit) for digit in str(num))
#     if check(digits):
#         return "yes"
#     else:
#         return "no"
# num=input()
# print(is_p(num))





# # encode
# s=input()
# d=''
# c=''
# for i in s:
#     if i=='1':
#         c+=i
#     else:
#         if c:
#             d+=chr(ord('A')+len(c)-1)
#             c=''
# if c:
#     d+=chr(ord('A')+len(c)-1)
# print(d)
    



# The number of occurrences of the second highest element in the array.
# def aa(a):
#     a.sort()
#     u=list(set(a))
#     u.reverse()
#     s=u[1]
#     o=a.count(s)
#     return o
# a=list(map(int,input().split()))
# print(aa(a))



# sum of -ve numbers
# def aa(a):
#     e=[]
#     for i in range(len(a)):
#         if a[i]<0:
#             e.append(a[i])
#     return sum(e)
# a=list(map(int,input().split()))   
# print(aa(a))



# inversion
# n=int(input())
# a=list(map(int,input().split()))
# c=0
# for i in range(n):
#     for j in range(i+1,n):
#         if i<j and a[i]>a[j]:
#             c+=1
# print(c)




# island life
# def min_boxes_to_buy(N, E, D):
#     total_sweets_needed = E * D
#     total_sundays = D // 7
#     buy_days = D - total_sundays
#     if E > N and buy_days == 0:
#         return -1
#     total_boxes_needed = (total_sweets_needed + N - 1) // N  
#     if total_boxes_needed <= buy_days:
#         return total_boxes_needed
#     else:
#         return -1
# N = int(input()) 
# E = int(input())   
# D = int(input())  
# output = min_boxes_to_buy(N, E, D)
# print(output)  




# superrior
# def Superior(arr, n):
#     count = 0
#     for i in range(n-1):
#         is_superior = True
#         for j in range(i+1, n):
#             if arr[i] <= arr[j]:
#                 is_superior = False
#                 break
#         if is_superior:
#             count += 1
#     return count + 1  
# arr=list(map(int,input().split()))
# n=len(arr)
# print(Superior(arr, n))





# if n is odd make n/2, if n is even make (n-2)/2, if n is single digit print as it is
# def oo(n):
#     while n>9:
#         if n%2==0:
#             return (n-2)//2
#         else:
#             return n//2
#     return n
# n=int(input())
# print(oo(n))




# input: hello world op: dlrow olleh
# s = input( )
# print(s[::-1])



# floyds triangle
# n=4
# 1
# 12
# 123
# 1234
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()  




# file  version
# s = list(map(str, input().split()))
# v = []
# if len(s) < 1:
#     print(-1)
# else:
#     for i in s:
#         if len(i) >= 5 and i[:5] == 'File_' and i[5:].isdigit():
#             v.append(int(i[5:]))
#     if v:
#         print(max(v))
#     else:
#         print(-1)



# sum of odd and even elements in array
# def su(n,a):
#     o=[]
#     e=[]
#     for i in range(n):
#         if a[i]%2!=0:
#             o.append(a[i])
#         else:
#             e.append(a[i])
#     sum_odd = sum(o)
#     sum_even = sum(e)
#     return sum_odd, sum_even
# n=int(input())
# a=list(map(int,input().split()))
# sum_odd,sum_even=su(n,a)
# print(sum_odd)
# print(sum_even)



# def ab(n,input1):
#     r=''
#     for i in range(n):
#         r+=input1
#     return r
# n=int(input())
# input1=input()
# print(ab(n,input1))
    




# def file(s):
#     v=[]
#     for i in s:
#         if len(i)>=6 and i[:5]=='File_' and i[5:].isdigit():
#             v.append(int(i[5:]))
#     if v:
#         return max(v)
#     else:
#         return -1
# s=input().split(",")
# print(file(s))



# rebound height
# def rebound_height(h,v,vn):
#     en=(v/vn)
#     h1=h*(v/vn)**2
#     return h1
# h=int(input())
# v=int(input())
# vn=int(input())
# print(rebound_height(h,v,vn))


# n=int(input())
# a=list(map(int,input().split()))
# o=[]
# e=[]
# for i in range(n):
#     if a[i]%2==0:
#         e.append(a[i])
#     else:
#         o.append(a[i])
# print(sum(e)) 
# print(sum(o))  





# s=input()
# ch1=input()
# ch2=input()
# ans=[]
# for i in s:
#     if i==ch1:
#         ans.append(ch2)
#     elif i==ch2:
#         ans.append(ch1)
#     else:
#         ans.append(i)
# print("".join(ans))




# a=list(map(int,input().split()))
# g=list(set(a))
# g.reverse()
# second=g[1]
# i=a.count(second)
# print(i)



# reverse the string
# s=input().split()
# s.reverse()
# print(" ".join(s))


# arr=[1,2,3,4,5,6,7]
# v=[2,4,6]

# arr=list(map(int,input().split()))
# v=[]
# w=[]
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         v.append(arr[i])
#     else:
#         w.append(arr[i])
# print (sum(v))
# print (sum(w))



# given array,reverse,even,odd
# arr=list(map(int,input().split()))
# arr.reverse()
# e=[]
# o=[]
# for i in range(len(arr)):
#     if i%2==0:
#         e.append(str(arr[i]))
#     else:
#         o.append(str(arr[i]))
# print (*e)
# print (*o):


# googly prime
# def check(num):
#     if n<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# def is_p(n):
#     digits=sum(int(i) for i in str(n))
#     if check(digits):
#         return "YES"
#     else:
#         return "NO"
# n=int(input())
# print(is_p(n))




# def trip(a,m,n):
#     c=0
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if a[i]*a[j]*a[k]==m:
#                     c+=1
#     return c
# n=int(input())
# a=list(map(int,input().split()))
# m=int(input())
# print(trip(a,m,n))



# def is_p(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True

# def check(n):
#     s=0
#     for i in range(2,n+1):
#         if is_p(i):
#             s+=i
#     return s

# n=int(input())
# print(check(n))




# special fibonaci
# n=int(input())
# f=[1,1]
# for i in range(2,n+1):
#     f.append(int((f[i-1]**2)+(f[i-2]**2))%(47))
# print(f[n])


# a=list(map(int,input().split()))
# s=0
# s1=0
# for i in range(len(a)):
#     if i%2==0:
#         s+=a[i]
#     else:
#         s1^=a[i]
# print(s+s1)


# string seperated by "." find largest word
# s=input().split(".")
# m=0
# l=''
# for i in s:
#     if len(i)>m:
#         l=i
#         m=len(i)
# print(l)



# ip: 1 2 3 4 5   op:oddevenoddevenodd
# def check(a):
#     ans=[]
#     for i in a:
#         if i%2==0:
#             ans.append("even")
#         else:
#             ans.append("odd")
#     return "".join(ans)
# a=list(map(int,input().split()))
# print(check(a))



# vowel permutation
# def count_consonant_permutations(s):
#     vowels = "aeiouAEIOU"
#     consonants = []
#     for ch in s:
#         if ch.isalpha() and ch not in vowels:
#             consonants.append(ch)
#     if len(consonants) == 0:
#         return 0
    
#     total_consonants = len(consonants)
#     unique_consonants = set(consonants)

#     denominator = 1
#     for consonant in unique_consonants:
#         count = consonants.count(consonant)
#         if count > 1:
#             for i in range(2, count + 1):
#                 denominator *= i

#     permutations = 1
#     for i in range(2, total_consonants + 1):
#         permutations *= i
#     permutations //= denominator
#     return permutations





# s=input().split(",")
# v=[]
# for i in s:
#     v.append(i[:1])
# print("".join(v))



# s=input().split(",")
# v=[]
# for i in s:
#     if len(i)>=6 and i[:5]=='File_' and i[5:].isdigit():
#         v.append(i[5:])
# if v:
#     print(max(v))
# else:
#     print(-1)



# n=int(input())
# a=list(map(int,input().split()))
# c=0
# for i in a:
#     if i<0:
#         c+=1
# print(c)



# def check(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def is_p(a,m):
#     v=[]
#     for i in range(m):
#         if check(a[i]):
#             v.append(str(a[i]))
#     if v:
#         v.reverse()
#         return " ".join(v)
#     else:
#         return -1 
# a=list(map(int,input().split()))
# m=len(a)
# print(is_p(a,m))


# s = list(input())  
# v = []  
# c = [] 
# b = []  
# a = []  

# for i in s:
#     if i.isdigit():
#         v.append(i)
#     elif i.isalpha() and i.isupper():
#         c.append(i)
#     elif i.isalpha() and i.islower():
#         b.append(i)
#     else:
#         a.append(i)
# print(*v)  
# print(*c) 
# print(*b)  




# maximize pair
# def maximize(a,n):
#     m=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i]+a[j]==d:
#                 if a[i]>a[j]:
#                     p=a[i]*a[j]
#                     if p>m:
#                         m=p
#                         r=[a[i],a[j]]
#                 else:
#                     p=a[j]*a[i]
#                     if p>m:
#                         m=p
#                         r=[a[j],a[i]]
#     return r
# a=list(map(int,input().split()))
# n=len(a)
# d=int(input())
# print(maximize(a,n))



# difference of whitespaces
# s1=input()
# s2=input()
# c=0
# c1=0
# for i in s1:
#     if i==' ':
#         c+=1
# for i in s2:
#     if i==' ':
#         c1+=1
# s=abs(c-c1)
# if s%2==0:
#     print(f"even: {s}")
# else:
#     print(f"odd: {s}")



# poet and ryhm
# def longest_common_suffix(word1, word2):
#     # Start from the end of both words and find the longest common suffix
#     i, j = len(word1) - 1, len(word2) - 1
#     count = 0
    
#     while i >= 0 and j >= 0 and word1[i] == word2[j]:
#         count += 1
#         i -= 1
#         j -= 1
        
#     return count

# def find_best_rhyme(arr, input_word):
#     best_word = ""
#     max_suffix_length = 0

#     for i in arr:
#         common_suffix_length = longest_common_suffix(i, input_word)
#         if common_suffix_length > max_suffix_length or (common_suffix_length == max_suffix_length and len(i) < len(best_word)):
#             best_word = i
#             max_suffix_length = common_suffix_length
#     return best_word
# arr = list(map(str,input().split()))
# input_word = input()
# result = find_best_rhyme(arr, input_word)
# print(result)  


# toss and score
# s=input()
# score=0
# cont=0
# for i in s:
#     if i=="H":
#         score+=2
#         cont+=1
#         if cont==3:
#             break
#     elif i=="T":
#         score-=1
#         cont=0
# print(score)



# encode num
# n=int(input())
# s=str(n)
# a=[]
# for i in s:
#     a.append(str(int(i)**2))
# print("".join(a))


# s=input()
# ss=set(s)
# a="qwertyuiopasdfghjklzxcvbnm"
# aa=set(a)
# print("".join(sorted(list(aa-ss))))

# def summ(a,s):
#     for i in range(len(a)):
#         if i%2==0:
#             s+=a[i]
#     return s
# a=list(map(int,input().split()))
# n=int(input())
# s=0
# print(summ(a,s))


# def check(n):
#     if n<1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def is_p(num):
#     s=0
#     for i in range(2,num+1):
#         if check(i):
#             s+=i
#     return s
# num=int(input())
# print(is_p(num))


# def countt(s,c):
#     return s.count(c)
# n=int(input())
# s=input()
# c=input()
# print(countt(s,c))



# s=input().split()
# v=[]
# for file in s:
#     parts=file.split("_")
#     if len(parts)==2 and parts[0]=="File" and parts[1].isdigit():
#         v.append(parts[1])
# if v:
#     print(max(v))
# else:
#     print(-1)



# def convert_to_binary(n):
#     binary = ""
#     while n > 0:
#         binary = str(n % 2) + binary
#         n = n // 2
#     return binary

# n = int(input("Enter a number: "))
# binary = convert_to_binary(n)
# print(f"The binary representation of {n} is {binary}")


# n=input()
# c=''
# d=''
# for i in n:
#     if i=='1':
#         c+=i
#     else:
#         if c:
#             d+=chr(ord("A")+len(c)-1)
#             c=''
# if c:
#     d+=chr(ord("A")+len(c)-1)
# print(d)



# def check(n):
#     if n<1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%2==0:
#             return False
#     return True
# def is_p(a,n):
#     s=0
#     for i in range(2,n+1):
#         if check(i):
#             s+=a[i]
#     return s
# a=list(map(int,input().split()))
# n=int(input())
# print(is_p(a,n))


# def count(word1,word2):
    
#     i,j=len(word1)-1,len(word2)-1
#     count=0
#     while i>0 and j>0 and i==j:
#         count+=1
#         i-=1
#         j-=1
#     return count
# def check(s,n):
#     best=""
#     m=0
#     for i in s:
#         common=count(i,n)
#         if common>m or(common==m and len(i)<len(best)):
#             best=i
#             m=common
#     return best
# s=list(map(str,input().split()))
# n=input()
# print(check(s,n))


# n = int(input())
# count_a = 0
# count_b = 0

# for i in range(n):
#     s = input()
#     count_a += s.count("Team A")
#     count_b += s.count("Team B")

# if count_a > count_b:
#     print("Team A")
# else:
#     print("Team B")



# def c(input1):
#     g=bin(input1)[2:]
#     return sum(int(digit) for digit in g)
# input1=int(input())
# print(c(input1))



# def sec_s(input1):
#     unique_sorted = sorted(set(input1))
#     return unique_sorted[-2],unique_sorted[1]
# input1=list(map(int,input().split()))
# print(sec_s(input1))

# def rotate_array_right(arr, k):
#     if not arr:
#         return arr
#     n = len(arr)
#     k = k % n  
#     return arr[-k:] + arr[:-k]

# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3

# rotated_arr = rotate_array_right(arr, k)
# print(f"Original array: {arr}")
# print(f"Array rotated right by {k} steps: {rotated_arr}")


# a=list(map(int,input().split()))
# p=[]
# n=[]
# r=[]
# for i in a:
#     if i>0:
#         p.append(i)
#     else:
#         n.append(i)
# for i in range(len(p)):
#     r.append(p[i])
#     r.append(n[i])
# print(r)

# count characters without space
# s=input()
# c=0
# for i in s:
#     if i!=" ":
#         c+=1
# print(c)/


# dice=int(input())
# num=list(map(int,input().split()))
# v=[]
# if dice%2==0:
#     for i in range(len(num)):
#         if i%2!=0:
#             v.append(num[i])
# else:
#     for i in range(len(num)):
#         if i%2==0:
#             v.append(num[i])
# print(sum(v))



# a=list(map(int,input().split()))
# ans=[]
# for i in a:
#     if i%3==0 and i%2==0:
#         ans.append(i)
# print(sum(ans)//len(ans))




# colourful stones
# s = input()  
# t = input()  
# position = 1
# for i in t:
#     if s[position - 1] == i: 
#         position += 1
# print(position)


# a=list(map(int,input().split()))
# a.sort(reverse=True)
# print(a[0])

# arr=list(map(int,input().split()))
# ans=[]
# for i in range(len(arr)):
#     if i%2==0:
#         ans.append(arr[i])
# print(ans)

# def countPairs(arr):
#     count = 0
    
#     # Iterate over all pairs in the array
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             # If the sum of the two elements is 60, increase the count
#             if (arr[i] + arr[j]) % 60 == 0:
#                 count += 1
                
#     return count

# # Example usage
# minutes = [2, 58, 58, 2, 60, 60]
# print(countPairs(minutes))  # Output should be 4



# def remove_vowels_between_consonants(s):
#     vowels = "aeiouAEIOU"
#     result = []

#     for i in range(len(s)):
#         if s[i] in vowels:
#             # Check if the current vowel is between two consonants
#             if i > 0 and i < len(s) - 1:  # Ensure it's not the first or last character
#                 if s[i-1] not in vowels and s[i+1] not in vowels:
#                     continue  # Skip the vowel if it's surrounded by consonants
#         result.append(s[i])  # Append the character to the result

#     return ''.join(result)

# # Example usage
# input_str = "applesarefallingfromtheskies"
# output_str = remove_vowels_between_consonants(input_str)
# print(output_str)



# def maximize(a,n):
#     m=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i]+a[j]==d:
#                 if a[i]>a[j]:
#                     p=a[i]*a[j]
#                     if p>m:
#                         m=p
#                         r=[a[i],a[j]]
#                 else:
#                     p=a[j]*a[i]
#                     if p>m:
#                         m=p
#                         r=[a[j],a[i]]
#     return r
# a=list(map(int,input().split()))
# n=len(a)
# d=int(input())
# print(maximize(a,n))



# s=input().split()
# c=0
# c1=0
# for i in s:
#     if i=='A':
#         c+=1
#     elif i=='B':
#         c1+=1
# if c>c1:
#     print("A")
# else:
#     print("B")




# n = float(input())  # takes a floating-point number as input
# f = int(n ) # converts the input to an integer (truncating the decimal part)
# g = bin(f)[2:] # converts the integer to binary and removes the '0b' prefix
# print(sum(int(digit) for digit in g)) # prints the sum of the binary digits


# def low(s):
#     ans=[]
#     for i in s:
#         if i.islower():
#             ans.append(i)
#     return "".join(ans),len(ans)
# s=input()
# lower_case_chars, count = low(s)
# print(lower_case_chars, count)


# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# n=int(input())
# ans=[]
# s=0
# for i in range(max(len(arr1),len(arr2))):
#     ans.append(arr2[i]-arr1[i])
# for i in range(n):
#     ans.sort(reverse=True)
#     s+=ans[i]
# print(s)




# def wordc(word1,word2):
#     count = 0
#     i,j=len(word1)-1,len(word2)-1
#     while i>=0 and j>=0 and word1[i]==word2[j]:
#         count+=1
#         i-=1
#         j-=1
#     return count
# def main(input1,input2):
#     best_word=''
#     maxi=0
#     for i in input1:
#         common_length=wordc(i,input2)
#         if common_length>maxi or (common_length==maxi and len(i)<len(best_word)):
#             maxi=common_length
#             best_word=i
#     return best_word
# input1=input().split()
# input2=input()
# print(main(input1,input2))



# def vowel(input1):
#     vowels = "aeiouAEIOU"
#     con=[]
#     for i in input1:
#         if i not in vowels:
#             con.append(i)
#     length=len(con)
#     unq=set(con)
#     d=1
#     for i in unq:
#         count=con.count(i)
#         if count>1:
#             for i in range(2,count+1):
#                 d*=i
#     p=1
#     for i in range(1,length+1):
#         p*=i
#     p//=d
#     return p
# input1=input()
# print(vowel(input1))



# s=list(map(str,input().split()))
# a=[]
# for i in s:
#     if i[:5]=='File_' and i[5:].isdigit():
#         a.append(int(i[5:]))
# print(max(a))


# def island(input1,input2,input3):
#     sweets=input2*input3
#     sun=input3//7
#     total_days=input3-sun
#     total_sweet_box=(sweets+input1-1)//input1
#     if total_sweet_box<=total_days:
#         return total_sweet_box
#     else:
#         return -1
# input1=int(input())
# input2=int(input())
# input3=int(input())
# print(island(input1,input2,input3))


# def h(input1,input2,input3):
#     c=0
#     for i in range(input1):
#         if i%5==0:
#             c+=1
#         elif i<input3:
#             c+=1
#             input3-=i
#     return c

# input1=int(input())
# input2=list(map(int,input().split()))
# input3=int(input())
# print(h(input1,input2,input3))



# def hp(input1):
#     if input1==0 or input1==1:
#         return False
#     for i in range(2,int(input1**0.5)+1):
#         if input1%i==0:
#             return False
#     return True
# def np(n):
#     sum=0
#     for i in range(n+1):
#         if hp(i):
#             sum+=i
#     return sum
# n=int(input())
# print(np(n))
          

# n=int(input())
# arr=[0,1,1]
# for i in range(3,n+1):
#     arr.append(arr[i-1]+arr[i-2]+arr[i-3])
# print(arr[n])        


# s=input()
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         print(i)
#         break


# n=int(input())
# res=1
# for i in range(1,n+1):
#     for j in range (i):
#         print(res,end=' ')
#         res=res+1
#     print()



# s=input().lower()
# t=input().lower()
# if s==t:
#     print("same")
# elif s<t:
#     print("first is smaller")
# else:
#     print("1")



# n=int(input())
# arr=[0,1,1]
# for i in range(3,n+1):
#     arr.append(arr[i-1]+arr[i-2]+arr[i-3])
# print(arr[n])

# s=input().lower()
# t=input().lower()
# if s==t:
#     print(0)
# elif s<t:
#     print(-1)
# else:
#     print(1)


# n=int(input())
# s=input()
# c=0
# for i in range(n-1):
#     if s[i]==s[i+1]:
#         c+=1
# print(c)


# def check(num):
#     if num==0 or num==1:
#         return False
#     for i in range(2,int(num**2)+1):
#         if num%i==0:
#             return False
#     return True
# a,b=list(map(int,input().split()))
# res=0
# for i in range(a+1,b+1):
#     if check(i):
#         res=i
#         break
# if res=='b':
#     print("YES")
# else:
#     print("NO")


# x1,x2,y1,y2=list(map(int,input().split()))
# if x1==x2 and y1==y2:
#     print(x1,x2,y1,y2)
# else:
#     print(-1)


a,b=input().split()
a=int('0b'+a,2)
b=int("0b"+b,2)
res=a+b
print(bin(res)[2:])