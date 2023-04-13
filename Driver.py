import csv
from multiprocessing.connection import answer_challenge
import CustomerClass
import random


## take in time string formatted as 00:00:00 and convert it to total seconds
def toSeconds(time):
    time = str(time)
    numbers = time.split(":")
    hours = int(numbers[0])
    minutes = int(numbers[1])
    seconds = int(numbers[2])
    return hours*3600 + minutes*60 + seconds

def randomD(min, max):
    return random.uniform(min, max)
incoming_calls = []
answer_calls = []
abandonded_calls = []
answer_speed = []

#  CSV FORMAT
#  Index,Incoming Calls,Answered Calls,Answer Rate,Abandoned Calls,Answer Speed (AVG),Talk Duration (AVG),Waiting Time (AVG),Service Level (20 Seconds)
#  Open sample data file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    #next(reader)

    for row in reader:
        incoming_calls.append(int(row[1]))
        answer_calls.append(int(row[2]))
        abandonded_calls.append(int(row[4]))
        answer_speed.append(toSeconds(row[5]))

avg = sum(abandonded_calls) / len(abandonded_calls)
numofA = len(abandonded_calls)
answerSpeedSecondList = list()
rand = random.randint(0, max(answer_speed))
print(rand)

customerEntered = 0.0
customerList = []
for i in range(20):
    num = random.randint(0, 4)
    if num == 4:
        cus = CustomerClass.Customer(i, randomD(0.2, 1.3) + customerEntered, randomD(2.7,3.1))
    else:
        cus = CustomerClass.Customer(i, randomD(0.2, 1.3) + customerEntered, randomD(1.0, 2.6))
    customerEntered = cus.getEntryTime()
    customerList.append(cus)

print(customerList)
customerList[0].setServiceStartTime(customerList[0].getEntryTime())
customerList[0].setServiceEndTime(customerList[0].getServiceStartTime() + customerList[0].getServiceTime())
print(customerList[0].toString())

for i in range(1, len(customerList)):
    cus = customerList[i]
    prevCus = customerList[i-1]
    
    cus.setServiceStartTime(prevCus.getServiceEndTime())
    cus.setServiceEndTime(cus.getServiceStartTime() + cus.getServiceTime())
    print(cus.toString())


