import random
from strategies import letter_frequency, position_frequency, choose_best_word
import pandas as pd

def feedback(guess, solution):
    """Return feedback: G=green, Y=yellow, B=black/grey"""
    fb = ['B'] * 5
    solution_letters = list(solution)
    # First pass: correct letters
    for i in range(5):
        if guess[i] == solution[i]:
            fb[i] = 'G'
            solution_letters[i] = None
    # Second pass: letters in word but wrong position
    for i in range(5):
        if fb[i] == 'B' and guess[i] in solution_letters:
            fb[i] = 'Y'
            solution_letters[solution_letters.index(guess[i])] = None
    return ''.join(fb)

def filter_words(possible_words, guess, fb):
    """Filter word list based on feedback"""
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
            if fb[i] == 'B' and guess[i] in word:
                match = False
                break
        if match:
            filtered.append(word)
    return filtered

def simulate_single_game(solution, allowed_words, solution_words, w1=0.5, w2=0.5, max_guesses=6):
    """Simulate one Wordle game using a strategy"""
    possible_words = solution_words.copy()
    guesses = 0
    while guesses < max_guesses:
        lf = letter_frequency(possible_words)
        pf = position_frequency(possible_words)
        guess = choose_best_word(allowed_words, lf, pf, w1, w2)
        guesses += 1
        fb = feedback(guess, solution)
        if fb == 'GGGGG':
            break
        possible_words = filter_words(possible_words, guess, fb)
        if len(possible_words) == 0:
            break
    return guesses

def run_simulations(num_games=1000, w1=0.5, w2=0.5):
    """Run multiple simulations and compute average guesses"""
    solution_words_df = pd.read_csv("solution_words.csv")['word'].tolist()
    allowed_words_df = pd.read_csv("allowed_words.csv")['word'].tolist()
    total_guesses = 0
    for i in range(num_games):
        solution = random.choice(solution_words_df)
        g = simulate_single_game(solution, allowed_words_df, solution_words_df, w1, w2)
        total_guesses += g
        if i % 100 == 0:
            print(f"{i} games simulated")
    avg_guesses = total_guesses / num_games
    print(f"Average guesses for w1={w1}, w2={w2}: {avg_guesses}")
    return avg_guesses

if __name__ == "__main__":
    run_simulations(500, w1=0.7, w2=0.3)