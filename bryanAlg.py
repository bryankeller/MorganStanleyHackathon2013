def getJavaAdjust(replies):
	# naWebServers = euWebServers = apWebServers = 0
	naJavaServers = euJavaServers = apJavaServers = 0
	# naDbServers = euDbServers = apDbServers = 0

	# naWebRateOfChange  = euWebRateOfChange = apWebRateOfChange = 0
	naJavaRateOfChange = euJavaRateOfChange = apJavaRateOfChange = 0
	# naDbRateOfChange = euDbRateOfChange = apDbRateOfChange = 0

	minuteInterval = 60

	if(len(replies) % minuteInterval == 0 and len(replies) > 0):
		for num in range(len(replies) - (minuteInterval + 1), len(replies) - 1):
			# naWebRateOfChange += float(replies[num+1].executedNums("WEB")["na"]) - float(replies[num].executedNums("WEB")["na"])
			# euWebRateOfChange += float(replies[num+1].executedNums("WEB")["eu"]) - float(replies[num].executedNums("WEB")["eu"])
			# apWebRateOfChange += float(replies[num+1].executedNums("WEB")["ap"]) - float(replies[num].executedNums("WEB")["ap"])

			naJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["na"]) - float(replies[num].executedNums("JAVA")["na"])
			euJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["eu"]) - float(replies[num].executedNums("JAVA")["eu"])
			apJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["ap"]) - float(replies[num].executedNums("JAVA")["ap"])

			# naDbRateOfChange += float(replies[num+1].executedNums("DB")["na"]) - float(replies[num].executedNums("DB")["na"])
			# euDbRateOfChange += float(replies[num+1].executedNums("DB")["eu"]) - float(replies[num].executedNums("DB")["eu"])
			# apDbRateOfChange += float(replies[num+1].executedNums("DB")["ap"]) - float(replies[num].executedNums("DB")["ap"])

		# naWebRateOfChange /= minuteInterval - 1
		# euWebRateOfChange /= minuteInterval - 1
		# apWebRateOfChange /= minuteInterval - 1
		# if(naWebRateOfChange > 0.5):
		# 	naWebServers = 1
		# elif(naWebRateOfChange < -0.5):
		# 	naWebServers = -1

		# if(euWebRateOfChange > 0.5):
		# 	euWebServers = 1
		# elif(euWebRateOfChange < -0.5):
		# 	euWebServers = -1

		# if(apWebRateOfChange > 0.5):
		# 	apWebServers = 1
		# elif(apWebRateOfChange < -0.5):
		# 	apWebServers = -1
		# jDict.setWebNodeCounts(naWebServers, euWebServers, apWebServers)

		naJavaRateOfChange /= minuteInterval - 1
		euJavaRateOfChange /= minuteInterval - 1
		apJavaRateOfChange /= minuteInterval - 1
		if(naJavaRateOfChange > 1.0):
			naJavaServers = 1
		elif(naJavaRateOfChange < -1.0):
			naJavaServers = -1

		if(euJavaRateOfChange > 1.0):
			euJavaServers = 1
		elif(euJavaRateOfChange < -1.0):
			euJavaServers = -1

		if(apJavaRateOfChange > 1.0):
			apJavaServers = 1
		elif(apJavaRateOfChange < -1.0):
			apJavaServers = -1

	return (naJavaServers, euJavaServers, apJavaServers)

		# naDbRateOfChange /= minuteInterval - 1
		# euDbRateOfChange /= minuteInterval - 1
		# apDbRateOfChange /= minuteInterval - 1
		# if(naDbRateOfChange > 1.5):
		# 	naDbServers = 1
		# elif(naDbRateOfChange < -1.5):
		# 	naDbServers = -1

		# if(euDbRateOfChange > 1.5):
		# 	euDbServers = 1
		# elif(euDbRateOfChange < -1.5):
		# 	euDbServers = -1

		# if(apDbRateOfChange > 1.5):
		# 	apDbServers = 1
		# elif(apDbRateOfChange < -1.5):
		# 	apDbServers = -1
		# jDict.setDBNodeCounts(naDbServers, euDbServers, apDbServers)

	# 	print "Turn Number: " + str(replies[len(replies) - 1].turnNo()) + "     Accumulated Profit: $" + str(replies[len(replies) - 1].profitAccumulated()) + "     Current Profit: $" + str(replies[len(replies) - 1].profitEarned())
		
	
	# reply = jDict.getGeneratedJSONPostData()

	# return reply