import random
from strategies import letter_frequency, position_frequency, choose_best_word
from load_data import solution_words, allowed_words

# FEEDBACK

def feedback(guess, solution):
    fb = ['X'] * 5
    solution_letters = list(solution)

    # first pass: correct letters
    for i in range(5):
        if guess[i] == solution[i]:
            fb[i] = 'G'
            solution_letters[i] = None

    # second pass: letters in word but wrong position
    for i in range(5):
        if fb[i] == 'X' and guess[i] in solution_letters:
            fb[i] = 'Y'
            solution_letters[solution_letters.index(guess[i])] = None
    return ''.join(fb)

# FILTER WORDS

def filter_words(possible_words, guess, fb):
    filtered = []

    for word in possible_words:
        match = True
        for i in range(5):
            if fb[i] == 'G' and word[i] != guess[i]:
                match = False
                break
            if fb[i] == 'Y':
                if guess[i] not in word or word[i] == guess[i]:
                    match = False
                    break
            if fb[i] == 'X' and guess[i] in word:
                match = False
                break
        if match:
            filtered.append(word)
    return filtered

# SIMULATE SINGLE GAME

def simulate_single_game(solution, allowed_words, solution_words, w1, w2):
    possible_words = solution_words.copy()
    max_guesses = 6
    guesses = 0

    while guesses < max_guesses:
        lf = letter_frequency(possible_words)
        pf = position_frequency(possible_words)
        guess = choose_best_word(allowed_words, lf, pf, w1, w2)
        guesses += 1
        fb = feedback(guess, solution)
        if fb == 'GGGGG': # solution was found
            break
        possible_words = filter_words(possible_words, guess, fb)
        if len(possible_words) == 0:
            break
    return guesses

# RUN SIMULATIONS

def run_simulations(num_games, w1, w2):
    total_guesses = 0

    for i in range(num_games):
        solution = random.choice(solution_words)
        g = simulate_single_game(solution, allowed_words, solution_words, w1, w2)
        total_guesses += g
        # if i % 100 == 0:
            # print(f"{i} games simulated")
    
    avg_guesses = total_guesses / num_games
    print(f"Average guesses for w1 = {w1}, w2 = {w2}: {avg_guesses}")
    return avg_guesses

# MAIN

if __name__ == "__main__":
    run_simulations(500, 0.7, 0.3)