# code to find index associated with a key using the
# enumerate function

records = [ ('mikaeel@example.com','Hello world'),
            ('mathers@example.com','Hello to you too'),
            ('shady@example.com','Python is awesome')
            ]

for index, record in enumerate(records):
    key, value = record
    if key == "shady@example.com":
        break

print(records[index])
