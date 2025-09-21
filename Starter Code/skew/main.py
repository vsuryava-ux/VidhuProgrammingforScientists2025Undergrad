from matplotlib import pyplot

import urllib.request

def main():
    print("Building a skew array.")

    # --- Tiny local demo (uncomment after implementing functions) ---
    """
    demo_genome = "CATGGGCATCGGCCATACGCC"
    arr = skew_array(demo_genome)
    print("Demo skew array length:", len(arr))
    print("First few values:", arr[:10])
    print("Minimum skew indices (demo):", minimum_skew(demo_genome))
    """

    # --- E. coli genome experiment & plotting (uncomment to run) ---
    """
    demo_genome = "CATGGGCATCGGCCATACGCC"
    arr = skew_array(demo_genome)
    print("Demo skew array length:", len(arr))
    print("First few values:", arr[:10])
    print("Minimum skew indices (demo):", minimum_skew(demo_genome))
    """

    # --- E. coli genome experiment & plotting (uncomment to run) ---
    """
    url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
    contents = urllib.request.urlopen(url)

    # Check status code
    if contents.getcode() != 200:
        raise urllib.error.URLError("Bad status code")

    # Read and decode
    contents = contents.read()
    genome = contents.decode('utf-8')
    if not genome:
        raise ValueError("Downloaded genome sequence is empty.")

    print("The number of nucleotides in E. coli genome is " + str(len(genome)))

    ecoli_skew_array = skew_array(genome)
    min_skew_positions = minimum_skew(genome)
    if len(min_skew_positions) == 0:
        raise RuntimeError("No minimum positions found (unexpected).")

    first_pos = min_skew_positions[0]
    print(
        "The minimum skew value of "
        + str(ecoli_skew_array[first_pos])
        + " occurs at positions "
        + str(min_skew_positions)
    )

    # Plot (requires matplotlib)
    
    draw_skew(ecoli_skew_array)
    print("Skew diagram drawn! Exiting normally.")
    """

"""
SkewArray(genome)
    n ← length(genome)
    array ← array of length n + 1
    array[0] ← 0
    for every integer i between 1 and n
        array[i] = array[i-1] + Skew(genome[i-1])
    return array
"""

"""
Skew(symbol)
    if symbol = 'G'
        return 1
    else if symbol = 'C'
        return -1
    return 0
"""

"""
MinimumSkew(genome)
    indices ← array of integers of length 0
    n ← length(genome)
    array ← SkewArray(genome)
    m ← MinIntegerArray(array)
    for every integer i between 0 and n
        if array[i] = m
            indices = append(indices, i)
    return indices
"""

def skew_array(genome: str) -> list[int]:
    """
    Returns the skew array for `genome`, where skew[i] is the difference
    (# of 'G') - (# of 'C') in genome[0:i].

    Parameters:
    - genome (str): DNA string.

    Returns:
    - list[int]: Skew array of length len(genome) + 1.

    Raises:
    - ValueError: If genome is empty.
    """
    if len(genome) == 0:
        raise ValueError("Zero length genome given.")
    
    n = len(genome)

    # define a skew array
    skew_array = [0] * n+1  # we do n+1 because a given index of the skew_array is 1 plus the current value of the nucleotides we are counting. So an element of this list at n+1 is equal to the GC skew from the first nucleotide to the nth nucleotide.

    # range over genome, and set skew_array[i-1] using previous value

    for i in range(1, n+1):
        skew_array[i] = skew_array[i-1] + skew(genome[i-1])  # this essentially takes the previous element of skew array and calls a subroutine which adds or subtracts 1 if the next nucleotide encountered is G or C

    return skew_array




def skew(symbol: str) -> int:
    """
    Returns 1 if symbol is 'G'/'g', -1 if 'C'/'c', else 0.

    Parameters:
    - symbol (str): Single-character string.

    Returns:
    - int: Skew contribution for this symbol.

    Raises:
    - ValueError: If `symbol` is not length 1.
    """
    
    if len(symbol) != 1:
        raise ValueError("Length of string must be 1.")

    if symbol == "G" or symbol == "g":
        return 1
    elif symbol == "C" or symbol == "c":
        return -1
    else:
        return 0




def MinIntegerArray(a: list[int]) -> int:
    """
    Takes in an array of integers. Returns the minimum integer in this array.

    a: integer array

    Returns: minimum element of a
    """
    if len(a) == 0:
        raise ValueError("List cannot be empty.")
    
    min = a[0]  # assumes for now that the first element is the minimum

    for element in a:
        if min > element:  # ranges through the elements of a and if it finds an element less than the current min, then min gets assigned to this element
            min = element

    return min


def minimum_skew(genome: str) -> list[int]:
    """
    Returns all indices i (0..len(genome)) where the skew array achieves
    its minimum value.

    Parameters:
    - genome (str): DNA string.

    Returns:
    - list[int]: Indices where skew is minimal.

    Raises:
    - ValueError: If genome is empty.
    """
    
    if len(genome) == 0:
        raise ValueError("Empty genome given.")
    
    # create list of indices
    indices = []

    skew_arr = skew_array(genome)

    # find the minimum value
    m = MinIntegerArray(skew_arr)

    # range over the skew array, and find all indicies where val = m
    for i in range(0, len(skew_arr)):
        if skew_arr[i] == m:
            indices.append(i)

    return indices



def draw_skew(skew_list: list[int]) -> None:
    """
    draw_skew draws a skew diagram using a skew_array output.
    
    """
    if len(skew_list) == 0:
        raise ValueError("skew_list is empty")
    pyplot.plot(skew_list)
    pyplot.title("Skew Diagram")
    pyplot.xlabel("Genome Position")
    pyplot.ylabel("Skew Value")
    pyplot.savefig("skewDiagram.png")

if __name__ == "__main__":
    main()