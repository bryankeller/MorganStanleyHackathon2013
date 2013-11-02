#pipe program through 'python -mjson.tool'
import requests
import json
from pprint import pprint
import time
import JSONPostData

def main():
	print "Enter turn printing interval: "
	num = int(raw_input())
	initializeGame()
	processTurn(num)

def initializeGame():
	payload = {
		'Command' : 'INIT',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	replyDict = json.loads(reply.text)
	print 'Game has started'
	quickInfo(replyDict)
	#wait()
	return reply

def processTurn(num):
	replies = []
	lastReply = None
	while True:
		replies.append(lastReply)
		jtool = getJson()#Creates a new jtool
		jDict = algorithm(jtool, replies)#returns the dict of json file
		change(jDict)
		lastReply = play()#array of all replies
		#if((int(lastReply['ServerState']['TurnNo'])%num)==0):
			#quickInfo(lastReply)
	
def algorithm(jDict, replies):
	lastReply = replies[len(replies)-1]

	#num of successful transfactions in each region
	if(lastReply != None):
		print lastReply['ServerState']['TurnNo']
		print "------------------"
		naNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsSuceeded"]
		euNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsSuceeded"]
		apNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsSuceeded"]

		naSuccesses = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"]
		euSuccesses = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"]
		apSuccesses = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"]

		print "[NA]  Nodes:" + str(naNodes) + ", Successes: " + str(naSuccesses)
		print "[EU]  Nodes:" + str(euNodes) + ", Successes: " + str(euSuccesses)
		print "[AP]  Nodes:" + str(apNodes) + ", Successes: " + str(apSuccesses)
		print "  "
	reply = jDict.getGeneratedJSONPostData()
	return reply


def change(json):
	payload = {
		'Command' : 'CHNG',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : json
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)

def play():
	payload = {
		'Command' : 'PLAY',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	replyDict = json.loads(reply.text)
	return replyDict

def getJson():
	jtool = JSONPostData.JSONPostData()
	return jtool

def quickInfo(replyDict):
	turn = replyDict['ServerState']['TurnNo']
	bank = replyDict['ServerState']['ProfitAccumulated']
	profit = replyDict['ServerState']['ProfitEarned']
	error = replyDict['Error']
	print "Turn: "+str(turn)
	print "Turn Profit: $"+str(profit)
	print "Bankroll: $"+str(bank)
	if error != None:
		print "ERROR: "+str(error)
	print "-------------------"

if __name__ == '__main__':
	main()