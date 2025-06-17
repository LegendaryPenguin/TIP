# words = ['banana', 'apple', 'apple', 'apple', 'orange', 'banana', 'apple']
# words.sort()
# freq = {}
# # for i in words:
# #     if i in freq:
# #         freq[i] += 1
# #     else:
# #         freq[i] = 1
        
# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print (freq)


def find_difference(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    diff1 = []
    