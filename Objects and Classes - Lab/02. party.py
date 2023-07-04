class Person:

    def __init__(self, name):
        self.name = name


class Party:

    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def name_of_attendees(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guest(self):
        return len(self.people)


obj = Party()

while True:
    command = input()
    if command == 'End':
        break
    name = command
    person = Person(name)
    obj.invite(person)
print(f'Going: {obj.name_of_attendees()}')
print(f'Total: {obj.number_of_guest()}')
