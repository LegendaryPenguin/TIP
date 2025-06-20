# def arrange_guest_arrival_order(arrival_pattern):
#     answer = []
#     stack = []
#     for i in range(1, len(arrival_pattern) + 2):
#         stack.append(i)
#         if i == len(arrival_pattern) + 1 or arrival_pattern[i-1] == 'I':
#             while stack:
#                 answer.append(stack.pop())
    
#     return answer

# # method 2: stack
# def arrange_guest_arrival_order1(arrival_pattern):
    
#     answer = []
#     later = []
#     # iterating through the list backwards
#     for i in range(len(arrival_pattern)+1):
#         if i == len(arrival_pattern):
#             if arrival_pattern[i-1] == 'D':
#                 later.append(i+1)
#             if arrival_pattern[i-1] == 'I':
#                 answer.append(i+1)
#         elif arrival_pattern[i] == 'D':
#             later.append(i+1)
#         elif arrival_pattern[i] == 'I':
#             answer.append(i+1)
#             while later:
#                 answer.append(later.pop())
#             later = []
#     while later:
#         answer.append(later.pop())
#     return answer



# print(arrange_guest_arrival_order1("IIIDIDDD"))  
# print(arrange_guest_arrival_order1("DDD"))  