#pipe program through 'python -mjson.tool'
import requests
import json
from pprint import pprint
import time
from JSONPostData import JSONPostData

from processReply import *


def main():
	print "Enter turn printing interval: "
	num = int(raw_input())
	initializeGame()
	processTurn(num)

def initializeGame():
	headers = {'content-type': 'application/json'}
	payload = {
		'Command' : 'INIT',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=json.dumps(payload), headers=headers)
	replyDict = json.loads(reply.text)
	print 'Game has started'
	quickInfo(replyDict)
	return reply

def processTurn(num):
	replies = []
	posts = []

	i = 0
	while i < 4:
		lastReply = play()
		replies.append(lastReply)
		emptyPost = JSONPostData()
		post = algorithm(emptyPost, replies) #returns the dict of json file
		change(post)
		posts.append(post)
		i = i + 1
		printStats(lastReply)
		#printStats(lastReply)
		#if((int(lastReply['ServerState']['TurnNo'])%num)==0):
			#quickInfo(lastReply)
	
def algorithm(post, replies):
	newPost = JSONPostData()
	lastReply = replies[-1]
	#generates a summary report every 15 turns
	turnNo = int(lastReply['ServerState']['TurnNo'])
	#print "Replies sizeee: "+str(len(replies))
	#print "Turn Nono: "+ str(turnNo)
	newPost.setWebNodeCounts(eu=3)

	if((turnNo%15)==0 and turnNo!=0):
		summary(replies);

	reply = newPost.getGeneratedJSONPostData()
	return reply

def summary(replies):
	#print "Replies size: "+str(len(replies))
	length = len(replies)
	lastReply = replies[length-1]
	naExecuted = euExecuted = apExecuted = naNodes = euNodes = apNodes = profit= 0
	#replies = reversed(replies)
	for i in range(length-15,length):
		naExecuted = naExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsInput"]
		euExecuted = euExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsInput"]
		apExecuted = apExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsInput"]
		naSucceeded = naExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsInput"]
		euSucceeded = euExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsInput"]
		ap = apExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsInput"]
		naNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"]
		euNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"]
		apNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"]
		profit = profit + int(replies[i]["ServerState"]["ProfitEarned"])
		#print "Turn " + str(i) + "    " + str(replies[i]["ServerState"]["ProfitEarned"]) + "   " + str(profit)

	lastReply = replies[length-1]
	naExecuted = naExecuted/15  
	euExecuted = euExecuted/15 
	apExecuted = apExecuted/15 
	profit = profit/15
	bank = lastReply["ServerState"]["ProfitAccumulated"]
	turnNo = int(lastReply['ServerState']['TurnNo'])

	print "Turn: " + str(turnNo)
	print "[NA]  Nodes:" + str(naNodes) + ", Executed: " + str(naExecuted)
	print "[EU]  Nodes:" + str(euNodes) + ", Executed: " + str(euExecuted)
	print "[AP]  Nodes:" + str(apNodes) + ", Executed: " + str(apExecuted)
	print "Total profit $"+str(bank) + "     Average turn profit $" + str(profit)
	print " "




def change(request):
	headers = {'content-type': 'application/json'}
	payload = {
		'Command' : 'CHNG',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : request
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=json.dumps(payload), headers=headers)

def play():
	headers = {'content-type': 'application/json'}
	payload = {
		'Command' : 'PLAY',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=json.dumps(payload), headers=headers)
	replyDict = json.loads(reply.text)
	return replyDict

if __name__ == '__main__':
	main()