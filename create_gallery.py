import uuid
import requests
import json
import base64

def get_upload_details(get_upload_details_url, get_upload_details_auth_token):

    header = {'Authorization': f'Bearer {get_upload_details_auth_token}'}
    response = requests.get(get_upload_details_url, headers=header)
    if response.status_code!=200:
        print(response)
        exit()

    response_content = json.loads(response.content.decode('utf-8'))
    upload_details = response_content['upload_details']

    return upload_details

def upload_gallery(gallery_path, upload_details):
    with open(gallery_path, 'rb') as f: # opens the zip file as binary
        files = {'file': (gallery_path, f)}
        upload_response = requests.post(upload_details['url'], data=upload_details['fields'], files=files)
    return upload_response

def main(gallery_path, get_upload_details_url, get_upload_details_auth_token):

    upload_details = get_upload_details(get_upload_details_url, get_upload_details_auth_token)
    print(f'[ INFO ] Upload Details: {upload_details}')
    upload_response = upload_gallery(gallery_path, upload_details)
    print(upload_response)

if __name__=='__main__':

    gallery_path = 'gallery.zip'
    get_upload_details_url = 'https://vgpdf3oowa.execute-api.sa-east-1.amazonaws.com/create-gallery'
    get_upload_details_auth_token = '' # add your token here

    main(
        gallery_path,
        get_upload_details_url,
        get_upload_details_auth_token
        )