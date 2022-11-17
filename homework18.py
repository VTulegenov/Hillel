import json
import csv
import random


with open('task_1.json') as write_file:
    input_data = json.load(write_file)


with open("task_1.csv", mode="w", encoding='utf-8') as w_file_csv:
    file_writer = csv.writer(w_file_csv, delimiter=",")
    file_writer.writerow(['id', 'name', 'age', 'phone'])
    r_int = lambda: random.randint(0, 9)

    for item_key in input_data:
        phone = f'09{r_int()}-{r_int()}{r_int()}-{r_int()}{r_int()}'
        file_writer.writerow(
            [item_key, input_data[item_key][0], input_data[item_key][1], phone]
        )
