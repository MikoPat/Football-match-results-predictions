# Predict football match result


### Idea
Use historical data, take into account form of the team in 


### Problem

Przewidzieć wyni


### Process:

Data was scrape from [FbRef](https://fbref.com/en/).

1. Get links to specific match from fixture list 
2. Get data from parciular match (specyfic values listed in file *Columns_from_FbRef.md* in *Doc* folder)

Then I added values that can indicate the level of the team. I chose values from [Elo Ranking](http://clubelo.com/) and added two columns:

- elo_home_team
- elo_away_team

I chose Elo Ranking because of the historical data and the value not only based on the result in the European competitions.

3. Based on match data, calculate last 5 matches and last 3 matches with opponent of similar level. 
4. Do this for all matches


### Results

1. Only Premier League
    All results were similar within 0.5 accuracy.
    The number of columns selected did not matter.
2. All matches from the top 5 leagues (\*without the first 10 matchweeks, because the data for the network is dirty)
    - selected columns - 0.5 accuracy
    - all columns - 0.55 accuracy

3. Data without pandemic season - not checked


### Conclusion



