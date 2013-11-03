# from JSONPostData import JSONPostData

def algorithm(jDict, replies):
	lastReply = replies[len(replies)-1]

	#generates a summary report every 15 turns
	turnNo = lastReply.turnNo()
	#print "Replies sizeee: "+str(len(replies))
	#print "Turn Nono: "+ str(turnNo)
	analysisInterval = 13
	if((turnNo%analysisInterval)==0 and turnNo!=0):
		length = len(replies)
		lastReply = replies[length-1]

		web = getAdjustment('WEB', 50, .007)
		java = getAdjustment('JAVA', 150, .007)
		db = getAdjustment('DB', 250, .007)

		jDict.setWebNodeCounts(web[0], web[1], web[2])
		jDict.setJavaNodeCounts(java[0], java[1], java[2])
		jDict.setDBNodeCounts(db[0], db[1], db[2])

	reply = jDict.getGeneratedJSONPostData()
	return reply

def getAdjustment(serverType, baseVal, linearConst):
	profit = 0
	naSucceeded = euSucceeded = apSucceeded = 0
	naExecuted = euExecuted = apExecuted = 0
	naNodes = euNodes = apNodes = 0
	naInput = euInput = apInput = 0
	#replies = reversed(replies)

	for reply in replies[-analysisInterval:]:
		#Web Server Data
		naInput = naInput + reply.inputNums(serverType)['na']
		euInput = euInput + reply.inputNums(serverType)['eu']
		apInput = apInput + reply.inputNums(serverType)['ap']
		naExecuted = naExecuted + reply.executedNums(serverType)['na']
		euExecuted = euExecuted + reply.executedNums(serverType)['eu']
		apExecuted = apExecuted + reply.executedNums(serverType)['ap']
		naSucceeded = naSucceeded + reply.successNums(serverType)['na']
		euSucceeded = euSucceeded + reply.successNums(serverType)['eu']
		apSucceeded = apSucceeded + reply.successNums(serverType)['ap']
		naNodes = lastReply.nodeCounts(serverType)['na']
		euNodes = lastReply.nodeCounts(serverType)['eu']
		apNodes = lastReply.nodeCounts(serverType)['ap']

		profit = profit + replies[i].profitEarned()

	#Averaging Web Servers
	naInput = naInput/analysisInterval
	euInput = euInput/analysisInterval
	apInput = apInput/analysisInterval
	naSucceeded = naSucceeded/analysisInterval
	euSucceeded = euSucceeded/analysisInterval
	apSucceeded = apSucceeded/analysisInterval
	naExecuted = naExecuted/analysisInterval
	euExecuted = euExecuted/analysisInterval
	apExecuted = apExecuted/analysisInterval
	naLoad = naInput / naNodes
	euLoad = euInput / euNodes
	apLoad = apInput / apNodes

	naDBLoad = naDBInput / naDBNodes if naDBNodes == 0 else 0
	euDBNodes = naDBInput / naDBNodes if naDBNodes == 0 else 0
	apDBLoad = naDBInput / naDBNodes if naDBNodes == 0 else 0

	#total profit infod
	profit = profit/analysisInterval
	bank = lastReply.profitAccumulated()

	turnNo = lastReply.turnNo()

	naAdjust = euAdjust = apAdjust = 0

	for load in [naLoad, euLoad, apLoad]:
		if(load > baseVal):
			naAdjust = 3
		elif(load > 80):
			naAdjust = 2
		elif(load > 50):
			naAdjust = 1
		elif(load < 60):
			if(load < 20):
				if (naNodes>5):
					naAdjust = -5
			elif(load < 40):
				if (naNodes>3):
					naAdjust = -3
			elif (naNodes!=1):
				naAdjust = -1

	return [naAdjust, euAdjust, apAdjust]

