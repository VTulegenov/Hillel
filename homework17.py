import json
dict_old = {111111: ('Vlad', 20), 222222: ('Jan', 22), 333333: ('Gus', 45),
            444444: ('Alisher', 33), 555555: ('Lina', 21), 666666: ('Sergio', 38)}

with open('task_1.json', 'w') as write_file:
    json.dump(dict_old, write_file)

