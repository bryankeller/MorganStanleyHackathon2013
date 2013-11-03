# from JSONPostData import JSONPostData

def algorithm(jDict, replies):
	lastReply = replies[len(replies)-1]

	#generates a summary report every 15 turns
	turnNo = lastReply.turnNo()
	#print "Replies sizeee: "+str(len(replies))
	#print "Turn Nono: "+ str(turnNo)
	analysisInterval = 10
	if((turnNo%analysisInterval)==0 and turnNo!=0):
		length = len(replies)
		lastReply = replies[length-1]
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
		for i in range(length-analysisInterval,length):
			#Web Server Data
			naWebInput = naWebInput + replies[i].inputNums('WEB')['na']
			euWebInput = euWebInput + replies[i].inputNums('WEB')['eu']
			apWebInput = apWebInput + replies[i].inputNums('WEB')['ap']
			naWebExecuted = naWebExecuted + replies[i].executedNums('WEB')['na']
			euWebExecuted = euWebExecuted + replies[i].executedNums('WEB')['eu']
			apWebExecuted = apWebExecuted + replies[i].executedNums('WEB')['ap']
			naWebSucceeded = naWebSucceeded + replies[i].successNums('WEB')['na']
			euWebSucceeded = euWebSucceeded + replies[i].successNums('WEB')['eu']
			apWebSucceeded = apWebSucceeded + replies[i].successNums('WEB')['ap']
			naWebNodes = lastReply.nodeCounts('WEB')['na']
			euWebNodes = lastReply.nodeCounts('WEB')['eu']
			apWebNodes = lastReply.nodeCounts('WEB')['ap']

			#Java Server Data
			naJavaInput = naJavaInput + replies[i].inputNums('JAVA')['na']
			euJavaInput = euJavaInput + replies[i].inputNums('JAVA')['eu']
			apJavaInput = apJavaInput + replies[i].inputNums('JAVA')['ap']
			naJavaExecuted = naJavaExecuted + replies[i].executedNums('JAVA')['na']
			euJavaExecuted = euJavaExecuted + replies[i].executedNums('JAVA')['eu']
			apJavaExecuted = apJavaExecuted + replies[i].executedNums('JAVA')['ap']
			naJavaSucceeded = naJavaSucceeded + replies[i].successNums('JAVA')['na']
			euJavaSucceeded = euJavaSucceeded + replies[i].successNums('JAVA')['eu']
			apJavaSucceeded = apJavaSucceeded + replies[i].successNums('JAVA')['ap']
			naJavaNodes = lastReply.nodeCounts('JAVA')['na']
			euJavaNodes = lastReply.nodeCounts('JAVA')['eu']
			apJavaNodes = lastReply.nodeCounts('JAVA')['ap']

			#DB Server Data
			naDBInput = naDBInput + replies[i].inputNums('DB')['na']
			euDBInput = euDBInput + replies[i].inputNums('DB')['eu']
			apDBInput = apDBInput + replies[i].inputNums('DB')['ap']
			naDBExecuted = naDBExecuted + replies[i].executedNums('DB')['na']
			euDBExecuted = euDBExecuted + replies[i].executedNums('DB')['eu']
			apDBExecuted = apDBExecuted + replies[i].executedNums('DB')['ap']
			naDBSucceeded = naDBSucceeded + replies[i].successNums('DB')['na']
			euDBSucceeded = euDBSucceeded + replies[i].successNums('DB')['eu']
			apDBSucceeded = apDBSucceeded + replies[i].successNums('DB')['ap']
			naDBNodes = lastReply.nodeCounts('DB')['na']
			euDBNodes = lastReply.nodeCounts('DB')['eu']
			apDBNodes = lastReply.nodeCounts('DB')['ap']

			profit = profit + replies[i].profitEarned()
			#print "Turn " + str(i) + "    " + str(replies[i]["ServerState"]["ProfitEarned"]) + "   " + str(profit)

		lastReply = replies[length-1]

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

		totalDBLoad = (naDBInput + euDBInput + apDBInput) / euDBNodes

		#total profit infod
		profit = profit/analysisInterval
		bank = lastReply.profitAccumulated()

		turnNo = lastReply.turnNo()

		naWebAdjust = euWebAdjust = apWebAdjust = 0
		naJavaAdjust = euJavaAdjust = apJavaAdjust = 0
		naDBAdjust = euDBAdjust = apDBAdjust = 0


		#Making adjustments for web serverss
		adjustConst = 0.004
		upperBound = lastReply.upperLimit('WEB')
		lowerBound = upperBound*.8

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

		adjustConst = 0.003
		upperBound = lastReply.upperLimit('JAVA') * 0.9
		lowerBound1 = upperBound*0.6
		# upperBound = lastReply.upperLimit('JAVA')
		# lowerBound1 = upperBound*.833
		# lowerBound2 = upperBound*.633
		# lowerBound3 = upperBound*.480

		# if(naJavaLoad > upperBound):
		# 	naJavaAdjust = 2
		# elif(naJavaLoad > lowerBound1):
		# 	naJavaAdjust = 1
		# elif(naJavaLoad < lowerBound2):
		# 	if (naJavaNodes!=1):
		# 		naJavaAdjust = -1

		# if(euJavaLoad > upperBound):
		# 	euJavaAdjust = 2
		# elif(euJavaLoad > lowerBound1):
		# 	euJavaAdjust = 1
		# elif(euJavaLoad < lowerBound2):
		# 	if (euJavaNodes!=1):
		# 		euJavaAdjust = -1

		# if(apJavaLoad > upperBound):
		# 	apJavaAdjust = 2
		# elif(apJavaLoad > lowerBound1):
		# 	apJavaAdjust = 1
		# elif(apJavaLoad < lowerBound2):
		# 	if(apJavaLoad < lowerBound3):
		# 		if(apJavaNodes > 3):
		# 			apJavaAdjust = -3
		# 	elif (apJavaNodes!=1):
		# 		apJavaAdjust = -1

		#making adjustments for java
		if(naJavaLoad > upperBound):
			naJavaAdjust = int(1 + (naJavaInput*adjustConst))
		elif(naJavaLoad < lowerBound1):
			if(naJavaNodes!=1):
				naJavaAdjust = int(-1 - (naJavaInput*adjustConst))

		if(euJavaLoad > upperBound):
			euJavaAdjust = int(1 + (euJavaInput*adjustConst))
		elif(euJavaLoad < lowerBound1):
			if(euJavaNodes!=1):
				euJavaAdjust = int(-1 - (euJavaInput*adjustConst))

		if(apJavaLoad > upperBound):
			apJavaAdjust = int(1 + (apJavaInput*adjustConst))
		elif(apJavaLoad < lowerBound1):
			if(apJavaNodes!=1):
				apJavaAdjust = int(-1 - (apJavaInput*adjustConst))

		#making adjustments for db

		upperBound = lastReply.upperLimit('DB')*.6875
		lowerBound = upperBound*.8

		if(totalDBLoad > upperBound):
			euDBAdjust = 1
		elif(totalDBLoad < lowerBound):
			if(euDBNodes > 1):
				euDBAdjust = -1

		if(turnNo == 1500):
			jDict.upgradeInfraStructure()

		jDict.setWebNodeCounts(naWebAdjust, euWebAdjust, apWebAdjust)
		jDict.setJavaNodeCounts(naJavaAdjust, euJavaAdjust, apJavaAdjust)
		jDict.setDBNodeCounts(naDBAdjust, euDBAdjust, apDBAdjust)


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
		print " "
		print " "
		print " "


	reply = jDict.getGeneratedJSONPostData()
	return reply
