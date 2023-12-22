# Predict football match result


### Idea
Use historical data, taking into account the team's form in the last 5 games and the last 3 games against opponents of a similar level to the current team.


### Problem

Football is a complex sport. The final result of a match depends on many aspects. There are 22 players on the pitch, all of whom are independent (they can make their own decisions).
The number of goals scored in a match is small, unlike basketball where two teams can score more than 100 points each. It is necessary to take into account other aspects such as the quality of the grass, the weather conditions, the well-being of the players.


### Process:

Data was scrape from [FbRef](https://fbref.com/en/).

1. Get links to specific matches from the fixture list 
2. Get data from specific match (specific values listed in file *Columns_from_FbRef.md* in *Doc* folder)

Then I added values that could indicate the level of the team. I chose values from [Elo Ranking](http://clubelo.com/) and added two columns:

- elo_home_team
- elo_away_team

I chose Elo Ranking because of the historical data and because the value is not only based on the result in the European competitions.

3. Based on the match data, calculate the last 5 matches and the last 3 matches against opponents of similar level. 
4. Do this for all matches. As a result for the neural network was the result of the home team in a particular match (win - 3, draw - 1, loss - 0).
5. Prepared data used in neural network in class. Before final processing of data - in result column values *3* were changed for *2*.


### Results

1. Premier League only
    All results were within 0.5 of each other.
    The number of columns selected made no difference.
2. All matches from the top 5 leagues (\*without the first 10 matchweeks, because the data for the network is dirty)
    - selected columns - 0.5 accuracy
    - all columns - 0.55 accuracy
3. Data without pandemic season - unchecked

The neural network code is in the *neuralNetwork.ipynb* file in the *Code* folder.


### Conclusion

The results are not satisfactory: only 50% of the predictions are correct. Future work:
1. Get more historical data
2. Change the number of matches calculated in the preparation process.

