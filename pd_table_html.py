# Python program to convert  
# CSV to HTML Table 
  
import pandas as pd 
  
# to read csv file named "samplee" 
#
weather = pd.read_csv("cities.csv") 
  
# to save as html file 
# named as "Table" 

weather.to_html("Tables.htm") 
  
# assign it to a  
# variable (string) 

html_file = weather.to_html() 