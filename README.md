# weather-tools
All my code i use when tracking severe weather

I used chatGPT to assist me in creating these files

"velocity calc.py" is used to estimate the windspeeds of a tornado based off of measurements taken through tools in radaromega

"infolist.py" can be used to store the location and estimated windspeeds from a storm that you want to keep tabs on, the data is stored in a list which is displayed to the user. the thought behind this tool is that the user can log data from multiple storms in one place to better keep situational awareness when tracking storms. all the data in the list can be saved into a .txt file named "storm_data.txt"

"stormlist.html" is simply used to access the saved data from the current session. When the "infolist.py" application is closed, the data in "storm_data.txt" is automatically saved to "archive.txt"

"archive.txt" is the saved data from stormlist.html 
