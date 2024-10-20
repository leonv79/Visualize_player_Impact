# Visualize_player_Impact
Use Statistics methods to identify the most impactful categories in the PBP stats library

Most notably we use a non parametric method, and the on off stats of the PBP library to identify which categories a player affects the most. 

A small example to give a better understanding:
![image](https://github.com/user-attachments/assets/76958741-9f9f-4ee1-a044-10a3e3b38329)

Those are the Turnovers per 100 Possesions for the Clippers when Paul George was in vs when he is out. So I tried to find the most categories that PG impacts (statistically) significantly.

#########################
Small but really big note: All this wouldn't have been possible without the FANTASTIC work that has been done on the PBP library, with such a large number of categories that motivated me to use my field to identify the most important ones. (My only note to them was if I could have a glossary because some of these categories seem so specific that I cannot understand what they represent.)
#########################


###########################
Some background on the tecnhical part

The PBP library contains a plethora of categories. My thinking was to use hypothesis testing to figure out the most statistically significant ones. 

To do that I had to check normality, which with such a small sample was really naive of me to assume, and then i used the Wilcoxon method to measure the important categories.

The confidence level also was a bit of trouble. For the really impactful players 95% was adequent to give a good picture (like PG and LBJ), but for others i had to increase that to 90%(like Klay Thompson). In this case i risked some error to gain more insight. 

All graphs are done through plotly.

##########################

In this project, I wanted to check for the 2023-24 season the individual impact a player has on others. 

The reason for this was to see which of the main free-agent moves really impacted their teams, and how can they help their new teams.

My first target for this project was Paul Geogre move to Philly. Main target there was to see what Clippers are losing. 

And to no one's surprise PG's impact is huge. 



