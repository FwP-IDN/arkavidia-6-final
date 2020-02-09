import sys
import requests

BASE_PORT = 0
HOST = 'arkav.host'
PORT = BASE_PORT + int(sys.argv[1])


import requests



def submit_flag(flag):
	headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '_jpAwZkBwMndWRrAd4IMH4pE8n7qO7WfFTuM9OAYQlK92lsTFs63HQ',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://172.31.1.1',
    'Referer': 'http://172.31.1.1/attack/submit',
    'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
	}

	data = json.dumps({"flag":flag})

	response = requests.post('http://172.31.1.1/api/flag/submit', headers=headers, data=data, verify=False)


print 'Attacking', HOST, PORT
