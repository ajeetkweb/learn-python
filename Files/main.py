"""
   File Handling in Python

# Python File Open
   f = open(filename, mode)
"""



# Open and read a file line by line
file = open('hello.txt', 'r')
for line in file:
    print(line)



# Open and read a file
print('Open and read a file-----')
with open('hello.txt', 'r') as file:
    content = file.read()
    print(content)


# Open and read a CSV file
print(' Open and read a CSV file......................')
import csv
with open('continent.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)



# Open and write to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', '30', 'New York'])
    writer.writerow(['Ajeet kumar', '34', 'Hyderabad'])



# Open and read a JSON file
import json
with open('employee.json', 'r') as file:
    data = json.load(file)
    print(data)





# Open and write to a JSON file
import json
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('example.json', 'w') as file:
    json.dump(data, file)
















  