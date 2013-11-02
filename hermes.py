#pipe program through 'python -mjson.tool'
import requests

def main():
	initReply = initializeGame()
	print initReply.text

def initializeGame():
	payload = {
		'Command' : 'INIT',
		'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
		'ChangeRequest' : 'null'
	}
	reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
	return reply

if __name__ == '__main__':
	main()