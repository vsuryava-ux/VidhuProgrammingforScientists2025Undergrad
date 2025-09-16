import random  # for generating random numbers

def main() :
	print("Let's simulate an election!")
      

"""
SimulateMultipleElections(pollingData, numTrials, marginOfError)
    winCount1 ← 0
    winCount2 ← 0
    tieCount ← 0
    for numTrials total trials
        votes1,votes2 ← SimulateOneElection(pollingData, marginOfError)
        if votes1 > votes2
            winCount1 ← winCount1 + 1
        else if votes2 > votes1
            winCount2 ← winCount2 + 1
        else (tie!)
            tieCount ← tieCount + 1
    probability1 ← winCount1/numTrials
    probability2 ← winCount2/numTrials
    probabilityTie ← tieCount/numTrials
    return probability1, probability2, probabilityTie
"""

def simulate_multiple_elections(polls: dict[str, float], electoral_votes: dict[str, int], num_trials: int, margin_of_error: float) -> Tuple[float, float, float]
    """
    Simulates election multiple times, calculating winning "probabilities".

    Parameters:
    - polls: maps state names to candidate 1 percentages
    - electoral_votes: maps state names to electoral college votes 
    - num_trials: number of trials to simulate 
    - margin_of_error: margin of error of each poll

    Returns:
    - tuple of 3 floats corresponding to percentages of simulations won by candidate 1, candidate 2, and a tie
    """

    if num_trials <= 0:
         raise ValueError("Number of trials must be positive.")
    if margin_of_error < 0:
         raise ValueError("Margin of error must be non-negative.")

    # keep track of number of simulations won in each of three cases
    win_count_1 = 0
    win_count_2 = 0
    tie_count = 0

    # simulations go here

    for _ in range(num_trials):
        # simulate one election, giving EC votes for candidate 1 and 2
        votes_1, votes_2 = simulate_one_election(polls, electoral_votes, margin_of_error)
        # who won? 
        if votes_1 > votes_2:
           win_count_1 += 1 # candidate 1 
        elif votes_2 > votes_1:
             win_count_2 += 1 # candidate 2
        else:
             # worst possible outcome, tie! 
             tie_count += 1


    probability_1 = win_count_1/num_trials 
    probability_2 = win_count_2/num_trials 
    probability_tie = tie_count/num_trials 

    return probability_1, probability_2, probability_tie

def simulate_one_election(polls: dict[str, float], electoral_votes: dict[str, int], margin_of_error: float) -> Tuple[int, int]:
    """
    Simulates one presidential election between two candidates using polling data and a given margin of error, and returns the # of electoral college votes for each candidate.

    Parameters:
    - polls: maps state names to candidate 1 percentages
    - electoral_votes: maps state names to electoral college votes 
    - margin_of_error: margin of error of each poll
    
    Returns:
    - tuple of 2 integers corresponding to # of EC votes for candidate 1 and candidate 2, respectively, after one simulation
    """

if __name__ == "__main__":
    main()