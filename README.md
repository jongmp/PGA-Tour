# PGA-Tour
Machine Learning Project on the PGA Tour Data from 2010-2018

## Data set
The Dataset selected for this project contains data was scraped from the PGA Tour's official website. The code for data collection is included in the folder Data Scraping.

## Brief Description of the Data
pgaTourData.csv contains 1674 rows and 18 columns. Each row indicates a golfer's performance for that year.

Player Name: Name of the golfer
Rounds: The number of games that a player played
Fairway Percentage: The percentage of time a tee shot lands on the fairway
Year: The year in which the statistic was collected
Avg Distance: The average distance of the tee-shot
gir: (Green in Regulation) is met if any part of the ball is touching the putting surface while the number of strokes taken is at least two fewer than par
Average Putts: The average number of strokes taken on the green
Average Scrambling: Scrambling is when a player misses the green in regulation, but still makes par or better on a hole
Average Score: Average Score is the average of all the scores a player has played in that year
Points: The number of FedExCup points a player earned in that year. These points can be earned by competing in tournaments.
Wins: The number of competition a player has won in that year
Top 10: The number of competitions where a player has placed in the Top 10
Average SG Putts: Strokes gained: putting measures how many strokes a player gains (or loses) on the greens.
Average SG Total: The Off-the-tee + approach-the-green + around-the-green + putting statistics combined
SG:OTT: Strokes gained: off-the-tee measures player performance off the tee on all par-4s and par-5s.
SG:APR: Strokes gained: approach-the-green measures player performance on approach shots. Approach shots include all shots that are not from the tee on par-4 and par-5 holes and are not included in strokes gained: around-the-green and strokes gained: putting. Approach shots include tee shots on par-3s.
SG:ARG: Strokes gained: around-the-green measures player performance on any shot within 30 yards of the edge of the green. This statistic does not include any shots taken on the putting green.
Money: The amount of prize money a player has earned from tournaments
The official explanation for strokes gained is included here.

## Installation
To run the .ipynb file, you will need to first install [Python](https://www.python.org/), then install [Jupyter Notebook.](https://jupyter.readthedocs.io/en/latest/install.html) The instructions for the installation are provided in these links. For a local installation of Jupyter Notebook, make sure you have pip installed and run:
```bash
pip install notebook
```
## Usage - Running Jupyter notebook
Running in a local installation
Launch with:
```bash
jupyter notebook
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

