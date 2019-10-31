import json
import urllib.request

group_ids = [25152, 20, 21, 22, 23, 24, 25151, 25150]

linkFirstHalf = "http://augur.osshealth.io:5000/api/unstable/repo-groups/"
linkSecondHalf = "/top-committers"


for i in range(len(group_ids)):
    with urllib.request.urlopen(linkFirstHalf+str(group_ids[i])+linkSecondHalf) as url:
        data = json.loads(url.read().decode("utf-8"))
        print (json.dumps(data, indent=4, sort_keys=True))

