#pipe program through 'python -mjson.tool'
import requests
import json
from pprint import pprint
import time

def main():
	initializeGame()
	processTurn()

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

def processTurn():
	while True:
		change()
		play()
	
	

def change():
	jsonDict = getDummyJson()
	payload = {
		'Command' : 'CHNG',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : jsonDict
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)

def play():
	jsonDict = getDummyJson()
	payload = {
		'Command' : 'PLAY',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	replyDict = json.loads(reply.text)
	if((int(replyDict['ServerState']['TurnNo'])%100)==0):
		quickInfo(replyDict)

def getDummyJson():
	generatedJSON = json.load(open("standardJSON.json"))
	return generatedJSON

def wait():
	idontgiveafuckinput = raw_input()

def quickInfo(replyDict):
	turn = replyDict['ServerState']['TurnNo']
	bank = replyDict['ServerState']['ProfitAccumulated']
	profit = replyDict['ServerState']['ProfitEarned']
	print "Turn: "+str(turn)
	print "Turn Profit: "+str(profit)
	print "Bankroll Yo: "+str(bank)
	print "-------------------"

if __name__ == '__main__':
	main()