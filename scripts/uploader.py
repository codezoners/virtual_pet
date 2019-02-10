# Call a JSON endpoint with current date and time.

import requests
import time

now = time.time()

root = "https://cryptic-bastion-90714.herokuapp.com"
#root = ""http://localhost:5000"

r = requests.post("{root}/add_data".format(root=root),
                  json={'time': now,
                        'value': 1.0})

if r.status_code == requests.codes.ok:
    data = r.json()
    print("Data OK: ", data)
else:
    print("error fetching, status is ", r.status_code)
