import string, random, requests
from database import *
initDB()

def generateName(length):
	name = ""
	for i in range(length):
		name += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
	return name

def downloadMedia(length):
	name = generateName(length)
	if checkLink(link = name) == None:
		response = requests.get("https://i.imgur.com/" + name + ".jpeg", allow_redirects = False)
		if response.status_code != 302:
			fileType = response.headers["content-type"].split("/")[1]
			addLink(link = name, length = length, condition = True)
			with open(name + "." + fileType, "wb") as f:
				f.write(response.content)
				f.close()
		else:
			addLink(link = name, length = length, condition = False)

while True:
	downloadMedia(5)