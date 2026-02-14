from __future__ import division

import random

TeamA_Wins=input("Input Team A's regular season wins " )
TeamB_Wins=input("Input Team B's regular season wins " )
games_season=82.

TeamA_Series=input("Input Team A's wins in series so far ")
TeamB_Series=input("Input Team B's wins in series so far ")

# Validate series win totals
if TeamA_Series >= 4:
	print "Error: Team A already has 4+ wins. The series is already over (Team A won)."
	exit()
if TeamB_Series >= 4:
	print "Error: Team B already has 4+ wins. The series is already over (Team B won)."
	exit()
if TeamA_Series + TeamB_Series >= 7:
	print "Error: Combined wins (%d) cannot be 7 or more. A series ends when one team reaches 4 wins." % (TeamA_Series + TeamB_Series)
	exit()
if TeamA_Series < 0 or TeamB_Series < 0:
	print "Error: Series wins cannot be negative."
	exit()

pa=TeamA_Wins/games_season
pb=TeamB_Wins/games_season

log5_wins=(pa-pa*pb)/(pa+pb-2*pa*pb)
#print log5_wins

trials=10**5

#print log5

def sim(TeamA,TeamB,odds,series_length):
	#TeamA_Advances=0
	while TeamA<4 and TeamB<4:
			if random.random()<odds:
				TeamA=TeamA+1
			else:
				TeamB=TeamB+1
			#print "A has %d wins, B has %d wins" %(TeamA,TeamB)
	if TeamA>=4:
		#TeamA_Advances=1
		series_length.append(TeamA+TeamB)		
	#return TeamA_Advances

total=0
length=[]
for n in xrange(trials):
	sim(TeamA_Series,TeamB_Series,log5_wins,length)
	#total = total+A
#print total/trials
oddswin= len(length)/trials*100
length.sort()
if TeamB_Series<1:
	odds4=length.index(5)
	print "Odds of Team A winning in 4 games is %d percent" %(odds4/trials*100)
else:
	odds4=0
if TeamB_Series <2:
	odds5=(length.index(6)-odds4)
	print "Odds of Team A winning in 5 games is %d percent" %(odds5/trials*100)
else:
	odds5=0
if TeamB_Series<3:
	odds6= (length.index(7)-odds5-odds4)
	print "Odds of Team A winning in 6 games is %d percent" %(odds6/trials*100)
else:
	odds6=0
odds7=len(length[length.index(7):])
print "Odds of Team A winning in 7 games is %d percent" %(odds7/trials*100)
print "Odds of Team A advancing is %d percent" %((odds4+odds5+odds6+odds7)/trials*100)
print "Odds of Team A being eliminated is %d percent" %(100-oddswin)
#print length


