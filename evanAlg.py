def algorithm(jDict, replies):
	lastReply = replies[len(replies)-1]

	#generates a summary report every 15 turns
	turnNo = lastReply.turnNo()
	#print "Replies sizeee: "+str(len(replies))
	#print "Turn Nono: "+ str(turnNo)
	if((turnNo%15)==0 and turnNo!=0):
		length = len(replies)
		lastReply = replies[length-1]
		naSucceeded = euSucceeded = apSucceeded = 0
		naExecuted = euExecuted = apExecuted = 0
		naNodes = euNodes = apNodes = 0
		naInput = euInput = apInput = 0
		profit = 0

		#replies = reversed(replies)
		for i in range(length-15,length):
			naInput = naInput + replies[i].inputNums()['na']
			euInput = euInput + replies[i].inputNums()['eu']
			apInput = apInput + replies[i].inputNums()['ap']

			naExecuted = naExecuted + replies[i].executedNums()['na']
			euExecuted = euExecuted + replies[i].executedNums()['eu']
			apExecuted = apExecuted + replies[i].executedNums()['ap']

			naSucceeded = naSucceeded + replies[i].successNums()['na']
			euSucceeded = euSucceeded + replies[i].successNums()['eu']
			apSucceeded = apSucceeded + replies[i].successNums()['ap']

			naNodes = lastReply.nodeCounts()['na']
			euNodes = lastReply.nodeCounts()['eu']
			apNodes = lastReply.nodeCounts()['ap']

			profit = profit + replies[i].profitEarned()
			#print "Turn " + str(i) + "    " + str(replies[i]["ServerState"]["ProfitEarned"]) + "   " + str(profit)

		lastReply = replies[length-1]

		#average input for each region
		naInput = naInput/15  
		euInput = euInput/15 
		apInput = apInput/15 

		#average succeded from each region
		naSucceeded = naSucceeded/15  
		euSucceeded = euSucceeded/15 
		apSucceeded = apSucceeded/15 

		#average executed for each region
		naExecuted = naExecuted/15  
		euExecuted = euExecuted/15 
		apExecuted = apExecuted/15 

		#total profit info
		profit = profit/15
		bank = lastReply.profitAccumulated()

		turnNo = lastReply.turnNo()

		print "Turn: " + str(turnNo)
		print "[NA]  Nodes: " + str(naNodes) + ", Input: " + str(naInput) + ", Executed: " + str(naExecuted) + ", Succeeded: " + str(naSucceeded)
		print "[EU]  Nodes: " + str(euNodes) + ", Input: " + str(euInput) + ", Executed: " + str(euExecuted) + ", Succeeded: " + str(euSucceeded)
		print "[AP]  Nodes: " + str(apNodes) + ", Input: " + str(apInput) + ", Executed: " + str(apExecuted) + ", Succeeded: " + str(apSucceeded)
		print "Total profit $"+str(bank) + "     Average turn profit $" + str(profit)
		print " "


	reply = jDict.getGeneratedJSONPostData()
	return reply



