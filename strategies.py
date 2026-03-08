import pandas as pd
from collections import Counter

def letter_frequency(words):
    """Return frequency of letters in a list of words"""
    all_letters = ''.join(words)
    freq = Counter(all_letters)
    return freq

def position_frequency(words):
    """Return frequency of letters in each position"""
    position_freq = [Counter() for _ in range(5)]
    for word in words:
        for i, letter in enumerate(word):
            position_freq[i][letter] += 1
    return position_freq

def score_word(word, letter_freq, pos_freq, w1=0.5, w2=0.5):
    """Score a word using strategy parameters"""
    score_letters = sum(letter_freq[l] for l in word)
    score_positions = sum(pos_freq[i][l] for i, l in enumerate(word))
    return w1 * score_letters + w2 * score_positions

def choose_best_word(word_list, letter_freq, pos_freq, w1=0.5, w2=0.5):
    """Return the word with the highest score according to strategy"""
    scored_words = [(word, score_word(word, letter_freq, pos_freq, w1, w2)) for word in word_list]
    scored_words.sort(key=lambda x: x[1], reverse=True)
    return scored_words[0][0]