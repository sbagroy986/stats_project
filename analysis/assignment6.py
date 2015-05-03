#Ambar Pal, 2014012

import matplotlib.pyplot as P
import numpy as N

f = open('data.csv', 'r')
x = f.readlines()

numUsers, nineteenMale, obCorrect,ogCorrect, gbCorrect, ob, gb, nineteenMaleCorrect = 0, 0, 0, 0, 0, 0, 0, 0
correctResponseOB, correctResponseGB, correctResponseOG  = dict(), dict(), dict()
obMean, gbMean, ogMean = 0, 0, 0
def f(x): return map(int,sorted(x.keys())), [x[y] for y in sorted(x.keys())]

for i in xrange(1,4536):
	x[i] = x[i].split(',')
	numUsers += 1
	if x[i][7] == 'M' and int(x[i][8]) == 19: nineteenMale += 1
	if x[i][7] == 'M' and int(x[i][8]) == 19 and x[i][4] == x[i][5]: nineteenMaleCorrect += 1
	if x[i][3] == 'OB': ob += 1
	if x[i][3] == 'OB' and x[i][4] == x[i][5]:
		obMean += int(x[i][6])
		obCorrect += 1
		key = int(x[i][6])
		if key in correctResponseOB:
			correctResponseOB[key] += 1
		else:
			correctResponseOB[key] = 1
	if x[i][3] == 'GB': gb += 1
	if x[i][3] == 'GB' and x[i][4] == x[i][5]:
		gbMean += int(x[i][6])
		gbCorrect += 1
		key = int(x[i][6])
		if key in correctResponseGB:
			correctResponseGB[key] += 1
		else:
			correctResponseGB[key] = 1
	if x[i][3] == 'OG' and x[i][4] == x[i][5]:
		ogMean += int(x[i][6])
		ogCorrect += 1
		key = int(x[i][6])
		if key in correctResponseOG:
			correctResponseOG[key] += 1
		else:
			correctResponseOG[key] = 1	

obActualMean = obMean*1.0/obCorrect
ogActualMean = ogMean*1.0/ogCorrect
gbActualMean = gbMean*1.0/gbCorrect

print "OB Actual Mean:", obActualMean
print "OG Actual Mean: ", ogActualMean
print "GB Actual Mean: ", gbActualMean

##############################
#Ans 1, Ans2 and Ans3
print "Q1: ", nineteenMaleCorrect/(1.0*nineteenMale), "\n", "Q2: ", obCorrect/(1.0*ob), "\n", "Q3: ", gbCorrect/(1.0*gb)

