def algorithm(post, replies):
	newPost = JSONPostData()
	lastReply = replies[len(replies)-1]

	#generates a summary report every 15 turns
	turnNo = int(lastReply['ServerState']['TurnNo'])
	newPost.setWebNodeCounts(1,1,1)
	#print "Replies sizeee: "+str(len(replies))
	#print "Turn Nono: "+ str(turnNo)
	if((turnNo%15)==0 and turnNo!=0):
		summary(replies);

	reply = newPost.getGeneratedJSONPostData()
	return reply

def summary(replies):
	#print "Replies size: "+str(len(replies))
	length = len(replies)
	lastReply = replies[length-1]
	naExecuted = euExecuted = apExecuted = naNodes = euNodes = apNodes = profit= 0
	#replies = reversed(replies)
	for i in range(length-15,length):
		naExecuted = naExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsInput"]
		euExecuted = euExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsInput"]
		apExecuted = apExecuted + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsInput"]
		naSucceeded = naSucceeded + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsSucceeded"]
		euSucceeded = euSucceeded + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsSucceeded"]
		apSucceeded = apSucceeded + replies[i]["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsSucceeded"]
		naNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"]
		euNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"]
		apNodes = lastReply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"]
		profit = profit + int(replies[i]["ServerState"]["ProfitEarned"])
		#print "Turn " + str(i) + "    " + str(replies[i]["ServerState"]["ProfitEarned"]) + "   " + str(profit)

	lastReply = replies[length-1]
	naExecuted = naExecuted/15  
	euExecuted = euExecuted/15 
	apExecuted = apExecuted/15 
	profit = profit/15
	bank = lastReply["ServerState"]["ProfitAccumulated"]
	turnNo = int(lastReply['ServerState']['TurnNo'])

	print "Turn: " + str(turnNo)
	print "[NA]  Nodes:" + str(naNodes) + ", Executed: " + str(naExecuted)
	print "[EU]  Nodes:" + str(euNodes) + ", Executed: " + str(euExecuted)
	print "[AP]  Nodes:" + str(apNodes) + ", Executed: " + str(apExecuted)
	print "Total profit $"+str(bank) + "     Average turn profit $" + str(profit)
	print " "


