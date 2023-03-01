import requests

def main():

    image_path = 'demo_data.jpg'
    delete_image_from_gallery_api_url = 'https://q5hdkzogf2.execute-api.sa-east-1.amazonaws.com/delete-image-from-gallery'
    auth_token = ''

    data = {
        "filename": image_path
        }

    payload = {"Authorization": f"Bearer {auth_token}"}

    # send request
    response = requests.delete(delete_image_from_gallery_api_url, params=data, headers=payload)
    print(response)


if __name__=='__main__':
    main()

