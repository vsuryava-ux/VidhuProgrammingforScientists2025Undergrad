# Pseudocode from the learning objectives (for reference)
import requests

def main():
    print("Finding clumps.")

    text = "AAAACGTCGAAAA"
    k = 3
    window_length = 4
    t = 2

    # should print "AAA"
    print(find_clumps(text, k, window_length, t))

    url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"

    response = requests.get(url)

    response.raise_for_status() # give us an error if there was a problem 

    genome = response.text

    print("Genome has length", len(genome), "nucleotides.")

    # call the clump finding algorithm
    k = 9
    window_length = 500  # practical length for ori region
    t = 3

    patterns = find_clumps(genome, k, window_length, t)


    print("Success!")
    print("We found", len(patterns), "total patterns that form clumps")



"""
FindClumps(text, k, L, t)
    patterns ← an array of strings of length 0
    n ← length(text)
    for every integer i between 0 and n − L
        window ← text[i, i + L]
        freqMap ← FrequencyTable(window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t and Contains(patterns, s) = false
                patterns ← append(patterns, s)
    return patterns
"""

"""
Contains(patterns, s)
    for every string pattern in patterns
        if s = pattern
            return true
    return false
"""



def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times
    in a window of given length in the string.

    Parameters:
    - text (str): The input string.
    - k (int): The k-mer length.
    - window_length (int): Length L of the sliding window.
    - t (int): Frequency threshold within a window.

    Returns:
    - list[str]: All distinct k-mers forming (L, t)-clumps in text.

    Notes:
    - Follow the pseudocode in FIND_CLUMPS_PSEUDOCODE.
    - Build a frequency table for each window using `frequency_table`.
    - Use `contains` to avoid duplicates (or see the faster variant below).
    """
    # TODO: Implement this function
    patterns = []
    n = len(text)  # finds the length of the dna string

    # range over all windows (all substrings having length window_length in the text)
    for i in range(0, n-window_length+1):
        current_window = text[i:i+window_length]  # this takes a slice of the dna string isolating just the window we are considering
        freq_map = frequency_table(current_window, k)  # this will essentially create a dictionary that maps all substrings of length k within current_window to their number of occurences

        # find any k-mers in the table that occur at least t times and have we not seen it before
        for pattern, occurences in freq_map.items():
            # does it occur at least t times and is it not already in our list that we are accumulating?
            if occurences >= t and (pattern not in patterns):
                patterns.append(pattern)


    return patterns  # the list returned is a list of all substrings of length k that occur greater than or equal to t times in a window of a given length, so it returns substrings that occur in close proximity to one another


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






def contains(patterns: list[str], s: str) -> bool:
    """
    Returns True if s appears in the list `patterns`, else False.

    Parameters:
    - patterns (list[str]): A list of strings.
    - s (str): Query string.

    Returns:
    - bool: True if s ∈ patterns, else False.

    Hint:
    - You may use the `in` operator or a manual loop, per the code along.
    """
    # TODO: Implement this function
    
    # we can pass this function as we have a simple way of seeing whether a key is within a dictionary or not
    pass




if __name__ == "__main__":
    main()