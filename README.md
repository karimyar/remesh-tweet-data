# remesh-tweet-data
Remesh Data Visualization project for Ali Karimyar

I created a video demonstration that walks through the project (how to start, execute program, etc.) along with commentary regarding the various analytical insights I discovered. 
Here's a link to the video: https://www.youtube.com/watch?v=aWmBAzEV5sE 

In case any directions are unclear or something goes awry, please refer to the first 1-2 minutes of the video which may clarify how to run the program or provide potential trouble-shooting tips. 

This project is based off Python3 and can be run through the terminal (or any command line prompt). Make sure the json file (i.e. Twitter data) is in the same directory as the actual python file. The Python file utilizes certain libraries such as json, pandas, plotly and dash, so please be sure to have installed those dependencies beforehand (see below for commands to install each).

To run the program, open the terminal (or command line prompt) and navigate to the folder where both the json data file and python project file are hosted. In my case I put these files on my desktop so it's easier to navigate to/from. Make sure to install the various required Python libraries/dependencies within this folder (see below). 

After you've navigated to the necessary folder in the terminal (where json & python file is housed), type "python3 project.py" in command line and the program should attempt to execute. 

If it is succesfull you will see a prompt pop up underneath the previous command saying: "Dash is running on http://127.0.0.1:8050/"

This URL is a localhost where the actual Python-based interactive data visuailzation is occuring. I am using the Dash library, which allows for creating reactive/interactive web-based visualziations and applications through Python. The actual URL provided may not be the same as what I copied-pasted above, but whatever is outputted will be the URL you will copy and paste to your browser. 

After, it should take you to a local webpage that actually displays the various data visualizations created in Python. There should be two interactive plots, both have range sliders which allow you to interact with the plot and see changes happening in real-time. You can interact the the plots and see the various points along with their respective data. 

In regards to audience engagment, I classified and defined this as the number of likes a tweet has. If a particular tweet has a lot of likes (>100) it is more engaging than tweets with less likes (<50). In general, Twitter users more often like tweets than retweet because it's easier to do, is less intrusive to others (i.e more intimate), and doesn't clog/spam the Twitter feed. 

Furtermore, taking a look at the top 30 most liked and retweeted tweets on Wikipedia (https://en.wikipedia.org/wiki/List_of_most-liked_tweets, https://en.wikipedia.org/wiki/List_of_most-retweeted_tweets) we can clearly see that the top tweets have more likes than retweets, meaning more people engage in liking tweets than retweeting.   

## Installation commands:

pip install json 

pip install pandas

pip install plotly

pip install dash
