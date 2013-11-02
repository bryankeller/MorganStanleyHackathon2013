def algorithm(jDict, replies):
	naRateOfChange = 0
	euRateOfChange = 0
	apRateOfChange = 0

	minuteInterval = 60;

	if(len(replies) % minuteInterval == 0 and len(replies) > 0):
		for num in range(len(replies) - (minuteInterval + 1), len(replies) - 1):
			naRateOfChange += float(replies[num+1].executedNums()["na"]) - float(replies[num].executedNums()["na"])
			euRateOfChange += float(replies[num+1].executedNums()["eu"]) - float(replies[num].executedNums()["eu"])
			apRateOfChange += float(replies[num+1].executedNums()["ap"]) - float(replies[num].executedNums()["ap"])

		naRateOfChange /= minuteInterval - 1
		euRateOfChange /= minuteInterval - 1
		apRateOfChange /= minuteInterval - 1

		print "NA Executed Transactions Rate of Change: " + str(naRateOfChange)
		print "EU Executed Transactions Rate of Change: " + str(euRateOfChange)
		print "AP Executed Transactions Rate of Change: " + str(apRateOfChange)
		print "Current Profit: " + str(replies[len(replies) - 1].profitAccumulated())
		# print "Executed: " + str(replies[len(replies) - 1].profitAccumulated())
		# print "Successes: " + str(replies[len(replies) - 1].profitAccumulated())
		print ""
	
	reply = jDict.getGeneratedJSONPostData()

	return reply