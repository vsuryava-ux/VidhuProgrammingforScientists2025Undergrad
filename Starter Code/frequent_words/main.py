def find_frequent_words(text: str, k: int) -> list[str]:
    """
    Returns a list containing the most frequent k-mers occurring in text, 
    including overlaps.
    
    Parameters:
    - text (str): The input string.
    - k (int): The size of the k-mers.
    
    Returns:
    - list[str]: The most frequent k-mers in text.
    """
    # TODO: Implement this function
    if k <= 0:
        raise ValueError("k is not positive.")
    if k > len(text):
        return []
    
    freq_patterns = []

    # let's hand off most of the hard labor to a subroutine, to build a frequency table
    freq_map = frequency_table(text, k)

    # what is the maximum value? Again we pass this task to a subroutine
    max_val = max_map_value(freq_map)

    # range over all the keys in the dictionary and if anybody has a value equal to max, add it to freq_patterns.
    for pattern, val in freq_map.items():
        if val == max_val:
            # found a pattern occuring max times
            freq_patterns.append(pattern)

    return freq_patterns


def frequency_table(text: str, k: int) -> dict[str, int]:
    """
    Builds a frequency table of all k-mers of length k in the given text, 
    including overlaps.
    
    Parameters:
    - text (str): The input string.
    - k (int): The size of the k-mers.
    
    Returns:
    - dict[str, int]: A dictionary mapping each k-mer to its frequency.
    """
    # TODO: Implement this function
    if k <= 0:
        raise ValueError("k is not positive.")
    if k > len(text):
        return []
    
    freq_map: dict[str, int] = {}

    # range over all k-mer substrings of the text
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]

        # does pattern exist in freq_map??
        # if not, then we create it as an entry
        """
        if not(pattern in freq_map):
            freq_map[pattern] = 1
        else:
            # we have seen it
            freq_map[pattern] += 1
        """
        
        # shortcut approach using get()
        # get() takes two parameters: the key to retrieve, and a default value to assign it if it doesn't exist as a key
        freq_map[pattern] = freq_map.get(pattern, 0) + 1

    return freq_map

    


def max_map_value(dictionary: dict[str, int]) -> int:
    """
    Finds the maximum value in a dictionary with string keys and integer values.
    
    Parameters:
    - dictionary (dict[str, int]): The dictionary to evaluate.
    
    Returns:
    - int: The maximum value in the dictionary.
    
    Raises:
    - ValueError: If the dictionary is empty.
    """
    # TODO: Implement this function
    if len(dictionary.keys()) == 0:
        raise ValueError("Dictionary empty")

    m = 0
    # one fix, m is the smallest possible integer allowed
    # second fix, use a boolean flag
    first_time_through = True

    # range through the dictionary, and find anybody that can beat the current value of m, updating m
    for _, val in dictionary.items():
        if val > m or first_time_through:
            # update m
            m = val  # this sets m to a value in the dictionary, so comparisons should be fine now
            # turn off light
            first_time_through = False

    return m




def main():
    """
    Main entry point for testing frequent words finder.
    """
    print("Finding frequent words in Python!")
    
    # Small example test case
    text = "ACGTTTTGAGACGTTTACGC"
    k = 3
    print(find_frequent_words(text, k))
    
    # Uncomment this block to experiment with the Vibrio cholerae ori region
    """
    text = ("ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGG"
            "ATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAA"
            "GAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCA"
            "GCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTG"
            "TTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTA"
            "CTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGAT"
            "CATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCT"
            "TGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGT"
            "TTC")
    for k in range(3, 10):
        print(k, find_frequent_words(text, k))
    """


if __name__ == "__main__":
    main()


"""
Pseudocode
"""

"""
FrequencyTable(text, k)
    freqMap ← empty map
    n ← length(text)
    for every integer i between 0 and n − k
        pattern ← text[i, i + k]
        if freqMap[pattern] doesn't exist
            freqMap[pattern] = 1
        else
            freqMap[pattern]++
    return freqMap
"""

"""
BetterFrequentWords(text, k)
    frequentPatterns ← an array of strings of length 0
    freqMap ← FrequencyTable(text, k)
    max ← MaxMapValue(freqMap)
    for all strings pattern in freqMap
        if freqMap[pattern] = max
            frequentPatterns ← append(frequentPatterns, pattern)
    return frequentPatterns
"""

"""
MaxMapValue(dict)
    m ← 0
    firstTime = true
    for every key pattern in dict
        if firstTime = true or dict[pattern] > m
            firstTime= false
            m ← dict[pattern]
    return m
"""