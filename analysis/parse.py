import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
r = requests.get('http://stats-project.herokuapp.com/statistics/view')
html = r.content
open('htmlDump', 'w').write(html)
html = open('htmlDump', 'r').read()
soup = BeautifulSoup(html)
table = soup.find("table", {"class": "table table-condensed table-hover"})
users = table.find_all("tr")
incGenre = [0, 0, 0]
decGenre = [0, 0, 0]
score = {"love":5, "like":4, "neutral":3, "dislike":2, "hate":1, "":1}
for user in users[1:]:
	responses = user.find_all("th")
	if score[str(responses[1].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[1].get_text()).replace(" ","").split('/')[1]]: incGenre[0] += 1
	else: decGenre[0] += 1

	if score[str(responses[2].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[2].get_text()).replace(" ","").split('/')[1]]: incGenre[1] += 1
	else: decGenre[1] += 1

	if score[str(responses[2].get_text()).replace(" ","").split('/')[0]] <= score[str(responses[2].get_text()).replace(" ","").split('/')[1]]: incGenre[2] += 1
	else: decGenre[2] += 1

ax = plt.subplot(111)
ax.bar([0, 1, 2], incGenre, width = 0.2, color = 'b', align = 'center')
ax.bar([0.2, 1.2, 2.2], decGenre, width = 0.2, color = 'r', align = 'center')

ax.set_xticks([0.1,1.1,2.1])
ax.set_xticklabels(('Pop', 'Alternate Rock', 'Rock'))
plt.xlabel("Genres[increasing trend, decreasing trend]")
plt.ylabel("Number Of Users")
plt.savefig("Plot1")
plt.clf()

detailed = [0 for i in range(0, 9)]
for user in users[1:]:
	responses = user.find_all("th")
	for i in range(1,4):
		s0 = score[str(responses[i].get_text()).replace(" ","").split('/')[0]]
		s1 = score[str(responses[i].get_text()).replace(" ","").split('/')[1]]
		detailed[s1 - s0 + 4] += 1

ax = plt.subplot(111)
bars = ax.bar(range(0,9), detailed, width = 0.2, align = 'center')
for i in range(0,9):
	if i >= 4: bars[i].set_color('b')
	else: bars[i].set_color('r')

sample_mu = sum([(i-4)*detailed[i] for i in range(0,9)])*1.0/ (sum(detailed)*1.0)
sample_sigma = (sum([((i-4-sample_mu)**2)*detailed[i] for i in range(0,9)])*1.0 / ((sum(detailed) - 1)*1.0))**0.5

print sample_mu, sum(detailed), sample_sigma
ax.set_xticks(range(0,9))
ax.set_xticklabels(range(-4,5))
plt.xlabel("Difference in likability values")
plt.ylabel("Number of Users")
plt.savefig('Plot2')
plt.clf()

detailed2 = [[0 for i in range(0, 9)] for i in range(0,3)]
for user in users[1:]:
	responses = user.find_all("th")
	for i in range(1,4):
		s0 = score[str(responses[i].get_text()).replace(" ","").split('/')[0]]
		s1 = score[str(responses[i].get_text()).replace(" ","").split('/')[1]]
		detailed2[i-1][s1 - s0 + 4] += 1

ax = plt.subplot(111)
ax.bar(range(0,9), detailed2[0], width = 0.2, color = 'c', align = 'center')
ax.bar([i+0.2 for i in range(0,9)], detailed2[1], width = 0.2, color = 'm', align = 'center')
ax.bar([i+0.4 for i in range(0,9)], detailed2[2], width = 0.2, color = 'y', align = 'center')


ax.set_xticks([i+0.2 for i in range(0,9)])
ax.set_xticklabels(range(-4,5))
plt.xlabel("Difference in likability values broken into Genres\n[Pop, Alternate Rock, Rock]")
plt.ylabel("Number of Users")
plt.savefig('Plot3')
plt.clf()