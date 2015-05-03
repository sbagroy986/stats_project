#parses the data collected from users
# import urllib
# req = urllib.urlopen('http://stats-project.herokuapp.com/statistics/view')
# print req.read()
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
r = requests.get('http://stats-project.herokuapp.com/statistics/view')
html = r.content
soup = BeautifulSoup(html)
table = soup.find("table", {"class": "table table-condensed table-hover"})
users = table.find_all("tr")
incGenre = [0, 0, 0]
decGenre = [0, 0, 0]
score = {"love":5, "like":4, "neutral":3, "dislike":2, "hate":1, "":0}
for user in users[1:]:
	responses = user.find_all("th")
	print str(responses[1].get_text()).split('/')
	if score[str(responses[1].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[1].get_text()).replace(" ","").split('/')[1]]: incGenre[0] += 1
	else: decGenre[0] += 1

	if score[str(responses[2].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[2].get_text()).replace(" ","").split('/')[1]]: incGenre[1] += 1
	else: decGenre[1] += 1

	if score[str(responses[2].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[2].get_text()).replace(" ","").split('/')[1]]: incGenre[2] += 1
	else: decGenre[2] += 1

ax = plt.subplot(111)
ax.bar([0, 1, 2], incGenre, width = 0.2, color = 'b', align = 'center')
ax.bar([0.2, 1.2, 2.2], decGenre, width = 0.2, color = 'r', align = 'center')
plt.xlabel("Genres[increasing trend, decreasing trend]")
plt.ylabel("Number Of Users")
plt.savefig("Plot1")
plt.clf()