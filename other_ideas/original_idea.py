import requests
import cv2
import time

# Setup Eyepop tokens/API stuff

pop_endpoint = 'EyePop URL'
token = 'EyePop Token'
directory_path = 'Directory Path'

# get configuration information from pop

def fetch_pop_config(pop_endpoint, token):
    headers = {'Accept': 'application/json',
               'Authorization': f'Bearer {token}'}
    response = requests.get(pop_endpoint, headers=headers)
    return response.json() if response.status_code == 200 else {"error": "Something went wrong!"}

config = fetch_pop_config(pop_endpoint, token)

# get json from a given file path

def get_json_from_eye_pop_upload(config, token, file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}

        target_url = f"{config['url']}/pipelines/{config['pipeline_id']}/source?mode=preempt&processing=sync"
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        try:
            response = requests.post(target_url, headers=headers, files=files)
            response.raise_for_status()

            j = response.json()
            return j
        except requests.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
        except Exception as err:
            print(f"Error: {err}")

# process result data for important information

def get_index_of_biggest_person(objects):
    people = []

    for i in range(len(objects)):
        if objects[i]['classLabel'] == 'person':
            people.append(i)

    biggest_person = -1
    biggest_height = -1

    for i in people:
        if objects[i]['height'] > biggest_height:
            biggest_height = objects[i]['height']
            biggest_person = i
    
    if biggest_person != -1:
        return biggest_person
    else:
        return -1
    

def process_results(result):
    objects = result[0]['objects']

    print(objects)

    index_of_biggest_person = get_index_of_biggest_person(objects)

    if index_of_biggest_person != -1:
        if 'keyPoints' in objects[index_of_biggest_person]:
            key_points = objects[index_of_biggest_person]['keyPoints'][0]['points']

            body_parts_and_location = {}

            for key_point in key_points:
                body_parts_and_location[key_point['classLabel']] = [key_point['x'], key_point['y']]
            
            return body_parts_and_location
        else:
            print('No key body parts detected')
            return 
    else:
        print('No people found :(')
        return

# compare previous with current to detect fall

def compare_results(previous, current):
    common_keys = list(set(previous).intersection(set(current)))
    
    y_differences = [current[key][0] - previous[key][0] for key in common_keys]

    print(y_differences)

# set up video feed

cap = cv2.VideoCapture(1)

prev = {}

while True:
    ret, frame = cap.read()
    
    if not ret:
        print('Failed to capture a photo')
        break

    cv2.imshow("Video Frame", frame)
    image_file_name = 'captured_photo.jpg'
    cv2.imwrite(image_file_name, frame)
    image_file_path = directory_path + image_file_name

    result = get_json_from_eye_pop_upload(config, token, image_file_path)

    if result:
        if 'objects' in result[0]:
            processed = process_results(result)
            if processed:
                print(processed)

                if len(prev):
                    compare_results(prev, processed)

                prev = processed
        else:
            print('Your cam probably is not working')
            print(result)
    
    time.sleep(10)


cap.release()
cv2.destroyAllWindows()
