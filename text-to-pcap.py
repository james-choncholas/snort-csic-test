import requests

# Provide path to your input file
# file_path = "./anomalousTrafficTest.txt"
# file_path = "./normalTrafficTest.txt"
file_path = "./normalTrafficTraining.txt"

# To run the requests against an echo server, use the command:
# docker run -p 8080:80 ealen/echo-server
#
# To capture a pcap of the traffic this generates, also run:
# sudo tcpdump -i lo -nn dst 127.0.0.1 and port 8080 -w test.pcap
#
# To test the pcap against snort, run:
# TODO

debug = False

with open(file_path, 'r') as file:
    lines = file.readlines()

line_i = 0
request_id = 0

def get_dummy_data(wanted_len):
    s = 'dummy_data'
    return (s * (wanted_len//len(s) + 1))[:wanted_len]

# For each request
while line_i < len(lines):
    # Parse the URL from the first line 
    get_or_post = lines[line_i].split(' ')[0]
    if get_or_post not in ['GET', 'POST']:
        line_i += 1
        continue

    url = lines[line_i].split(' ')[1]
    
    headers = {}
    while lines[line_i].strip() != '':
        key, value = lines[line_i].split(':', 1)
        headers[key.strip()] = value.strip()
        line_i += 1

    if debug:
        print(f"Request {request_id}:")
        print(f"Method: {get_or_post}")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print("")

    request_id += 1
    line_i += 2  # two empty lines between requests

    try:
        # Make the request
        if get_or_post == 'GET':
            response = requests.get(url, headers=headers)
        elif get_or_post == 'POST':
            dummy_data = get_dummy_data(int(headers['Content-Length']))
            response = requests.post(url, headers=headers, data=dummy_data)
    except Exception as e:
        print(f"Request {request_id} failed: {e}")
        continue
    
    # Print the response
    if debug:
        print('Response Code:', response.status_code)
        print('Response Headers:', response.headers)
        print('Response Body:', response.text)
        print('')
        print('')