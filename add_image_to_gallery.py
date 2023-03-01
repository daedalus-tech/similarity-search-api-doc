import requests
import argparse
import base64

def encode_image_base64(image_path):
    """
    Encodes an image into base 64
    """
    with open(image_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    return data

def main():

    image_path = 'demo_data.jpg'
    add_image_to_gallery_api_url = 'https://q5hdkzogf2.execute-api.sa-east-1.amazonaws.com/add-image-to-gallery'
    auth_token = '' # add your token here

    post_payload = {"Authorization": f"Bearer {auth_token}"}

    # encode image into base64
    encoded_image = encode_image_base64(image_path)

    data = {
        "encoded_image": encoded_image.decode("utf-8"),
        "image_filename": image_path
        }

    # send request
    response = requests.post(add_image_to_gallery_api_url, json=data, headers=post_payload)
    print(response)

if __name__=='__main__':
    main()
