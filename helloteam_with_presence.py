attendees = [
    {'name': 'John', 'present': True},
    {'name': 'Mary', 'present': False},
    {'name': 'Bob', 'present': True},
    {'name': 'Sarah', 'present': True},
    {'name': 'Ali', 'present': False},
]

for attendee in attendees:
    if attendee['present']:
        print('Hello', attendee['name'])
    else:
        print(f'Goodbye {attendee["name"]}')
