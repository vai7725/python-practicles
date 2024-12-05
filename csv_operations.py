import csv

# Creating and writing to a CSV file
data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 22, "Chicago"]
]

with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file and loading into a list of dictionaries
loaded_data = []
with open('people.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        loaded_data.append(row)

print(loaded_data)
