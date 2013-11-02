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

		#total profit infod
		profit = profit/analysisInterval
		bank = lastReply.profitAccumulated()

		turnNo = lastReply.turnNo()

		naWebAdjust = euWebAdjust = apWebAdjust = 0
		naJavaAdjust = euJavaAdjust = apJavaAdjust = 0

		#Making adjustments for web servers
		if(naWebLoad > 100):
			naWebAdjust = 2
		elif(naWebLoad > 50):
			naWebAdjust = 1
		elif(naWebLoad < 60):
			if (naWebNodes!=1):
				naWebAdjust = -1

		if(euWebLoad > 100):
			euWebAdjust = 2
		elif(euWebLoad > 50):
			euWebAdjust = 1
		elif(euWebLoad < 60):
			if (euWebNodes!=1):
				euWebAdjust = -1

		if(apWebLoad > 100):
			apWebAdjust = 2
		elif(apWebLoad > 50):
			apWebAdjust = 1
		elif(apWebLoad < 60):
			if (apWebNodes!=1):
				apWebAdjust = -1

		#making adjustments for java
		if(naJavaLoad > 125):
			naJavaAdjust = 1
		elif(naJavaLoad < 75):
			if (naJavaNodes!=1):
				naJavaAdjust = -1

		if(euJavaLoad > 125):
			euJavaAdjust = 1
		elif(euJavaLoad < 75):
			if (euJavaNodes!=1):
				euJavaAdjust = -1

		if(apJavaLoad > 125):
			apJavaAdjust = 2
		elif(apJavaLoad < 75):
			if (apJavaNodes!=1):
				apJavaAdjust = -1


		jDict.setWebNodeCounts(naWebAdjust, euWebAdjust, apWebAdjust)
		jDict.setJavaNodeCounts(naJavaAdjust, euJavaAdjust, apJavaAdjust)


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
		print "[EU]  Nodes: " + str(euDBNodes) + ", Input: " + str(euDBInput) + ", Executed: " + str(euDBExecuted) + ", Succeeded: " + str(euDBSucceeded) + ", Avg Load: " + str(euDBLoad)
		print "[AP]  Nodes: " + str(apDBNodes) + ", Input: " + str(apDBInput) + ", Executed: " + str(apDBExecuted) + ", Succeeded: " + str(apDBSucceeded) + ", Avg Load: " + str(apDBLoad)
		print "Total profit $"+str(bank) + "     Average turn profit $" + str(profit)
		print " "
		print " "
		print " "


	reply = jDict.getGeneratedJSONPostData()
	return reply



