def solution(N):
    # Convert the integer N to its binary representation and strip the '0b' prefix
    binary_representation = bin(N)[2:]
    print(binary_representation)
    max_gap = 0
    current_gap = 0
    # in_gap = False
    
    for digit in binary_representation:
        if digit == '1':
                # We have reached the end of a gap
            max_gap = max(max_gap, current_gap)
            current_gap = 0
            # in_gap = True
        else:
            # We are inside a gap
            current_gap += 1
    
    return max_gap

# Example usage:
print(solution(9))     # Output: 2
print(solution(529))   # Output: 4
print(solution(20))    # Output: 1
print(solution(15))    # Output: 0
print(solution(1041))  # Output: 5
