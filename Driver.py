import csv
from io import StringIO
from multiprocessing.connection import answer_challenge
from os import system
from sre_constants import IN

incoming_calls = []
answered_calls = []
abandonded_calls = []
answer_speed = []

#  CSV FORMAT
#    0          1             2             3            4               5                    6                   7                    8
#  Index,Incoming Calls,Answered Calls,Answer Rate,Abandoned Calls,Answer Speed (AVG),Talk Duration (AVG),Waiting Time (AVG),Service Level (20 Seconds)
#  Open sample data file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        incoming_calls.append(int(row[1]))
        answered_calls.append(int(row[2]))
        abandonded_calls.append(int(row[4]))
        answer_speed.append((row[5]))

print("Input a day to view: ")
day = int(input())
answered_calls_percent = str(answered_calls[day]/incoming_calls[day] * 100)
abandonded_calls_percent = str(abandonded_calls[day]/incoming_calls[day] * 100)
print("Day: " + str(day))
print("Incoming Calls: " + str(incoming_calls[day]))
print("Answered Calls: " + str(answered_calls[day]))
print("Abandoned Calls: " + str(abandonded_calls[day]))
print("Average answer speed: " + answer_speed[day])
print("Answered Calls (%): " + answered_calls_percent + " %")
print("Abandonded Calls (%): " + abandonded_calls_percent + " %")

