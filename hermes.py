#pipe program through 'python -mjson.tool'
import requests
import json

payload = {
	'Command' : 'INIT',
	'Token' : '63b92b83-041d-4fac-a4db-07be7219f604',
	'ChangeRequest' : 'null'
}
reply = requests.post(r'http://hermes.wha.la/api/hermes', data=payload)
print reply.text
