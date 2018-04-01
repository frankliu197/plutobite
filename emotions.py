#created by Frank Liu
#gives you the emotions of the person in the given image
import requests  
def get_emotions(image):
    #gives the emotions of the person on the images
    #throws an exception if the image is faulty or if the internet sucks
    image_url = '' #maybe used for a future use
    params = {
        'returnFaceAttributes': 'emotion',
    }
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    
    headers  = {'Ocp-Apim-Subscription-Key': 'ceeccfc055fa4bcda459bc2a51fa16cd', "Content-Type": "application/octet-stream" }
    response = requests.post(face_api_url, params=params, headers=headers, data=open(image, "rb").read())
    response.raise_for_status()
    analysis = response.json()
    
    return analysis
