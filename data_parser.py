#created by Frank Liu
#this class contains methods to edit all the bat files as required

spacing = "\t\t"
feelings = ['contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
dictionary = {'faceRectangle': {'height': 162, 'left': 130, 'top': 141, 'width': 162},
  'scores': {'anger': 9.29041e-06,
   'contempt': 0.000118981574,
   'disgust': 3.15619363e-05,
   'fear': 0.000589638,
   'happiness': 0.06630674,
   'neutral': 0.00555004273,
   'sadness': 7.44669524e-06,
   'surprise': 0.9273863}}

#helper function. Find the current picture number with the given file name
#code copied from https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def picture_num(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i - 1


def new_bat_file(ad_num):
    #sets up a new information file to use
    data_file = open("temp/ad" + str(ad_num) + ".txt", "w")

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

def add_to_bat_file(ad_num, json):
    #adds an image onto the bat file. params: ad_num and the json file returned from emotion api
    data_file_name = "temp/ad" + str(ad_num) + ".txt"
    pic_num = picture_num(data_file_name)
    data_file.open(data_file_name, "a") 
    s = str(pic_num) + spacing
    for i in dictionary['scores'].values():
        s += str(round(i * 100, 2)) + spacing
    data_file.write(s + "\n")
    data_file.close()
