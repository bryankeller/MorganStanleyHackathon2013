def algorithm(jDict, replies):
	naRateOfChange = 0
	euRateOfChange = 0
	apRateOfChange = 0

	# print replies[0].executedNums()
	if(len(replies) % 15 == 0 and len(replies) > 0):
		for num in range(len(replies) - 16, len(replies) - 1):
			naRateOfChange += float(replies[num+1].executedNums()["na"]) - float(replies[num].executedNums()["na"])
			euRateOfChange += float(replies[num+1].executedNums()["eu"]) - float(replies[num].executedNums()["eu"])
			apRateOfChange += float(replies[num+1].executedNums()["ap"]) - float(replies[num].executedNums()["ap"])

		naRateOfChange /= 14.00
		euRateOfChange /= 14.00
		apRateOfChange /= 14.00

		print "NA Executed Transactions Rate of Change: " + str(naRateOfChange)
		print "EU Executed Transactions Rate of Change: " + str(euRateOfChange)
		print "AP Executed Transactions Rate of Change: " + str(apRateOfChange)
		print "Current Profit: " + str(replies[len(replies) - 1].profitAccumulated())
		# print "Executed: " + str(replies[len(replies) - 1].profitAccumulated())
		# print "Successes: " + str(replies[len(replies) - 1].profitAccumulated())
		print ""
	
	reply = jDict.getGeneratedJSONPostData()

	return reply