def main():
    print("Dictionaries in Python (aka maps).")

    # polls = {} # empty dictionary

    # polls is going to be a dictionary whose keys are states and whose values are a polling percentage for a candidate in that state 
    polls: dict[str, float] = {}

    # we can set the value associated with any key
    polls["Pennsylvania"] = 0.517 
    polls["Ohio"] = 0.488
    polls["Texas"] = 0.378
    polls["Florida"] = 0.5

    print("Number of states in dictionary:", len(polls))

    polls["Vermont"] = 0.69

    print("Vermont poll:", polls["Vermont"])

    print("Number of states in dictionary:", len(polls))

    # bye Florida forever

    # is Florida in our polling data?
    if "Florida" in polls: # this is useful for checking if a key is a key of a given dictionary
        del polls["Florida"]

    print("Number of states in dictionary after Florida deletion:", len(polls))




if __name__ == "__main__":
    main()