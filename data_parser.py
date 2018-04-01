#created by Frank Liu
#this class contains methods to edit all the bat files as required
from collections import OrderedDict

spacing = "\t\t"
def summary_data_file(ad_num):
    #adds an image onto the bat file inside the dat file folder
    data_file = open("overall/ad" + str(ad_num) + ".txt", "w")

    s = "#" + spacing
    for i in feelings:
        s += str(i) + spacing
    data_file.write(s + "\n")

    #need an empty line so the starting index is 0 not 1 in the graph
    s = "0" + spacing
    for i in feelings:
        s += str(0) + spacing
    data_file.write(s + "\n")
    data_file.close()

    data_file_name = "data/ad" + str(ad_num) + ".txt"
    s = str(pic_num) + spacing
    for i in dictionary['scores'].values():
        s += str(round(i * 100, 2)) + spacing
    data_file.write(s + "\n")


def to_dictionary(json):
    #converts the json to an ordered dictionary
    return OrderedDict(sorted(json[0]['faceAttributes']['emotion'].items()))

def add_data_file(ad_num, dictionary):
    #adds an image onto the bat file. params: ad_num and the dictionary file returned from emotion api
    data_file = open("data/ad" + str(ad_num) + ".txt", "w")
    data_file.write("#" + spacing + "Value")
    i = 0
    for k, v in dictionary.items():
        i+= 1
        data_file.write(str(i) + spacing + k + spacing + str(round(v * 100, 2)) + "\n")
    data_file.close()
