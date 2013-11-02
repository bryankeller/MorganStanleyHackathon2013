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
	while True:
		change()
		play(num)
	

def change():
	jsonDict = getDummyJson()
	payload = {
		'Command' : 'CHNG',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : jsonDict
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)

def play(num):
	jsonDict = getDummyJson()
	payload = {
		'Command' : 'PLAY',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	replyDict = json.loads(reply.text)
	if((int(replyDict['ServerState']['TurnNo'])%num)==0):
		quickInfo(replyDict)

def getDummyJson():
	jtool = JSONPostData.JSONPostData()
	newJson = jtool.getGeneratedJSONPostData()
	return newJson

def quickInfo(replyDict):
	turn = replyDict['ServerState']['TurnNo']
	bank = replyDict['ServerState']['ProfitAccumulated']
	profit = replyDict['ServerState']['ProfitEarned']
	print "Turn: "+str(turn)
	print "Turn Profit: $"+str(profit)
	print "Bankroll: $"+str(bank)
	print "-------------------"

if __name__ == '__main__':
	main()