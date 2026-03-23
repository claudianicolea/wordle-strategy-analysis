Math AA HL Internal Assessment
Wordle Strategy Analysis

This project simulates Wordle games to explore the optimal strategy for minimizing the number of guesses.
It uses a calculus-based continuous model to approximate the reduction of possible words over time.

Files

1. load_data.py
   - Loads Wordle solution words and allowed guess words from CSV files
   - Prints the number of words loaded

2. strategies.py
   - Defines strategies for choosing words
   - Calculates word scores based on letter frequency and position frequency
   - Includes strategy weights, which can be adjusted

3. simulate_wordle.py
   - Runs discrete simulations of Wordle games
   - Loops over solution words and applies chosen strategy
   - Records number of guesses needed to solve each game
   - Calculates the average number of guesses for multiple simulations
   - You can adjust strategy parameters w1 (letter frequency weight) and w2 (position weight)

4. euler_method.py
   - Implements Euler's method to simulate continuous reduction of solution space
   - Models rate of change of remaining words with a differential equation
   - Plots fraction of solution space remaining versus guesses

5. plot_surface.py
   - Graphs the solution space of the problem as 3D
   - Points to the global minimum
   - Thus finds the best strategy to minimize the number of guesses in the game

Data
(1 word per row)
- solution_words.csv : contains the list of Wordle solution words
- allowed_words.csv  : contains the full Wordle dictionary of allowed guesses

Requirements
- Python 3.x
- pandas
- numpy
- matplotlib

How to Run
1. Place solution_words.csv and allowed_words.csv in the same folder as the scripts
2. Run load_data.py to check data loading
3. Run simulate_wordle.py to simulate games and calculate average guesses
4. Run euler_method.py to see the continuous approximation plot
5. Adjust strategy parameters w1 and w2 in simulate_wordle.py to test different strategies
6. Run plot_surface.py to graph the solution space and find the best strategies for the least amount of guesses to win

Notes
- w1 = weight for letter frequency in scoring
- w2 = weight for letter position frequency in scoring
- Euler method is used to approximate the rate of reduction of possible solutions continuously
- You can run multiple simulations to optimize the strategy used in the game