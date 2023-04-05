import csv
import numpy as np;
from multiprocessing.connection import answer_challenge
import datetime as dt 

incoming_calls = []
answer_calls = []
abandonded_calls = []
times = []
avgCalls = -1
avgAnswers = -1
avgAbandoned = -1
totalHours = 6

def timeTaken(time):
    time = str(time)
    numbers = time.split(":")
    hours = int(numbers[0])
    minutes = int(numbers[1])
    seconds = int(numbers[2])
    return hours*3600 + minutes*60 + seconds

#  CSV FORMAT
#  Index,Incoming Calls,Answered Calls,Answer Rate,Abandoned Calls,Answer Speed (AVG),Talk Duration (AVG),Waiting Time (AVG),Service Level (20 Seconds)
#  Open sample data file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        incoming_calls.append(int(row[1]))
        answer_calls.append(int(row[2]))
        abandonded_calls.append(int(row[4]))
        timeInSeconds = timeTaken(row[6])
        times.append(timeInSeconds)


def getAverage(list):
    totalDays = 0
    totalValue = 0
    for number in list:
        totalDays = totalDays + 1
        totalValue = totalValue + number
    return totalValue / totalDays

avgCalls = getAverage(incoming_calls)
avgAnswers = getAverage(answer_calls)
avgAbandoned = getAverage(abandonded_calls)
avgCallLength = getAverage(times)


def callsPerDay():
    totalSeconds = totalHours * 3600
    totalCallsInSeconds = 0
    totalCalls = 0
    while (totalSeconds > totalCallsInSeconds):
        totalCallsInSeconds += np.random.poisson(avgCallLength)
        totalCalls += 1
    
    print(totalCalls)
    print(totalCallsInSeconds / 3600)


print(avgCallLength)

print (np.random.poisson(avgCallLength, 10))
print(avgCalls)
print(avgAnswers)
print(avgAbandoned)
callsPerDay()