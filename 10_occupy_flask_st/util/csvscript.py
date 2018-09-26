#Ji-N-Ja -- Jiayang Chen & Jabir Chowdhury + Peter Cwalina(from last work)
#SoftDev1 pd7
#K10: Jinja Tuning
#2018-09-23

from random import random

def make_dictionary(fname):
    f = open(fname) # Opens the file
    lines = f.read().strip('\n').split('\n') # Makes a list of all the lines
    f.close()
    dict = {}
    for name in lines[1:-1]:
        if name[0] == '"': # If there are quotations
            words = name.strip('"').split('"')
            temp = words[1].strip(',').split(',') #a list with percentage and URL
            dict[words[0]] = tuple(temp) #Converts list to a tuple and matches it with the key
        else: # If there are no quotations
            words = name.split(",")
            dict[words[0]] = (words[1], words[2]) # Matches job titles with a tuple containing percentage and URL

    return dict


#Picks a random number out of 100
#Loops until total is above the random number and returns the values
def random_job(dict):
    q = random() * 99.8 # Random value 0 to 1 incl -> 0 to 99.8 incl
    current = 0
    for key in dict:
        current += float(dict[key][0])
        if current > q:
            return key + " with a " + dict[key][0] + "% chance"
