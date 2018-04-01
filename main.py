#created by Frank Liu
#this class will tie all the methods together
from emotions import get_emotions
from data_parser import to_dictionary, add_to_bat_file, new_bat_file, feelings
from graph_creator import get_graph
#return_value = get_emotions('face.jpg')

return_value = [{'faceRectangle': {'top': 128, 'height': 207, 'width': 207, 'left': 57}, 'faceId': 'a45ca2ab-f64b-4018-8351-b835b72e0ca1', 'faceAttributes': {'emotion': {'disgust': 0.0, 'sadness': 0.0, 'happiness': 0.0, 'contempt': 0.0, 'anger': 0.0, 'fear': 0.0, 'neutral': 1.0, 'surprise': 0.0}}}]
to_dictionary(return_value)


