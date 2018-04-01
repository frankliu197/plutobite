#created by Frank Liu
#this class will tie all the methods together
from emotions import get_emotions
from data_parser import to_dictionary, add_data_file, summary_data_file
from graph_creator import get_graph
import capture
#return_value = get_emotions('face.jpg')
ad_num = 0

def get_emotions_graph(image):
    #returns an the location of the graph made for the given ads
    add_data_file(ad_num, to_dictionary(get_emotions(image)))
    return get_graph(ad_num)

def get_overall_graph():
    summary_data_file()
    return get_graph()

def next_ad_number():
    #helper method
    global ad_num
    ad_num += 1
    return ad_num

def capture_image():
    #returns the image location that is captured
    return capture.capture(next_ad_number())

capture_image()
