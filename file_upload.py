import requests
import os
 
def send_data_to_server(image_path):
    """
    It takes an image path as input, creates a multipart form data object, and sends it to the server
    
    :param image_path: The path to the image file
    """
         
    image_filename = os.path.basename(image_path)
 
    multipart_form_data = {
        'image': (image_filename, open(image_path, 'rb')),        
    }
 
    response = requests.post('http://www.example.com/api/v1/sensor_data/',
                             files=multipart_form_data)
 
    print(response.status_code)

