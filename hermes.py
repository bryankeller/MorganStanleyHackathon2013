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
	payload = {
		'Command' : 'INIT',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	replyDict = json.loads(reply.text)
	print 'Game has started'
	quickInfo(replyDict)
	return reply

def processTurn(num):
	replies = []
	posts = []

	while True:
		emptyPost = JSONPostData()
		post = algorithm(emptyPost, replies) #returns the dict of json file
		change(post)
		lastReply = play()

		replies.append(lastReply)
		posts.append(post)
		printStats(lastReply)
		#if((int(lastReply['ServerState']['TurnNo'])%num)==0):
			#quickInfo(lastReply)
	
def algorithm(post, replies):
	if len(replies):
		lastReply = replies[-1]

		# --- Algorithm goes here ----

		if profitEarned(lastReply) > 100:
			post.setWebNodeCounts(eu=10)



		# ----------------------------

	return post.getGeneratedJSONPostData()



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

if __name__ == '__main__':
	main()