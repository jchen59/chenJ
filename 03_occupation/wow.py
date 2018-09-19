from random import random

def make_dictionary(fname):
    f = open(fname) # Opens the file
    lines = f.read().strip('\n').split('\n') # Makes a list of all the lines
    dict = {}
    for name in lines[1:-1]:
        if name[0] == '"': # If there are quotations
            words = name.strip('"').split('"')
            words[1] = words[1].strip(',') # Gets rip of comma
        else: # If there are no quotations
            words = name.split(",")

        dict[words[0]] = words[1] # Matches job titles with percentage

    return dict

#Picks a random number out of 100
#Loops until total is above the random number and returns the values
def random_job(dict):
    q = random() * 100 # Random value 0 to 1 incl -> 0 to 100 incl
    current = 0
    for key in dict:
        current += float(dict[key])
        if current > q:
            return key + " with a " + dict[key] + "% chance"


d = make_dictionary("occupations.csv")

print(random_job(d))
