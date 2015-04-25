# NBA-Playoff-Predictor
Uses regular season records and current series results to predict the likely outcome of a playoff series

When you run the program, it will ask you to input the number of wins each team had in the regular season (assumes an 82-game NBA season). I prefer to use Pythagorean wins from basketball-reference.com.

The program next asks for the number of wins each team has in the series so far. After this, it will simulate the series 100,000 times, using a random number generator and the log5 model to determine the winner of each simulated game.

The program will print the probability that Team A wins the series in 4, 5, 6, or 7 games, plus the probability that Team A is eliminated. If you care more about Team B's outcomes, simply reverse the labels when you run the program again.
