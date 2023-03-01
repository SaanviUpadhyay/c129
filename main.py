import csv
data = []
with open("dataset_2.csv" , "r") as f :
    csv_reader = csv.reader(f)

    for row in csv_reader :
        data.append(row)

headers = data[0]
star_data = data[1 : ]

for data_point in star_data :
     data_point[2] = data_point[2].lower()

star_data.sort(key = lambda star_data : star_data[2])

with open("dataset_2_sorted.csv" , "a+") as f :
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)
