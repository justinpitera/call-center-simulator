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


selection = int(input())
print(answered_calls[selection]/incoming_calls[selection])
print(abandonded_calls[selection]/incoming_calls[selection])
print("Average answer speed: " + answer_speed[selection])
