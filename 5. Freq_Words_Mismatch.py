def freq_words_mismatch(Text, k, d):
    freq_pattern = []   
    close = [0]*(4**k)
    freq_array = [0]*(4**k)
    
    # count all possible k-mers from Text in 4^k-sized list
    
    for i in range(len(Text)-k+1):
        neighborhood = neighbors(Text[i:i+k], d)
        for pattern in neighborhood:
            index = pattern_to_number(pattern)
            close[index] = 1
            
    # for each k-mer, check how many times it shows up in Text
    # with maximum mismatch, d
    
    for i in range(4**k):
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            freq_array[i] = approximate_pattern_count(pattern, Text, d)
    max_count = max(freq_array)
    
    for i in range(4**k):
        if freq_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            freq_pattern.append(pattern)
    return freq_pattern


# - Sample Input: ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
# - Sample Output: ATGC ATGT GATG
