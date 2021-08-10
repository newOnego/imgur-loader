import string, random, requests

def generateName(length):
	name = ""
	for i in range(length):
		name += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
	return name

def downloadMedia(length):
	name = generateName(length)
	response = requests.get("https://i.imgur.com/" + name + ".jpeg", allow_redirects = False)
	if response.status_code != 302:
		with open(name + "." + response.headers["content-type"].split("/")[1], "wb") as f:
			f.write(response.content)
			f.close()

while True:
	downloadMedia(5)