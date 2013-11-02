#pipe program through 'python -mjson.tool'
import requests
import json
from pprint import pprint
import time
from ProcessedReply import ProcessedReply
from JSONPostData import JSONPostData
import bryanAlg
#import liamAlg
import evanAlg


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
	# quickInfo(replyDict)
	return reply

def processTurn(num):
	replies = []
	posts = []

	while True:
		lastReply = play()
		lastReply = ProcessedReply(lastReply)
		replies.append(lastReply)
		emptyPost = JSONPostData()
		post = evanAlg.algorithm(emptyPost, replies) #returns the dict of json file
		change(post)
		posts.append(post)
		# printStats(lastReply)
		#printStats(lastReply)
		#if((int(lastReply['ServerState']['TurnNo'])%num)==0):
			#quickInfo(lastReply)

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