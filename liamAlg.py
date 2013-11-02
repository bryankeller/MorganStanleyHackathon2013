import bryanAlg
import evanAlg

def algorithm(post, replies):

	post = bryanAlg.algorithm(post, replies)
	post = evanAlg.algorithm(post, replies)


	# naRateOfChange = 0
	# euRateOfChange = 0
	# apRateOfChange = 0

	# minuteInterval = 60;

	# if(len(replies) % minuteInterval == 0 and len(replies) > 0):
	# 	for num in range(len(replies) - (minuteInterval + 1), len(replies) - 1):
	# 		naRateOfChange += replies[num+1].executedNums()["na"] - replies[num].executedNums()["na"]
	# 		euRateOfChange += replies[num+1].executedNums()["eu"] - replies[num].executedNums()["eu"]
	# 		apRateOfChange += replies[num+1].executedNums()["ap"] - replies[num].executedNums()["ap"]

	# 	naRateOfChange /= minuteInterval - 1
	# 	euRateOfChange /= minuteInterval - 1
	# 	apRateOfChange /= minuteInterval - 1

	# 	print "Turn: " + str(replies[num+1].turnNo())
	# 	print "NA Executed Transactions Rate of Change: " + str(naRateOfChange)
	# 	print "EU Executed Transactions Rate of Change: " + str(euRateOfChange)
	# 	print "AP Executed Transactions Rate of Change: " + str(apRateOfChange)
	# 	print "Current Profit: " + str(replies[len(replies) - 1].profitAccumulated())
	return post.getGeneratedJSONPostData()
