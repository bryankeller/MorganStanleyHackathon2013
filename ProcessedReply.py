class ProcessedReply:

	reply = []

	def __init__(self, currentReply):
		self.reply = currentReply

	def successNums(self, serverType):
		naSuccesses = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["NA"]["NoOfTransactionsSuceeded"]
		euSuccesses = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["EU"]["NoOfTransactionsSuceeded"]
		apSuccesses = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["AP"]["NoOfTransactionsSuceeded"]
		return {'na' : naSuccesses, 'eu' : euSuccesses, 'ap' : apSuccesses}

	def nodeCounts(self, serverType):
		naNodes = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["NA"]["NodeCount"]
		euNodes = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["EU"]["NodeCount"]
		apNodes = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["AP"]["NodeCount"]
		return {'na' : naNodes, 'eu' : euNodes, 'ap' : apNodes}

	def executedNums(self, serverType):
		naTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["NA"]["NoOfTransactionsExecuted"]
		euTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["EU"]["NoOfTransactionsExecuted"]
		apTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["AP"]["NoOfTransactionsExecuted"]
		return {'na' : naTran, 'eu' : euTran, 'ap' : apTran}

	def inputNums(self, serverType):
		naTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["NA"]["NoOfTransactionsInput"]
		euTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["EU"]["NoOfTransactionsInput"]
		apTran = self.reply["ServerState"]["ServerTiers"][serverType]["ServerRegions"]["AP"]["NoOfTransactionsInput"]
		return {'na' : naTran, 'eu' : euTran, 'ap' : apTran}

	def upperLimit(self, serverType):
		return self.reply["ServerState"]["ServerTiers"][serverType]["ServerPerformance"]["CapactityLevels"][2]["UpperLimit"]

	def turnNo(self):
		return self.reply['ServerState']['TurnNo']

	def error(self):
		return self.reply['Error']

	def profitAccumulated(self):
		return self.reply['ServerState']['ProfitAccumulated']

	def profitEarned(self):
		return self.reply['ServerState']['ProfitEarned']

	# --- Print stuff ----

	def printStats(self):
		print turnNo(reply)
		print "------------------"
		executed = executedNums(reply)
		successes = successNums(reply)
		nodes = nodeCounts(reply)

		print "[NA] Nodes: " + str(nodes['na']) + " Executed:" + str(executed['na']) + ", Successes: " + str(successes['na'])
		print "[EU] Nodes: " + str(nodes['eu']) + " Executed:" + str(executed['eu']) + ", Successes: " + str(successes['eu'])
		print "[AP] Nodes: " + str(nodes['ap']) + " Executed:" + str(executed['ap']) + ", Successes: " + str(successes['ap'])
		print "  "


	#idk what this does so I left it
	def quickInfo(self, replyDict):
		print "Turn: "+str(turnNo(replyDict))
		print "Turn Profit: $"+str(profitEarned(replyDict))
		print "Bankroll: $"+str(profitAccumulated(replyDict))
		if error(replyDict) != None:
			print "ERROR: "+str(error(replyDict))
		print "-------------------"