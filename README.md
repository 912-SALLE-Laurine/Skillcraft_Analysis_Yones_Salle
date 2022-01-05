# Skillcraft_Analysis_Yones_Salle

Hello ! We are tow students at ESILV, in our 4th year of engineering studies. 
As a final project of the Python for Data Analysis course, we are glad to present you our analysis of the dataset SkillCraft1 created by Mark Blair, Joe Thompson, Andrew Henrey and Bill Chen on September 20 of 2013. <br>
SkillCraft1 is a game dataset with 20 attributes and 3395 instances of players from the game StarCraft 2.<br>
StarCraft II  is a science fiction real-time strategy video game developed and published by Blizzard Entertainment. It is a multiplayer game where several players compete in an arena to collect resources, capture strategic points and destroy opposing bases.
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

Our goal is to analyse the dataset more particularly the meaning variables in order to predict the league index of a given player players. <br>
We are in a classification problem.

Here is the link of our dataset: https://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset#
Our analysis is composed of different parts : 

    Dataset cleaning : Observe the variabe types, find if there is irrelevant datas, and try to correct this. 
    Data analysis: Show the correlations between the variables, show links between variables and target
    Machine learning : Predict the output, by trying different models, searching for the best approach, and the best parameters.  
    API Flask : Transform the model into a Flask API

To quickly summarize our results (more details can be found in the notebook and the PowerPoint):

For the presentation part : We implementend the best model in our Flask application, in the form of a form to fill out. 
To be able to run the api: download the "!!!!!!!!!!!!" folder, open your Anaconda Prompt (or any python supported cmd ) and go to the !!!!!! folder (cd .\!!!!!) then enter python app.py , and copy the localhost link (like http://127.0.0.1:8000/) in your browser.
