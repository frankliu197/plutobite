#created by Frank Liu
#this class contains methods to edit all the bat files as required
from collections import OrderedDict
from graph_creator import feelings
import os, os.path

spacing = "\t\t"
def summary_data_file():
    #adds an image onto the bat file inside the dat file folder
    data_file = open("overall/overall.txt", "w")
    s = "#" + spacing
    for i in feelings:
        s += str(i) + spacing
    data_file.write(s + "\n")
    
    #need an empty line so the starting index is 0 not 1 in the graph
    s = "0" + spacing
    for i in feelings:
        s += str(0) + spacing
    data_file.write(s + "\n")
   
    files = os.listdir("data") 

    a = 0
    for i in files:
        a+= 1
        sample_file = open("data/" + i, "r")
        lines = sample_file.read().split("\n")
        s = str(a) + spacing
        for line_n in range(1, len(lines)):
            line = lines[line_n]
            number = line[line.rfind("\t") + 1:len(line)]
            s += spacing + str(number)
        sample_file.close()
        data_file.write(s + "\n")
        

def to_dictionary(json):
    #converts the json to an ordered dictionary
    return OrderedDict(sorted(json[0]['faceAttributes']['emotion'].items()))

def add_data_file(ad_num, dictionary):
    #adds an image onto the bat file. params: ad_num and the dictionary file returned from emotion api
    data_file = open("data/ad" + str(ad_num) + ".txt", "w")
    data_file.write("#" + spacing + "Value \n")
    for k, v in dictionary.items():
        data_file.write(k + spacing + str(round(v * 100, 2)) + "\n")
    data_file.close()
