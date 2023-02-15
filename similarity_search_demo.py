import uuid
import requests
import json
import os
import base64

def encode_image_base64(image_path):
    """
    Encodes an image into base 64
    """
    with open(image_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    return data

def main(image_path, process_request_url, process_request_auth_token, get_results_url, get_results_auth_token):

    # -- Use Process Request API to start the processing -- #
    encoded_image = encode_image_base64(image_path) # encode image to base64
    request_uuid = str(uuid.uuid4()) # generate request uuid
    print(f"[ INFO ] Request UUID: {request_uuid}")

    data = {
        "encoded_image": encoded_image.decode("utf-8"),
        "request_uuid": request_uuid
        }

    post_payload = {"Authorization": f"Bearer {process_request_auth_token}"}
    # send process request
    response = requests.post(process_request_url, json=data, headers=post_payload)
    print(response)

    # -- Use Get Results API to retrieve the results -- #
    get_payload = {"Authorization": f"Bearer {get_results_auth_token}"}
    response = requests.get(f'{get_results_url}?request_uuid={request_uuid}', headers=get_payload)
    results = json.loads(response.content)
    print(results)

if __name__=='__main__':

    image_path = 'demo_data.jpg'

    process_request_url = 'https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/process_request'
    process_request_auth_token = '' # add your token here
    get_results_url = 'https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/get_results'
    get_results_auth_token = '' # add your token here

    main(
        image_path,
        process_request_url,
        process_request_auth_token,
        get_results_url,
        get_results_auth_token
        )