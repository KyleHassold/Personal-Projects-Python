

import requests, re, json, time, random
requests.packages.urllib3.disable_warnings()

# Created by Alex Beals
# Last updated: February 20, 2016

base_url = "https://polldaddy.com/poll/"
redirect = ""

useragents = []
current_useragent = ""

proxies = []
current_proxy = {"http":""}
current_proxy_num = -1




def vote_once(form, value):
    c = requests.Session()
    #Chooses useragent randomly
    redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",  "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}



    # Search for the data-vote JSON object
    data = re.search("data-vote=\"(.*?)\"",init.text).group(1).replace('&quot;','"')
    data = json.loads(data)
    # Search for the hidden form value
    pz = re.search("type='hidden' name='pz' value='(.*?)'",init.text).group(1)
    # Build the GET url to vote
    request = "https://polldaddy.com/vote.php?va=" + str(data['at']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data['t']) + "&token=" + str(data['n']) + "&pz=" + str(pz)
    try:
        send = c.get(request, headers=redirect, verify=False)
    except:
        print "error with proxy"
        #proxies.remove(current_proxy_num)
        return None

    return ("revoted" in send.url)

def vote(form, value, times, wait_min = None, wait_max = None):
    global redirect
    # For each voting attempt
    i = 1
    while i < times+1:
        b = vote_once(form, value)
        # If successful, print that out, else try waiting for 60 seconds (rate limiting)
        if not b:
            # Randomize timing if set
            if wait_min and wait_max:
                seconds = random.randint(wait_min, wait_max)
            else:
                seconds = 3

            print "Voted (time number " + str(i) + ")!"
            time.sleep(seconds)
        else:
            print "Locked.  Sleeping for 60 seconds."
            i-=1
            time.sleep(60)
        i += 1

# Initialize these to the specific form and how often you want to vote
poll_id = 10295790
answer_id = 47371839
number_of_votes = 10
wait_min = 5
wait_max = 15


vote(poll_id, answer_id, number_of_votes, wait_min, wait_max)