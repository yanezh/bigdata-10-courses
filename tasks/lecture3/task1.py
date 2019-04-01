from urllib.request import urlopen, urlretrieve
import json

url = "https://api.github.com/repos/python/cpython"

with urlopen(url) as page:
	content = page.read()
	json_content = json.loads(content)
	image_url = json_content['owner']['avatar_url']
	urlretrieve(image_url, 'avatar.jpg')
	print("done")