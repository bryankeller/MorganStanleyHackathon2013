
def successNums(reply):
		naSuccesses = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsSuceeded"]
		euSuccesses = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsSuceeded"]
		apSuccesses = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsSuceeded"]
		return {'na' : naSuccesses, 'eu' : euSuccesses, 'ap' : apSuccesses}

def nodeCounts(reply):
		naNodes = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"]
		euNodes = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"]
		apNodes = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"]
		return {'na' : naNodes, 'eu' : euNodes, 'ap' : apNodes}

def executedNums(reply):
		naTran = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["NA"]["NoOfTransactionsExecuted"]
		euTran = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["EU"]["NoOfTransactionsExecuted"]
		apTran = reply["ServerState"]["ServerTiers"]["WEB"]["ServerRegions"]["AP"]["NoOfTransactionsExecuted"]
		return {'na' : naTran, 'eu' : euTran, 'ap' : apTran}

def turnNo(reply):
	return reply['ServerState']['TurnNo']

def error(reply):
	return reply['Error']

def profitAccumulated(reply):
	return reply['ServerState']['ProfitAccumulated']

def profitEarned(reply):
	return reply['ServerState']['ProfitEarned']

# --- Print stuff ----

def printStats(reply):
	print turnNo(reply)
	print "------------------"
	executed = executedNums(reply)
	successes = successNums(reply)
	nodes = nodeCounts(reply)

	print "[NA] Nodes: " + str(nodes['na']) + " Executed:" + str(executed['na']) + ", Successes: " + str(successes['na'])
	print "[EU] Nodes: " + str(nodes['eu']) + " Executed:" + str(executed['eu']) + ", Successes: " + str(successes['eu'])
	print "[AP] Nodes: " + str(nodes['ap']) + " Executed:" + str(executed['ap']) + ", Successes: " + str(successes['ap'])
	print "  "


def quickInfo(replyDict):
	print "Turn: "+str(turnNo(replyDict))
	print "Turn Profit: $"+str(profitEarned(replyDict))
	print "Bankroll: $"+str(profitAccumulated(replyDict))
	if error(replyDict) != None:
		print "ERROR: "+str(error(replyDict))
	print "-------------------"