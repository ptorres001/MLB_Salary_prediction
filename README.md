# Linear_Regression_Model: Predicting Baseball Player's Salaries After Arbitration
### Mod 2 Project by Paul Torres

This repository contains data collection, cleaning and analyses of the salar, batting statistics, awards, and all-star selections of MLB players that started their rookie season after 2000. It includes all those that played until the end of the 2019 season. 


# Project

For this project, I aim to build a linear regression model that will be able to predict the salary of a players entering their fourth year. The goal being a model that could be used by either a player or an MLB team in order to have a moore favorable outcome in salary arbitration. I started off with a number of ideas about the performance features that would have the most correlation with salary and used that as a baseline to guide EDA. Since the game of baseball has changed tremendously over its history, only recent players were taken into consideration.

# Structure of Repository
- PNG -- contains images linked in README
- jupyternotebooks -- contains the project breakdown in chronological order
- README.md


# Approach
1. *Understanding the data*
	- What effect has the change in basebal strategy had on the types of players they value?
		1. **The change from long ball to money ball**:  
		> "Chicks may dig the long ball, but is relying on it to produce runs a viable strategy for teams with World Series aspirations."
		2. **Establishing a negotiation plan**:  
		Presenting a case to arbitration that could convince the panel to agree with arbitration offer.

# Data
Before we dive deeper into the questions, here is some information on our data. 
1. Only players whose rookie season occured on 2000 or later were included.
2. Data used in this repository is available SeanLahman.com. 
3. Players who did not play more than 3 seasons were excluded. 

# Process
With negotiations in mind, I explored the data and answered some of the questions below.

## Is there a difference by side of the plate?
Left handed batters vs Right Handed Batters

## Where did you play?
Does country of origin matter?

# Results
My latest models return varying RMSE values. 

The lowest being a score of $1.01 million. 

# Conclusion

The change in strategy in baseball led to a much smaller dataset. The RMSEs found in these models explain 44% of the variance in the salary. With a larger dataset and contract information the model could be viable. 
