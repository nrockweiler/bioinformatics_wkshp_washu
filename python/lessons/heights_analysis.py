def calculate_mean(heights):
    '''
    Calculate and returns the mean of a list of heights.
    '''
    total = 0
    for height in heights:
        total = total + float(height)

    return total/len(heights)
    

def calculate_variance(heights):
    '''
    Calculates and returns the variance of a list of heights.
    '''
    sum_diffsq = 0
    for height in heights:
        diff = float(height)-calculate_mean(heights)
        diff_sq = diff**2
        sum_diffsq = sum_diffsq + diff_sq
        
    return sum_diffsq/(len(heights)-1)


