# remesh-tweet-data
Remesh Data Visualization project for Ali Karimyar

I created a video demonstration that walks through the project (how to start, execute program, etc.) along with commentary regarding the various analytical insights I discovered. 
Here's a link to the video: https://www.youtube.com/watch?v=aWmBAzEV5sE 

In case any directions are unclear or something goes awry, please refer to the first 1-2 minutes of the video which may clarify how to run the program or provide potential trouble-shooting tips.  

This project is based of off Python3 and can be run through the terminal (or any command line prompt). Make sure the json file (i.e. Twitter data) is in the same directory as the actual python file. 

The Python file utilizes certain libraries such as json, pandas, plotly and dash, so please be sure to have installed those dependencies beforehand (see below for commands to install each).

To run the program, open the terminal (or command line prompt) and navigate to the folder where the json data file and python project file are hosted. I put these files in the desktop folder so it's easier to navigate to/from. Make sure to install the various required Python libraries/dependencies within this folder (see below for). After you've navigated to the necessary folder in the terminal (where json & python file is housed), type "python3 project.py" in command line and the program should attempt to execute. 

If it is succesfull you will see a prompt pop up underneath the previous command saying: "Dash is running on http://127.0.0.1:8050/" 

Tthis URL is a localhost where the actual Python-based interactive data visuailzation is occuring. I am using the Dash library, which allows for creating reactive/interactive web-based visualziations and applications through Python. The actual URL provided may not be the same as what I copied-pasted above, but whatever is outputted will be the URL you will copy and paste to your browser. 

After, it should take you to a local webpage that actually displays the various data visualizations created in Python. There should be two interactive plots, both have range sliders which allow you to interact with the plot and see changes happening in real-time. 


## Installation commands:

pip install json 

pip install pandas

pip install plotly

pip install dash