##############################
#Ans 4a
lk, l = f(correctResponseOB)
P.title('Correct User Responses vs Confidence Value, Question type OB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('4a')
P.clf()

##############################
#Ans 4b
lk, l = f(correctResponseGB)
P.title('Correct User Responses vs Confidence Value, Question type GB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('4b')
P.clf()

##############################
#Ans 4c
lk, l = f(correctResponseOG)
P.title('Correct User Responses vs Confidence Value, Question type OG')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('4c')
P.clf()

##############################
#Ans 4. "Comment" on the three histograms
#Similarities between the three histograms:
#a) The common feature is that the confidence level 10 always garners a huge amount of votes
#this is partially because the set of questions asked were fairly easy and could be answered with a high
#confidence.
#b) The same reason holds for the fact that the number of votes increases at a good rate as the 
#confidence increases.

#Dissimilarities between the three histograms:
#a) The OG histogram sees a high shift of the votes towards the higher end of the confidence values.
#The same is not seen in other two histograms,OB and GB.

twentyIdsTemp = dict()
for i in xrange(1,4536): twentyIdsTemp[int(x[i][2])] = 1

twentyIds = list(twentyIdsTemp.keys())
twentyIds = N.random.permutation(twentyIds)[0:20]

correctResponseOB20, correctResponseGB20, correctResponseOG20  = dict(), dict(), dict()
for i in xrange(1,4536): 
	flag = 0
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if (flag == 1):
		if x[i][3] == 'OB' and x[i][4] == x[i][5]:
			key = int(x[i][6])
			if key in correctResponseOB20:
				correctResponseOB20[key] += 1
			else:
				correctResponseOB20[key] = 1
		if x[i][3] == 'GB' and x[i][4] == x[i][5]:
			gbMean += int(x[i][6])
			if key in correctResponseGB20:
				correctResponseGB20[key] += 1
			else:
				correctResponseGB20[key] = 1
		if x[i][3] == 'OG' and x[i][4] == x[i][5]:
			key = int(x[i][6])
			if key in correctResponseOG20:
				correctResponseOG20[key] += 1
			else:
				correctResponseOG20[key] = 1	

##############################
#Ans 5a
lk, l = f(correctResponseOB20)
P.title('Correct User Responses vs Confidence Value Random Sample 20, Question type OB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('5a')
P.clf()

##############################
#Ans 5b
lk, l = f(correctResponseGB20)
P.title('Correct User Responses vs Confidence Value Random Sample 20, Question type GB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('5b')
P.clf()

##############################
#Ans 5c
lk, l = f(correctResponseOG20)
P.title('Correct User Responses vs Confidence Value Random Sample 20, Question type OG')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('5c')
P.clf()

##############################
#Ans 5d
#finding mean, variance and construction of 95% confidence values
ogMean = sum([ i*correctResponseOG20[i] for i in correctResponseOG20.keys()]) * 1.0 / sum([ correctResponseOG20[i] for i in correctResponseOG20.keys()]) 
obMean = sum([ i*correctResponseOB20[i] for i in correctResponseOB20.keys()]) * 1.0 / sum([ correctResponseOB20[i] for i in correctResponseOB20.keys()]) 
gbMean = sum([ i*correctResponseGB20[i] for i in correctResponseGB20.keys()]) * 1.0 / sum([ correctResponseGB20[i] for i in correctResponseGB20.keys()])

ogVar = sum([ correctResponseOG20[i]*((i - ogMean)**2) for i in correctResponseOG20.keys()]) * 1.0 / sum([ correctResponseOG20[i] for i in correctResponseOG20.keys()])
obVar = sum([ correctResponseOB20[i]*((i - obMean)**2) for i in correctResponseOB20.keys()]) * 1.0 / sum([ correctResponseOB20[i] for i in correctResponseOB20.keys()]) 
gbVar = sum([ correctResponseGB20[i]*((i - gbMean)**2) for i in correctResponseGB20.keys()]) * 1.0 / sum([ correctResponseGB20[i] for i in correctResponseGB20.keys()]) 

ogNum = sum([ correctResponseOG20[i] for i in correctResponseOG20.keys()])
obNum = sum([ correctResponseOB20[i] for i in correctResponseOB20.keys()])
gbNum = sum([ correctResponseGB20[i] for i in correctResponseGB20.keys()])

print "Confidence Values for sample size = 20"
print "\nOG20", ogMean - 1.96*(ogVar*1.0/ogNum)**0.5, " to ", ogMean + 1.96*(ogVar*1.0/200)**0.5 
print "OB20", obMean - 1.96*(obVar*1.0/obNum)**0.5, " to ", obMean + 1.96*(obVar*1.0/200)**0.5 
print "GB20", gbMean - 1.96*(gbVar*1.0/gbNum)**0.5, " to ", gbMean + 1.96*(gbVar*1.0/200)**0.5 
print "\n"

twentyIdsTemp = dict()
for i in xrange(1,4536): twentyIdsTemp[int(x[i][2])] = 1

twentyIds = list(twentyIdsTemp.keys())
twentyIds = N.random.permutation(twentyIds)[0:80]

correctResponseOB80, correctResponseGB80, correctResponseOG80  = dict(), dict(), dict()
for i in xrange(1,4536):
	flag = 0
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if (flag == 1):
		if x[i][3] == 'OB' and x[i][4] == x[i][5]:
			key = int(x[i][6])
			if key in correctResponseOB80:
				correctResponseOB80[key] += 1
			else:
				correctResponseOB80[key] = 1
		if x[i][3] == 'GB' and x[i][4] == x[i][5]:
			gbMean += int(x[i][6])
			if key in correctResponseGB80:
				correctResponseGB80[key] += 1
			else:
				correctResponseGB80[key] = 1
		if x[i][3] == 'OG' and x[i][4] == x[i][5]:
			key = int(x[i][6])
			if key in correctResponseOG80:
				correctResponseOG80[key] += 1
			else:
				correctResponseOG80[key] = 1	

##############################
#Ans 6a
lk, l = f(correctResponseOB80)
P.title('Correct User Responses vs Confidence Value Random Sample 80, Question type OB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('6a')
P.clf()

##############################
#Ans 6b
lk, l = f(correctResponseGB80)
P.title('Correct User Responses vs Confidence Value Random Sample 80, Question type GB')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('6b')
P.clf()

##############################
#Ans 6c
lk, l = f(correctResponseOG80)
P.title('Correct User Responses vs Confidence Value Random Sample 80, Question type OG')
P.bar(lk, l, width=0.8, bottom=None, hold=None, align='center')
P.xlabel('Confidence Value')
P.ylabel('Number of Correct User Responses')
P.savefig('6c')
P.clf()

##############################
#Ans 6d
#finding mean, variance and construction of 95% confidence values
ogMean2 = sum([ i*correctResponseOG80[i] for i in correctResponseOG80.keys()]) * 1.0 / sum([ correctResponseOG80[i] for i in correctResponseOG80.keys()]) 
obMean2 = sum([ i*correctResponseOB80[i] for i in correctResponseOB80.keys()]) * 1.0 / sum([ correctResponseOB80[i] for i in correctResponseOB80.keys()]) 
gbMean2 = sum([ i*correctResponseOG80[i] for i in correctResponseOG80.keys()]) * 1.0 / sum([ correctResponseOG80[i] for i in correctResponseOG80.keys()])

ogVar2 = sum([ correctResponseOG80[i]*((i - ogMean)**2) for i in correctResponseOG80.keys()]) * 1.0 / sum([ correctResponseOG80[i] for i in correctResponseOG80.keys()])
obVar2 = sum([ correctResponseOB80[i]*((i - obMean)**2) for i in correctResponseOB80.keys()]) * 1.0 / sum([ correctResponseOB80[i] for i in correctResponseOB80.keys()]) 
gbVar2 = sum([ correctResponseOG80[i]*((i - gbMean)**2) for i in correctResponseOG80.keys()]) * 1.0 / sum([ correctResponseOG80[i] for i in correctResponseOG80.keys()]) 

ogNum2 = sum([ correctResponseOG80[i] for i in correctResponseOG80.keys()])
obNum2 = sum([ correctResponseOB80[i] for i in correctResponseOB80.keys()])
gbNum2 = sum([ correctResponseGB80[i] for i in correctResponseGB80.keys()])

print "Confidence Values for sample size = 80"
print "\nOG80", ogMean2 - 1.96*(ogVar2*1.0/ogNum2)**0.5, " to ", ogMean2 + 1.96*(ogVar2*1.0/200)**0.5 
print "OB80", obMean2 - 1.96*(obVar2*1.0/obNum2)**0.5, " to ", obMean2 + 1.96*(obVar2*1.0/200)**0.5 
print "GB80", gbMean2 - 1.96*(gbVar2*1.0/gbNum2)**0.5, " to ", gbMean2 + 1.96*(gbVar2*1.0/200)**0.5 
print "\n"

##############################
#Ans 7
if ogMean - 1.96*(ogVar*1.0/ogNum)**0.5<= ogActualMean <= ogMean + 1.96*(ogVar*1.0/200)**0.5:
	print "OG Mean lies within Q5 Interval"
else: print "OG Mean does not lie within Q4 Interval"

if obMean - 1.96*(obVar*1.0/obNum)**0.5<= obActualMean <= obMean + 1.96*(obVar*1.0/200)**0.5:
	print "OB Mean lies within Q5 Interval"
else: print "OB Mean does not lie within Q4 Interval"

if gbMean - 1.96*(gbVar*1.0/gbNum)**0.5<= gbActualMean <= gbMean + 1.96*(gbVar*1.0/200)**0.5:
	print "GB Mean lies within Q5 Interval"
else: print "GB Mean does not lie within Q5 Interval"
print "\n"
#n = 20
twentyIdsTemp = dict()
for i in xrange(1,4536): twentyIdsTemp[int(x[i][2])] = 1

twentyIds = []
twentyIds = list(twentyIdsTemp.keys())
twentyIds = N.random.permutation(twentyIds)[0:20]
# print twentyIds

muNum, muDen, n = 0, 0, 0
for i in xrange(1,4536):
	flag = 0
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1: n += 1
	if flag == 1 and x[i][4] == x[i][5]:
		muNum += int(x[i][6])
		muDen += 1
mu = muNum*1.0/muDen
varNum = 0
for i in xrange(1,4536):
	flag = 0
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1 and x[i][4] == x[i][5]:
		varNum += (int(x[i][6]) - mu)**2
var=varNum*1.0/muDen
t = abs(mu-9)*1.0/(var/(n**0.5))

# print mu, var, n

##############################
#Ans 8a
if t>1.96: print "Null Hypothesis is rejected for sample size 20"
else: print "Null Hypothesis is accepted for sample size 20"

#n = 40
twentyIdsTemp = dict()
for i in xrange(1,4536): twentyIdsTemp[int(x[i][2])] = 1

twentyIds = []
twentyIds = list(twentyIdsTemp.keys())
twentyIds = N.random.permutation(twentyIds)[0:40]
# print twentyIds

muNum, muDen, n = 0, 0, 0
for i in xrange(1,4536):
	flag = 0 
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1: n += 1
	if flag == 1 and x[i][4] == x[i][5]:
		muNum += int(x[i][6])
		muDen += 1
mu = muNum*1.0/muDen
varNum = 0
for i in xrange(1,4536):
	flag = 0
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1 and x[i][4] == x[i][5]:
		varNum += (int(x[i][6]) - mu)**2
var=varNum*1.0/muDen
t = abs(mu-9)*1.0/(var/(n**0.5))

# print mu, var, n
##############################
#Ans 8b
if t>1.96: print "Null Hypothesis is rejected for sample size 40"
else: print "Null Hypothesis is accepted for sample size 40"

#n = 60
twentyIdsTemp = dict()
for i in xrange(1,4536): twentyIdsTemp[int(x[i][2])] = 1

twentyIds = []
twentyIds = list(twentyIdsTemp.keys())
twentyIds = N.random.permutation(twentyIds)[0:60]
# print twentyIds

muNum, muDen, n = 0, 0, 0
for i in xrange(1,4536):
	flag = 0 
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1: n += 1
	if flag == 1 and x[i][4] == x[i][5]:
		muNum += int(x[i][6])
		muDen += 1
mu = muNum*1.0/muDen
varNum = 0
for i in xrange(1,4536):
	for j in twentyIds:
		if int(x[i][2]) == j: flag = 1
	if flag == 1 and x[i][4] == x[i][5]:
		varNum += (int(x[i][6]) - mu)**2
var=varNum*1.0/muDen
t = abs(mu-9)*1.0/(var/(n**0.5))
# print mu, var, n

##############################
#Ans 8c
if t>1.96: print "Null Hypothesis is rejected for sample size 60"
else: print "Null Hypothesis is accepted for sample size 60"

#9th question
ob9, gb9 = dict(), dict()
nob, ngb = 0, 0 
for i in xrange(1,4536):
	key = int(x[i][6])
	if x[i][3] == 'OB':
		if key in ob9: ob9[key] += 1
		else: ob9[key] = 1
		nob += 1
	if x[i][3] == 'GB':
		gbMean += int(x[i][6])
		if key in gb9: gb9[key] += 1
		else: gb9[key] = 1
		ngb += 1

# print nob, ngb
obm = sum(i*ob9[i] for i in ob9.keys())*1.0/sum(ob9[i] for i in ob9.keys())
gbm = sum(i*gb9[i] for i in gb9.keys())*1.0/sum(gb9[i] for i in gb9.keys())

obvar = sum(((i-obm)**2)*ob9[i] for i in ob9.keys())*1.0/sum(ob9[i] for i in ob9.keys())
gbvar = sum(((i-gbm)**2)*gb9[i] for i in gb9.keys())*1.0/sum(gb9[i] for i in gb9.keys())

# print obm, gbm
# print obvar, gbvar
stat = abs(obm - gbm)*1.0/((obvar*1.0/nob + gbVar*1.0/ngb)**0.5)

##############################
#Ans 9
if (stat < 1.96): print "muOB is equal to muGB, hypothesis is accepted"
else: print "muOB is equal to muGB, hypothesis is rejected"