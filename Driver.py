import csv
from multiprocessing.connection import answer_challenge


incoming_calls = []
answer_calls = []
abandonded_calls = []

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



print(incoming_calls)
print(answer_calls)
print(abandonded_calls)