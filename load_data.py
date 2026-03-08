with open("solution_words.csv") as f:
    solution_words = [line.strip() for line in f]

with open("allowed_words.csv") as f:
    allowed_words = [line.strip() for line in f]

print(f"Solution words: {len(solution_words)}")
print(f"Allowed words: {len(allowed_words)}")