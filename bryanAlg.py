def algorithm(jDict, replies):
	naWebServers = 0
	euWebServers = 0
	apWebServers = 0

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

		if(naRateOfChange > 0.5):
			naWebServers++;
		else if(naRateOfChange < -0.5):
			naWebServers++;

		if(euRateOfChange > 0.5):
			euWebServers++;
		else if(euRateOfChange < -0.5):
			euWebServers++;

		if(apRateOfChange > 0.5):
			apWebServers++;
		else if(apRateOfChange < -0.5):
			apWebServers++;


		
	
	reply = jDict.getGeneratedJSONPostData()

	return reply