
def GetStartTimestampFromIndex(TimeStamps, index):
    return TimeStamps[index].split(' - ')[0]

def GetEndTimestampFromIndex(TimeStamps, index): 
    return TimeStamps[index].split(' - ')[1]

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

def GetSecondsBasedOnTimeStamp(timestamp):
    if(len(timestamp.split(':')) < 3):
        Minutes = int(timestamp.split(':')[0])
        Seconds = int(timestamp.split(':')[1])
        return (Seconds + (Minutes*60))
    else:
        Hours = int(timestamp.split(':')[0])
        Minutes = int(timestamp.split(':')[1])
        Seconds = int(timestamp.split(':')[2])
        return (Seconds + (Minutes*60) + (Hours * 60 * 60))


