import random  # for generating random numbers

from election_io import read_electoral_votes, read_polling_data 

# final way: import all functions from package
# from election_io import *

def main() :
	print("Let's simulate an election!")
     




def simulate_multiple_elections(electoral_votes: dict[str, int], polling_data: dict[str, float], num_trials: int, margin_of_error: float) -> tuple[float, float, float]:
    """
    simulates an election multiple times, calculating winning probabilities.

    polls: maps state names to candidate percentages
    electral_votes: maps state names to electoral college votes
    num_trials: number of trails to simulate
    margin_of_error: margin of error of each poll

    Returns: tuple of 3 floats corresponding to percentages of simulations won by candidate 1, candidate 2, and a tie
    """
    if num_trials <= 0:
         raise ValueError("Number of trials must be positive.")
    if margin_of_error < 0:
         raise ValueError("Margin of error must be positive.")
    
    
    win_count_1 = 0  # keeps track of the number of times candidate 1 wins
    win_count_2 = 0  # keeps track of the number of times candidate 2 wins
    tie_count = 0  # keeps track of the number of times both candidates tie
      
    for i in range(1, num_trials + 1):
        # simulate one election
        votes_1, votes_2 = simulate_one_election(electoral_votes, polling_data, margin_of_error)  # this gives EC votes for candidate 1 and 2
        if votes_1 > votes_2:
            win_count_1 += 1  # if EC votes for 1 are greater than that for 2, 1 will win
        elif votes_2 > votes_1:
            win_count_2 += 1  # if EC votes for 2 are greater than that for 1, 2 will win
        else:
             tie_count += 1
    
    probability_1  = win_count_1 / num_trials
    probability_2 = win_count_2 / num_trials
    probability_tie = tie_count / num_trials  # these compute the probabilities of each possible outcome

    return (probability_1, probability_2, probability_tie)


def simulate_one_election(electoral_votes: dict[str, int], polling_data: dict[str, float], margin_of_error: float) -> tuple[int, int]:
    """
    Simulates one presidential election between two candidates using polling data and returns the # of electoral college votes for each candidate.

    polls: maps state names to candidate percentages
    electral_votes: maps state names to electoral college votes
    margin_of_error: margin of error of each poll

    Returns: tuple of 2 integers representing the EC votes for candidate 1 and candidate 2
    """
    if margin_of_error < 0:
         raise ValueError("MOE can't be negative.")
    
    college_votes_1 = 0
    college_votes_2 = 0  # variables to store number of EC votes for each candidate

    # range over all of the states (keys of either polls or electoral_votes), and simulate an election in each one
    for state_name, polling_value in polling_data.items():
        # we also need to know how many votes this state is worth
        num_votes = electoral_votes[state_name]

        # we need to adjust the polling value in a random direction

        adjusted_polling_value = add_noise(polling_value, margin_of_error)

        if adjusted_polling_value > 0.5:
            college_votes_1 += num_votes

        else:
            college_votes_2 += num_votes

        # based on who won, we add num_votes to their tally
    

    return college_votes_1, college_votes_2






def add_noise(polling_value: float, margin_of_error: float) -> float:
     """
     Adds random noise to a polling value.

     polling_value: the polling value for candidate 1
     margin_of_error: the margin of error for this poll

     Returns: float corrsponding to the adjusted polling value after assigning some boise for candidate 1 with the given margin of error
     """

     # grab a number from the standard normal
     x = random.gauss(0, 1)  # first parameter is the mean and the second parameter is the standard deviation

     # we need to transform this into something we can add to the polling value

     # for a standard normal, the margin of error is 2x the standard_deviation

     # what we wanted to generate is something with a standard deviation of margin_of_error/2

     x /= 2.0 # now the standard deviation is 0.5 and the MOE is 1

     # now multiply it by the margin_of_error
     x *= margin_of_error  # now the standard dev is 0.5 * MOE, and the margin of error is MOE


     return x + polling_value



    


def simulate_state_once(poll: float, margin_of_error: float) -> bool:
    """
    This function decides the election winner of one state only. It adds noise to the states polling percentage for candidate 1 and returns a boolean of whether the candidate wins or loses

    poll: this is a float that represents candidate 1's polling share in the state
    margin_of_error: this is a float that represents the margin of error around the poll, which measures the uncertainty of which value represents the population level polling share for candidate 1

    Returns: bool representing whether candidate 1 wins or loses accounting for some flucuations in the poll from the margin of error
    """

    x = random.gauss(0, margin_of_error / 2)  # this will essentially return a random value from the standard normal distribution, such that the standard deviation in this distribution is margin_of_error/2. This will ensure that our 95% confidence interval is from [-margin_of_error, margin_of_error] because confidence intervals always have to be within 2 standard deviations from the center

    # the x value that is generated essentially represents our "noise", or the magnitude of the flucuation of poll within its confidence interval. Thus, we can complete the flucuation by adding x to poll

    adjusted_poll = x + poll

    if adjusted_poll >= 0.5:
         return True  # this means that with the adjusted poll, candidate 1 will win
    
    return False  # if the adjusted poll is not greater than or equal to 0.5, then candidate 1 will lose in this simulation








if __name__ == "__main__":
    main()