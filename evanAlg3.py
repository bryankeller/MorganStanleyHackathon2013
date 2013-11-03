import bryanRateOfChange

def algorithm(jDict, replies):
	lastReply = replies[len(replies)-1]

	#generates a summary report every 15 turns
	turnNo = lastReply.turnNo()
	analysisInterval = 10

	if((turnNo%analysisInterval)==0 and turnNo > 0):
		#initialize web server data
		naWebSucceeded = euWebSucceeded = apWebSucceeded = 0
		naWebExecuted = euWebExecuted = apWebExecuted = 0
		naWebNodes = euWebNodes = apWebNodes = 0
		naWebInput = euWebInput = apWebInput = 0

		#initialize java server data
		naJavaSucceeded = euJavaSucceeded = apJavaSucceeded = 0
		naJavaExecuted = euJavaExecuted = apJavaExecuted = 0
		naJavaNodes = euJavaNodes = apJavaNodes = 0
		naJavaInput = euJavaInput = apJavaInput = 0

		#initializeaJava server data
		naDBSucceeded = euDBSucceeded = apDBSucceeded = 0
		naDBExecuted = euDBExecuted = apDBExecuted = 0
		naDBNodes = euDBNodes = apDBNodes = 0
		naDBInput = euDBInput = apDBInput = 0

		profit = 0

		#replies = reversed(replies)
		for reply in replies[-analysisInterval:]:
			#Web Server Data
			naWebInput = naWebInput + reply.inputNums('WEB')['na']
			euWebInput = euWebInput + reply.inputNums('WEB')['eu']
			apWebInput = apWebInput + reply.inputNums('WEB')['ap']
			naWebExecuted = naWebExecuted + reply.executedNums('WEB')['na']
			euWebExecuted = euWebExecuted + reply.executedNums('WEB')['eu']
			apWebExecuted = apWebExecuted + reply.executedNums('WEB')['ap']
			naWebSucceeded = naWebSucceeded + reply.successNums('WEB')['na']
			euWebSucceeded = euWebSucceeded + reply.successNums('WEB')['eu']
			apWebSucceeded = apWebSucceeded + reply.successNums('WEB')['ap']
			naWebNodes = lastReply.nodeCounts('WEB')['na']
			euWebNodes = lastReply.nodeCounts('WEB')['eu']
			apWebNodes = lastReply.nodeCounts('WEB')['ap']

			#Java Server Data
			naJavaInput = naJavaInput + reply.inputNums('JAVA')['na']
			euJavaInput = euJavaInput + reply.inputNums('JAVA')['eu']
			apJavaInput = apJavaInput + reply.inputNums('JAVA')['ap']
			naJavaExecuted = naJavaExecuted + reply.executedNums('JAVA')['na']
			euJavaExecuted = euJavaExecuted + reply.executedNums('JAVA')['eu']
			apJavaExecuted = apJavaExecuted + reply.executedNums('JAVA')['ap']
			naJavaSucceeded = naJavaSucceeded + reply.successNums('JAVA')['na']
			euJavaSucceeded = euJavaSucceeded + reply.successNums('JAVA')['eu']
			apJavaSucceeded = apJavaSucceeded + reply.successNums('JAVA')['ap']
			naJavaNodes = lastReply.nodeCounts('JAVA')['na']
			euJavaNodes = lastReply.nodeCounts('JAVA')['eu']
			apJavaNodes = lastReply.nodeCounts('JAVA')['ap']

			#DB Server Data
			naDBInput = naDBInput + reply.inputNums('DB')['na']
			euDBInput = euDBInput + reply.inputNums('DB')['eu']
			apDBInput = apDBInput + reply.inputNums('DB')['ap']
			naDBExecuted = naDBExecuted + reply.executedNums('DB')['na']
			euDBExecuted = euDBExecuted + reply.executedNums('DB')['eu']
			apDBExecuted = apDBExecuted + reply.executedNums('DB')['ap']
			naDBSucceeded = naDBSucceeded + reply.successNums('DB')['na']
			euDBSucceeded = euDBSucceeded + reply.successNums('DB')['eu']
			apDBSucceeded = apDBSucceeded + reply.successNums('DB')['ap']
			naDBNodes = lastReply.nodeCounts('DB')['na']
			euDBNodes = lastReply.nodeCounts('DB')['eu']
			apDBNodes = lastReply.nodeCounts('DB')['ap']

			profit = profit + reply.profitEarned()
			#print "Turn " + str(i) + "    " + str(replies[i]["ServerState"]["ProfitEarned"]) + "   " + str(profit)

		#Averaging Web Servers
		naWebInput = naWebInput/analysisInterval
		euWebInput = euWebInput/analysisInterval
		apWebInput = apWebInput/analysisInterval
		naWebSucceeded = naWebSucceeded/analysisInterval
		euWebSucceeded = euWebSucceeded/analysisInterval
		apWebSucceeded = apWebSucceeded/analysisInterval
		naWebExecuted = naWebExecuted/analysisInterval
		euWebExecuted = euWebExecuted/analysisInterval
		apWebExecuted = apWebExecuted/analysisInterval
		naWebLoad = naWebInput / naWebNodes
		euWebLoad = euWebInput / euWebNodes
		apWebLoad = apWebInput / apWebNodes

		#Averaging Java Servers
		naJavaInput = naJavaInput/analysisInterval
		euJavaInput = euJavaInput/analysisInterval
		apJavaInput = apJavaInput/analysisInterval
		naJavaSucceeded = naJavaSucceeded/analysisInterval
		euJavaSucceeded = euJavaSucceeded/analysisInterval
		apJavaSucceeded = apJavaSucceeded/analysisInterval
		naJavaExecuted = naJavaExecuted/analysisInterval
		euJavaExecuted = euJavaExecuted/analysisInterval
		apJavaExecuted = apJavaExecuted/analysisInterval
		naJavaLoad = naJavaInput / naJavaNodes
		euJavaLoad = euJavaInput / euJavaNodes
		apJavaLoad = apJavaInput / apJavaNodes

		#Averaging DB Servers
		naDBInput = naDBInput/analysisInterval
		euDBInput = euDBInput/analysisInterval
		apDBInput = apDBInput/analysisInterval
		naDBSucceeded = naDBSucceeded/analysisInterval
		euDBSucceeded = euDBSucceeded/analysisInterval
		apDBSucceeded = apDBSucceeded/analysisInterval
		naDBExecuted = naDBExecuted/analysisInterval
		euDBExecuted = euDBExecuted/analysisInterval
		apDBExecuted = apDBExecuted/analysisInterval
		if(naDBNodes==0):
			naDBLoad = 0
		else:
			naDBLoad = naDBInput / naDBNodes

		if(euDBNodes==0):
			euDBLoad = 0
		else:
			euDBLoad = euDBInput / euDBNodes
		
		if(apDBNodes==0):
			apDBLoad = 0
		else:
			apDBLoad = apDBInput / apDBNodes

		if euDBNodes!=0:
			totalDBLoad = (naDBInput + euDBInput + apDBInput) / euDBNodes
		else:
			totalDBLoad = 0

		#total profit infod
		profit = profit/analysisInterval
		bank = lastReply.profitAccumulated()

		turnNo = lastReply.turnNo()

		naWebAdjust = euWebAdjust = apWebAdjust = 0
		naJavaAdjust = euJavaAdjust = apJavaAdjust = 0
		naDBAdjust = euDBAdjust = apDBAdjust = 0


		#Making adjustments for web serverss
		adjustConst = 0.005
		upperBound = 40
		lowerBound = upperBound*.65
		if(algorithm.upgradeLevel == 1):
			upperBound *= 1.05
		if(algorithm.upgradeLevel == 2):
			upperBound *= 1.1

		print "cost: " + str(lastReply.reply["ServerState"]["CostPerServer"])

		if(naWebLoad > upperBound):
			naWebAdjust = int(1 + (naWebInput*adjustConst))
		elif(naWebLoad<lowerBound):
			if(naWebNodes!=1):
				naWebAdjust = int(-1 - (naWebInput*adjustConst))

		if(euWebLoad > upperBound):
			euWebAdjust = int(1 + (euWebInput*adjustConst))
		elif(euWebLoad<lowerBound):
			if(euWebNodes!=1):
				euWebAdjust = int(-1 - (euWebInput*adjustConst))

		if(apWebLoad > upperBound):
			apWebAdjust = int(1 + (apWebInput*adjustConst))
		elif(apWebLoad<lowerBound):
			if(apWebNodes!=1):
				apWebAdjust = int(-1 - (apWebInput*adjustConst))

		roch = bryanRateOfChange.getRateOfChange(replies[-analysisInterval:], "WEB")

		roch = [x*.001 for x in roch]
		print roch
		# adjustConst = 0.003
		upperBound = 120
		lowerBound1 = upperBound*0.6

		if(algorithm.upgradeLevel == 1):
			upperBound *= 1.05
		if(algorithm.upgradeLevel == 2):
			upperBound *= 1.1

		#making adjustments for java
		if(naJavaLoad > upperBound):
			naJavaAdjust = int(1 + (naJavaInput*roch[0]))
		elif(naJavaLoad < lowerBound1):
			if(naJavaNodes!=1):
				naJavaAdjust = int(-1 - (naJavaInput*roch[0]))

		if(euJavaLoad > upperBound):
			euJavaAdjust = int(1 + (euJavaInput*roch[1]))
		elif(euJavaLoad < lowerBound1):
			if(euJavaNodes!=1):
				euJavaAdjust = int(-1 - (euJavaInput*roch[1]))

		if(apJavaLoad > upperBound):
			apJavaAdjust = int(1 + (apJavaInput*roch[2]))
		elif(apJavaLoad < lowerBound1):
			if(apJavaNodes!=1):
				apJavaAdjust = int(-1 - (apJavaInput*roch[2]))

		#making adjustments for db

		upperBound = 280
		lowerBound = upperBound*.8
		if(algorithm.upgradeLevel == 1):
			upperBound *= 1.05
		if(algorithm.upgradeLevel == 2):
			upperBound *= 1.1

		if(totalDBLoad > upperBound):
			euDBAdjust = 1
		elif(totalDBLoad < lowerBound):
			if(euDBNodes > 1):
				euDBAdjust = -1

		jDict.setWebNodeCounts(naWebAdjust, euWebAdjust, apWebAdjust)
		jDict.setJavaNodeCounts(naJavaAdjust, euJavaAdjust, apJavaAdjust)
		jDict.setDBNodeCounts(naDBAdjust, euDBAdjust, apDBAdjust)

		val = lastReply.reply["ServerState"]["InfraStructureUpgradeState"]["Key"]
		error = lastReply.error()


		# ----- Upgrades -----
		if algorithm.didUpgrade:
			algorithm.didUpgrade = False
			jDict.doneUpgrade()

		if(algorithm.upgradeLevel == 0): #and bank > 80000): # and trending up
			jDict.upgradeInfraStructure()
			algorithm.didUpgrade = True
			algorithm.upgradeLevel = algorithm.upgradeLevel + 1 
		elif(algorithm.upgradeLevel == 1 and turnNo > 1450): # and trending up
			jDict.upgradeInfraStructure()
			algorithm.didUpgrade = True
			algorithm.upgradeLevel = algorithm.upgradeLevel + 1 


		print "Turn: " + str(turnNo)
		print "## WEB SERVERS ##"
		print "[NA]  Nodes: " + str(naWebNodes) + ", Input: " + str(naWebInput) + ", Executed: " + str(naWebExecuted) + ", Succeeded: " + str(naWebSucceeded) + ", Avg Load: " + str(naWebLoad)
		print "[EU]  Nodes: " + str(euWebNodes) + ", Input: " + str(euWebInput) + ", Executed: " + str(euWebExecuted) + ", Succeeded: " + str(euWebSucceeded) + ", Avg Load: " + str(euWebLoad)
		print "[AP]  Nodes: " + str(apWebNodes) + ", Input: " + str(apWebInput) + ", Executed: " + str(apWebExecuted) + ", Succeeded: " + str(apWebSucceeded) + ", Avg Load: " + str(apWebLoad)
		print "  "
		print "## Java SERVERS ##"
		print "[NA]  Nodes: " + str(naJavaNodes) + ", Input: " + str(naJavaInput) + ", Executed: " + str(naJavaExecuted) + ", Succeeded: " + str(naJavaSucceeded) + ", Avg Load: " + str(naJavaLoad)
		print "[EU]  Nodes: " + str(euJavaNodes) + ", Input: " + str(euJavaInput) + ", Executed: " + str(euJavaExecuted) + ", Succeeded: " + str(euJavaSucceeded) + ", Avg Load: " + str(euJavaLoad)
		print "[AP]  Nodes: " + str(apJavaNodes) + ", Input: " + str(apJavaInput) + ", Executed: " + str(apJavaExecuted) + ", Succeeded: " + str(apJavaSucceeded) + ", Avg Load: " + str(apJavaLoad)
		print "  "
		print "## DB SERVERS ##"
		print "[NA]  Nodes: " + str(naDBNodes) + ", Input: " + str(naDBInput) + ", Executed: " + str(naDBExecuted) + ", Succeeded: " + str(naDBSucceeded) + ", Avg Load: " + str(naDBLoad)
		print "[EU]  Nodes: " + str(euDBNodes) + ", Input: " + str(euDBInput) + ", Executed: " + str(euDBExecuted) + ", Succeeded: " + str(euDBSucceeded) + ", Total Load: " + str(totalDBLoad)
		print "[AP]  Nodes: " + str(apDBNodes) + ", Input: " + str(apDBInput) + ", Executed: " + str(apDBExecuted) + ", Succeeded: " + str(apDBSucceeded) + ", Avg Load: " + str(apDBLoad)
		print "Total profit $"+str(bank) + "     Average turn profit $" + str(profit)
		print "Inf Level: " + str(val) + "   Error: " + str(error)
		print " "
		print " "
		print " "


	reply = jDict.getGeneratedJSONPostData()
	return reply

algorithm.didUpgrade = False
algorithm.upgradeLevel = 0