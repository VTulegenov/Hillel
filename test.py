import json
data = {111111: ('Sam', 42), 100003: ('Tom', 12), 222043: ('Adam', 69),
        679432: ('Jasy', 25), 980451: ('Kim', 33), 666740: ('Jasy', 15)}

with open('file_json.json', 'w') as file_json:
    json.dump(data, file_json)


