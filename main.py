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



# file version
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
#     for i in unique_consonants:
#         count = consonants.count(i)
#         if count > 1:
#             for i in range(2, count + 1):
#                 denominator *= i

#     permutations = 1
#     for i in range(2, total_consonants + 1):
#         permutations *= i
#     permutations //= denominator
#     return permutations



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



# string seperated by "." find largest word
# s=input().split(".")
# m=0
# l=''
# for i in s:
#     if len(i)>m:
#         l=i
#         m=len(i)
# print(l)



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



# sum of prime numbers
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



# Floydes pattern (1)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
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



# floyds triangle(2)
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



# hallowen candies
# n=int(input())
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



# rotate array for k steps
# def rotate_array_right(arr, k):
#     if not arr:
#         return arr
#     n = len(arr)
#     k = k % n  
#     r=arr[-k:] + arr[:-k]
#     return ' '.join(map(str,r))
# arr=list(map(int,input().split()))
# k=int(input())
# print(rotate_array_right(arr,k))




# def clock_product(X, Y):
#     product = X * Y
#     hour = product % 12
#     if hour == 0:
#         hour = 12
#     return hour
# X=int(input())
# Y=int(input())
# print(clock_product(X,Y))


# def max_n_sum(input1, input2, n):
#     # Step 1: Subtract input1 from input2 element-wise
#     diff_array = [input2[i] - input1[i] for i in range(len(input1))]
    
#     # Step 2: Sort the difference array in descending order and take the first 'n' largest elements
#     max_n_elements = sorted(diff_array, reverse=True)[:n]
    
#     # Step 3: Sum the 'n' largest elements
#     result_sum = sum(max_n_elements)
    
#     return result_sum

# # Example usage:
# input1 = [3, 1, 2, 4]
# input2 = [10, 5, 6, 9]
# n = 2

# print(max_n_sum(input1, input2, n))  # Output: Sum of the 2 largest differences



# def findTheWinner(self, n: int, k: int) -> int:
#         arr = [i for i in range(1, n + 1)]
#         i = 0 
#         while len(arr) > 1:
#             idx = (i + k - 1) % len(arr)
#             arr.pop(idx)
#             i = idx
#         return arr[0]



a=list(map(int,input().split()))
v=''
for i in a:
    if i%2==0:
        v+='Even'
    else:
        v+='odd'
print(v)