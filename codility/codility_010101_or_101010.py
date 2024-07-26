def min_flips_to_alternating(coins):
    # Define two possible alternating patterns
    # pattern1 = ['0', '1','0', '1','0', '1','0', '1'] 
    #or
    pattern1=["0","1"]* (len(coins) // 2 + 1)
    pattern2 = ['1', '0','1', '0','1', '0','1', '0'] 
    # * (len(coins) // 2 + 1)

    flips_to_pattern1=0
    for i in range(len(coins)):
                   if coins[i] != pattern1[i]:
                           flips_to_pattern1 +=1
    
    flips_to_pattern2=0
    for i in range(len(coins)):
                   if coins[i] != pattern2[i]:
                           flips_to_pattern2 +=1

    # Return the minimum flips required
    return min(flips_to_pattern1, flips_to_pattern2)

# Example usage:
coins = ['0', '1', '0',"0,'0","1","1"]
print(min_flips_to_alternating(coins))  # Output: 2
