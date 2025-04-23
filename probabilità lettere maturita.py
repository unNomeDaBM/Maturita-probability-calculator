import random

# The alphabet used
ABC = list("abcdefghijklmnopqrstwxyz")
# The Elenco is represented via innitials of everyone surname, the peaple we want to take as subject of observation have a "0" after the innitial
ELENCO = ["a", "a", "b0", "b", "c", "c", "c", "c", "c", "c", "d", "d", "e", "g", "l", "l0", "m", "r", "r", "r", "s", "s0", "s"]
# The number of peaple that take the exam every day
PERSONE_PER_GIORNO = 5
# The number of times we want to simulate the event
N_OF_ITERATION = 1000000


results = []

# A function that, given a starting letter, will return the number of day for the observed subjects to have, all, attended the exam
def number_of_day_for_completion(starting_letter:str):
    # Check if the "starting_letter" is even present in the "ELENCO"
    if ELENCO.count(starting_letter) > 0:
        
        # Copy the original "ELENCO" and reorder the new copy to start from the "starting_letter" 
        idx = ELENCO.index(starting_letter)
        ELENCO_copy = ELENCO.copy()
        for _ in range(idx):
            ELENCO_copy.append(ELENCO_copy[0])
            ELENCO_copy.pop(0)
        
        # Reverse the list and find the first (last in the original order) subject and its index
        ELENCO_copy.reverse()
        for i, person in enumerate(ELENCO_copy):
            if len(person) > 1:
                return len(ELENCO) - i

    # If the "startind_letter" is not present in "ELENCO" it recursively call itself with the next letter of the alphabet
    else:
        # Check if it's the last letter of the alphabet; if so, call itself from the first letter of the alphabet 
        if starting_letter == ABC[-1]:
            n_first_letter = ABC[0]
        else:
            n_first_letter = ABC[ABC.index(starting_letter) + 1]
        
        return number_of_day_for_completion(n_first_letter)


def main():
    # Iterate the "number_of_day_for_completion" function with randoms letters and store the results in the "results" list
    for _ in range(N_OF_ITERATION):
        first_letter = random.choice(ABC)
        results.append(number_of_day_for_completion(first_letter))  

    # Just to print in the console the results nicely
    for n in range(1, 24):
        res = results.count(n)
        if res == 0:
            continue
        print(f"{n} persone: {(res/N_OF_ITERATION)*100}% ---> circa {(n/PERSONE_PER_GIORNO).__ceil__()} giorni dall'inizio")


if "__main__" == __name__:
    main()
