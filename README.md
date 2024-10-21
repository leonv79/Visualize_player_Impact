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

To begin with it seems important to have a guy that spaces the floor and George does that. Almost all of the team's main shooters seem to have easier looks from the 3pt line. 

![image](https://github.com/user-attachments/assets/c05410ba-d9bb-484c-b2ea-0b252fabdbea)


Speaking of the 3pt line, here is everyone 3pt% with PG on and off. It is pretty evident that he plays a crucial role. Especially average shooters like Mann can really have a greater impact and will have to adjust a lot this season. Most notable one though: Norman Powell. Powell shoots a crazy 52%(!!!) with George in, while he hits 36% of his 3s when out. (Probably shouldn't throw jabs like the one he did in the offseason)

![image](https://github.com/user-attachments/assets/70b086f3-e02c-4309-afe9-4ca7fd80e18b)


Same pattern in the arc 3s

![image](https://github.com/user-attachments/assets/43b86a42-aa9a-45c3-ad31-d5a6dc09ffb5)

One cool stat (I have no clue how it is measured), is Shot Quality Average. Almost everyone, except for Theis, seem to take better shots and especially Harden and Powell. 

![image](https://github.com/user-attachments/assets/f0d51f65-671d-48ef-b638-37846a8882e9)


Side from shooting ball movement is a part that George can help a team with. 

More specifically watch the % of assisted Points at the rim, when he is on. Harden and Leonard especially will have to fill that role up a lot more this season, cuz without George they seem to play a lot more one on one (can't blame them though they are really good at it). 

![image](https://github.com/user-attachments/assets/bfee88c9-b52c-46c9-9aa5-ec79e7ac8490)

In a more general note Assisted 2s and 3s % are higher with George in highlighting his role in ball movement. Looking at the 3s of Kawhi there is a staggering difference(74% when in vs 45% when PG is out). 

![image](https://github.com/user-attachments/assets/b6dadeae-7058-4828-aa10-1fc9a0c95b62)

![image](https://github.com/user-attachments/assets/cebdd239-052a-460a-a7ce-f08d496aa055)

All in all the above are some of the most impactful categories that PG affects. We highlighted his importance on shooting and ball movement. Of course this project is on the beginnings and can offer insights up to a point. For example I couldn't highlight his Defensive excellence and there are also more aspects in his offensive game that can be studied. 

Nevertheless, this little tool can offer valuable information and can give a different perspective on how a player affects the others around him. In the case of Paul George, his loss will be visible in LA, and players like Derrick Jones Jr. have some really big shoes to fill (he won't, but he has to try to do at least something).

If you actually read all that thanks for the attention. I will probably do some studying on more players as the season goes on. 
