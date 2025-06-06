'''
Problem 1
Write a function linear_search() to help Winnie the Pooh locate his lost items. 
The function accepts a list items and a target value as parameters. 
The function should return the first index of target in items, and -1 if target is not in the lst. 
Do not use any built-in functions.
'''
# def linear_search(items, target):
#     index = 0

#     while index < len(items):
#         if items[index] == target:
#             return index
#         else:
#             index += 1
#     return -1

# def main():
#     items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
#     target = 'hunny'
#     print(linear_search(items, target))
#     items1 = ['bed', 'blue jacket', 'red shirt', 'hunny']
#     target2 = 'red balloon'
#     print(linear_search(items1, target2))
    
# main()
'''
Problem 2
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
    bouncy and flouncy both increment the value of the variable tigger by 1.
    trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, 
return the final value of tigger after performing all the operations.
'''  

# def final_value_after_operations(operations):
#     tigger = 1
#     for i in operations:
#         if i == 'bouncy' or i == 'flouncy':
#             tigger += 1 
#         if i == 'trouncy' or i == 'pouncy':
#             tigger -= 1 
#     return tigger

# def main():
#     operations = ["trouncy", "flouncy", "flouncy"]
#     print(final_value_after_operations(operations))

#     operations1 = ["bouncy", "bouncy", "flouncy"]
#     print(final_value_after_operations(operations1))
    
# main()
        
'''
Problem 3
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() 
that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. 
The function should be case insensitive.
'''

# def tiggerfy(word):
#     word1 = word.strip().lower()
#     # operator = True
#     if 't' or 'i' or 'gg' or 'er' in word1:
#         word = word.replace ('t', '')
#         word = word.replace ('T', '')
#         word = word.replace ('i', '')
#         word = word.replace ('I', '')
#         word = word.replace ('er', '')
#         word = word.replace ('Er', '')
#         word = word.replace ('gg', '')
#         return word

# def main():
#     word = "Trigger"
#     print(tiggerfy(word))


#     word1 = "eggplant"
#     print(tiggerfy(word1))

#     word2 = "Choir"
#     print(tiggerfy(word2))
    
# main()

'''
Question 4
Given an array nums with n integers, write a function non_decreasing() that checks if nums 
could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
such that (0 <= i <= n - 2).

'''
# def non_decreasing(nums):
#     hasOneFlag = True 
#     flags = 0
#     for i in range(len(nums) -1):
#         if nums[i] <= nums[i + 1]:
#             pass
#         else:
#             flags += 1
            
#     if flags > 1:
#         hasOneFlag = False
#         return hasOneFlag
#     else:
#         hasOneFlag = True
#         return hasOneFlag
        
        

# def main():
#     nums = [4, 2, 3]
#     print(non_decreasing(nums))

#     nums1 = [4, 2, 1]
#     print(non_decreasing(nums1))
# main() 


# Problem 5
# def find_missing_clues(clues, lower, upper):
#     missing_list = []
#     i = lower
#     while i <= upper:
#         if i not in clues:
#             start = i
#             while i <= upper and i not in clues:
#                 i += 1
#             end = i-1
#             missing_list.append([start, end])
#         else: 
#             i += 1
#     return missing_list

# def main():
#     clues = [0, 1, 3, 50, 75]
#     lower = 0
#     upper = 99
#     print(find_missing_clues(clues, lower, upper))
    
# main()

# Problem 6
# def harvest(vegetable_patch):
#     count = 0
#     for i in vegetable_patch:
#         for j in i:
#             if j == 'c':
#                 count += 1
#     return count

# def main():
#     vegetable_patch = [
# 	['x', 'c', 'x'], ['x', 'x', 'x'], ['x', 'c', 'c'], ['c', 'c', 'c']
#     ]
#     # print (len(vegetable_patch))
#     print(harvest(vegetable_patch))
# main()

# Problem 7
# def good_pairs(pile1, pile2, k):
#     pairs = 0
#     for i in pile1:
#         for j in pile2:
#             if i % (j*k) == 0:
#                 pairs += 1
#     return pairs
                

# def main():
#     pile1 = [1, 3, 4]
#     pile2 = [1, 3, 4]
#     k = 1
#     print(good_pairs(pile1, pile2, k))

#     pile3 = [1, 2, 4, 12]
#     pile4 = [2, 4]
#     k2 = 3
#     print(good_pairs(pile3, pile4, k2))
# main()

# Problem 8
# def local_maximums(grid):
#     n = len(grid)
#     local_maxes = []
    
#     for i in range(1, n-1): 
#         row_maxes = []
#         for j in range(1, n-1):
#             max_val = max(grid[x][y] for x in range (i-1, i+2) for y in range (j-1, j+2))
#             row_maxes.append(max_val)
#         local_maxes.append(row_maxes)    
    
#     return local_maxes        


# def main():
#     grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
#     ]
#     print(local_maximums(grid))
# main() 




# Problem 1
# def transpose(matrix):
#     rows = len(matrix)
#     col = len(matrix[0])
#     transposed = []    
#     for i in range (col):
#         new_row = []
#         for j in range (rows):
#             new_row.append(matrix[j][i])
#         transposed.append(new_row)
#     return transposed

# def main():
#     matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#     ]
#     matrix = transpose(matrix)
#     matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6]
#     ]
#     matrix1 = transpose(matrix1)
#     for row in matrix:
#         print (row)
#     for row1 in matrix1:
#         print (row1)
        
# main()

# Problem 2
# def reverse_list(lst):
#     left = 0
#     right = len(lst) - 1
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst
    
# def main():
#     lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
#     print(reverse_list(lst))
# main()


# Problem 1
# def add_matrices(matrix1, matrix2):
#     rows = len(matrix1)
#     col = len(matrix1[0])

#     emptyRow = [0 for i in range(col)]
#     sum_matrix = [emptyRow for i in range(rows)]

#     for i in range(rows):
#         for j in range(col):
#             sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    

#     # sum_matrix = []
#     # for i in range (rows):
#     #     row_add = []
#     #     for j in range (col):
#     #         row_add.append(matrix1[i][j] + matrix2[i][j])
#     #     sum_matrix.append(row_add)
#     return sum_matrix
            


# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# print(add_matrices(matrix1, matrix2))

'''
1. We take in a string
If left and right letters for each index match until the middle, its a palindrome: True
Otherwise return False
Left Pointer: Starts index 0
Right Pointer: Starts at len(string) - 1

We keep updating the pointers inwards while Left < Right
'''
# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# s = "madam"
# print(is_palindrome(s))

# s = "madamweb"
# print(is_palindrome(s))


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if target == nums[left] + nums[right]:
            return [left, right]
        elif target > nums[left] + nums[right]:
            left += 1
        else:
            right -= 1
    print ("Target cannot be found")


# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))

# nums = [2, 7, 11, 15]
# target = 18
# print(two_sum(nums, target))


def two_sum(nums, target):
    seen = set()
    used = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen and (complement, num) not in used:
            pairs.append([complement, num])
            used.add((complement, num))
            used.add((num, complement))  # prevent reversed duplicates
        seen.add(num)

    return pairs

def three_sum(nums):
    nums.sort()  # Step 1: Sort the list
    result = []

    for i in range(len(nums)):
        # Step 2: Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Step 3: Find pairs that sum to -nums[i]
        current = nums[i]
        pairs = two_sum(nums[i + 1:], -current)

        for pair in pairs:
            triplet = [current] + pair
            if triplet not in result:  # Optional check, helps ensure uniqueness
                result.append(triplet)

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))