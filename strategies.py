from collections import Counter

def letter_frequency(words):
    all_letters = ''.join(words)
    freq = Counter(all_letters)
    return freq

def position_frequency(words):
    position_freq = [Counter() for _ in range(5)]
    for word in words:
        for i, letter in enumerate(word):
            position_freq[i][letter] += 1
    return position_freq

def score_word(word, letter_freq, pos_freq, w1, w2):
    score_letters = sum(letter_freq[l] for l in word)
    score_positions = sum(pos_freq[i][l] for i, l in enumerate(word))
    return w1 * score_letters + w2 * score_positions

def choose_best_word(word_list, letter_freq, pos_freq, w1, w2):
    scored_words = [(word, score_word(word, letter_freq, pos_freq, w1, w2)) for word in word_list]
    scored_words.sort(key = lambda x: x[1], reverse = True)
    return scored_words[0][0]