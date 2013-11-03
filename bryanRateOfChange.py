def getJavaRateOfChange(replies):
	naJavaRateOfChange = euJavaRateOfChange = apJavaRateOfChange = 0

	for num in range(0, len(replies) - 2):
		naJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["na"]) - float(replies[num].executedNums("JAVA")["na"])
		euJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["eu"]) - float(replies[num].executedNums("JAVA")["eu"])
		apJavaRateOfChange += float(replies[num+1].executedNums("JAVA")["ap"]) - float(replies[num].executedNums("JAVA")["ap"])

	naJavaRateOfChange /= len(replies) - 1
	euJavaRateOfChange /= len(replies) - 1
	apJavaRateOfChange /= len(replies) - 1

	return {'na' : naJavaRateOfChange, 'eu' : euJavaRateOfChange, 'ap' : apJavaRateOfChange}