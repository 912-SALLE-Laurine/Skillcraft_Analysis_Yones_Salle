# Skillcraft Dataset Analysis 
*Yones Maélis and Sallé Laurine*

Hello ! We are tow students at ESILV, in our 4th year of engineering studies. <br>
As a final project of the Python for Data Analysis course, we are glad to present you our analysis of the dataset SkillCraft1 created by Mark Blair, Joe Thompson, Andrew Henrey and Bill Chen on September 20 of 2013. (link of our dataset : https://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset#)  <br>
SkillCraft1 is a game dataset with 20 attributes and 3395 instances of players from the game StarCraft 2.<br>
StarCraft II  is a science fiction real-time strategy video game developed and published by Blizzard Entertainment. It is a multiplayer game where several players compete in an arena to collect resources, capture strategic points and destroy opposing bases.
![Starcraft2-logo](https://user-images.githubusercontent.com/72121488/148266957-63e4b78a-d9fe-4993-9586-c7579adeb642.jpg)
In the game, players have a League, which is a ranking system based on the performances and the number of victories in competitions. 
There are 8 Leagues : 

League Index | Name Rank 
--- | ---
8| Professional
7|Grandmaster
6|Master
5|Diamond
4 |Platinum 
3 | Gold
2 | Silver 
1 | Bronze 

Our goal is to analyse the dataset, more particularly the meaning variables in order to predict the league index of a given player players. <br>
We are in a classification problem.

### Our analysis is composed of different parts :

    Dataset cleaning : Observe the variabe types, find if there is irrelevant datas, and try to correct this. 
    Data analysis: Show the correlations between the variables, show links between variables and target
    Machine learning : Predict the output, by trying different models, searching for the best approach, and the best parameters.  
    API Flask : Transform the model into a Flask API

To summarize our results:

### Data analysis : 
In this part, we identified the variables wich explains the most the output. 
<b>Variables positively correlated with LeagueIndex:</b> APM, SelectByHotkeys, AssignToHotkeys, NumberOfPACs
<b>Variables negatively correlated with LeagueIndex:</b> GapBetweenPACs, ActionLatency
We can therefore anticipate the profile of a good player with a low latency, quick reaction, a big number of action, etc. <br>

### Machine Learning : 
We tried a lot of models in order to do our prediction. 
We performed 2 types of predictions with our dataset: 
- The fist one, is the prediction of the LeagueIndex (8 possible output, from Bronze to Professional), but we observed that the prediction accuracy is very low : 0.40 is the maximum we obtained, with Gradient Boosting Classifier. <br>
- Then, we grouped the LeagueIndex to create 3 levels (beginner, intermediate, advanced), so instead of having 8 outputs, there is only 3 output to predict. With the best model, Gradient Boosting Classifier, the accuracy we obtained is around 0.80, so it is much better than the previous prediction.

### API Flask : 
We implementend the best model in our Flask application. You can fill the form with the player's parameters, and it will return a prediction of the League avec the Level of the player.
To be able to run the api: download the "!!!!!!!!!!!!" folder, open your Anaconda Prompt (or any python supported cmd ) and go to the !!!!!! folder (cd .\!!!!!) then enter python app.py , and copy the localhost link (like http://127.0.0.1:8000/) in your browser.
