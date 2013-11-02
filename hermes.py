#pipe program through 'python -mjson.tool'
import requests

def main():
	initReply = initializeGame()
	print initReply.text
	#play()

def initializeGame():
	payload = {
		'Command' : 'INIT',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	return reply

def processTurn(data):
	json = x

	payload = {
		'Command' : 'CHNG',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	processTurn(reply)

def play():
	payload = {
		'Command' : 'PLAY',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : None
	}
	requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	play()

if __name__ == '__main__':
	main()