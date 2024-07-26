def count_banana_occurrences(s):
    from collections import Counter
    filtered_string=[]
    for char in s:
        if char in "BANANA":
            filtered_string.append(char)
    counts=Counter(filtered_string)      #we got count of char's from the testcase string
    required_count=Counter("BANANA")
    return min(counts[char]//required_count[char] for char in required_count)

# Test cases
input1 = "BANXXANA"
input2 = "BXXAANANXXANANAB"
output1 = count_banana_occurrences(input1)
output2 = count_banana_occurrences(input2)

print(f'Input: "{input1}" - Output: {output1}')
print(f'Input: "{input2}" - Output: {output2}')