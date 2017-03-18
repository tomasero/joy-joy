import requests
import datetime
import time
import config

def send_command(user_id, command, token, endpoint):
    data = {
    	'user_id': user_id,
        'token': token,
        'command': command,
        'timestamp': time.time()
    }
    r = requests.post(endpoint, json=data)
    return r.text


def make_pocorn():
	user_id = 1
	command = "popcorn"
	return send_command(1, command, config.token, config.endpoint)


def main():
	print(make_pocorn())


if __name__ == "__main__":
    main()