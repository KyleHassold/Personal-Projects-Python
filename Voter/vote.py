import requests, re, json, time, random

# Created by Alex Beals
# Last updated: January 29th, 2016

base_url = 'https://polldaddy.com/poll/'
redirect = ""

def vote_once(form, value):
	c = requests.Session()
	init = c.get(base_url + str(form) + "/", headers=redirect, verify=False)
	# Search for the data-vote JSON object
	data = re.search("data-vote=\"(.*?)\"",init.text).group(1).replace('&quot;','"')
	data = json.loads(data)
	# Search for the hidden form value
	pz = re.search("type='hidden' name='pz' value='(.*?)'",init.text).group(1)
	# Build the GET url to vote
	request = "https://polldaddy.com/vote.php?va=" + str(data['at']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data['t']) + "&token=" + str(data['n']) + "&pz=" + str(pz)
	send = c.get(request, headers=redirect, verify=False)
	return ('revoted' in send.url)

def vote(form, value, times, canadate, isRand):
	global redirect
	redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36", "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}
	# For each voting attempt
	for i in xrange(1,times+1):
		b = vote_once(form, value)
		# If successful, print that out, else try waiting for 60 seconds (rate limiting)
		if not b:
			print "Voted " + canadate + "(" + str(i) + ")"
			if (isRand == False):
				time.sleep(3)
			elif (isRand):
				time.sleep(random.randrange(1,10))
		else:
			print "Locked.  Sleeping for 60 seconds."
			i-=1
			time.sleep(60)

# Initialize these to the specific form and how often you want to vote
poll_id = 10295790
subject_id = 47371839
canadate = "Gianna Cascio"

number_of_votes = input("Enter number of votes: ")

rand = None
isRand = raw_input("Random time gaps (yes/no): ")
if (isRand == "yes" or isRand == "y"):
	rand = True
elif (isRand == "no" or isRand == "n"):
	rand = False
print rand

vote(poll_id, subject_id, number_of_votes, canadate, rand)

#var PDV_nurl10295790 = "https://polldaddy.com/n/" + (typeof PDV_h10295790 !== "undefined" ? PDV_h10295790 : PDV_id10295790) + "/10295790" + (PDV_w10295790 != PDV_id10295790 ? "/" + PDV_w10295790 : "");