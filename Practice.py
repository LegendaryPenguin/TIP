
# def reveal_attendee_list_in_order(attendees):
#   attendees.sort()
#   original = []
#   for i in range (len(attendees)):
#       if i


# def reveal_attendee_list_in_order1(attendees):
#   pass

from collections import deque
# def blueprint_approval(blueprints):     
#     yay = deque()
#     for i in blueprints:
#         if not yay or i > yay[0]:
#             yay.append(i)
#         elif i < yay[0]:
#             yay.appendleft(i)
#     return list(yay)

# def main():
#     print(blueprint_approval([3, 5, 2, 1, 4])) 
#     print(blueprint_approval([7, 4, 6, 2, 5])) 
# main()

# def build_skyscrapers(floors):
#     yay = deque()
#     # answer = 1
#     # for i in floors:
#     #     if not yay:
#     #         yay.append(i)
#     #     elif i <= yay[-1]:
#     #         yay.append(i)
#     #     else:
#     #         while yay:
#     #             yay.pop()
#     #         answer +=1
#     #         yay.append(i) 
#     # return answer
#     tops = []
#     front = 0
#     for i in range (len(floors)):
#         front = floors[i-1]
#         if not tops:
#             tops.append(floors[i])
#         elif floors[i] > front:
#             tops.append(floors[i])
#         else:
#             pass
        
#     return len(tops)

# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

# def max_corridor_area(segments):
#     maximum = 0
#     for i in range (len(segments)):
#         for j in range (i+1, len(segments)):
#             maximum = max(maximum, (j-i) * min(segments[i], segments[j]))
                
#     return maximum
# def max_corridor_area(segments):
#     left = 0
#     right = len(segments) - 1
#     answer = 0
#     while right > left:
#         answer = max(min(segments[right], segments[left]) * (right - left), answer)
        
#         if right > left:
#             left +=1
#         else:
#             right -=1
#     return answer

# print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
# print(max_corridor_area([1, 1])) 

def min_swaps(s):
    stack = []
    swaps = 0
    balance = 0
    for i in s:
        if i == "[":
            balance += 1
        if i == ']':
            balance -= 1
        if balance < 0:
            swaps += 1
            balance = 1
    return swaps
print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  