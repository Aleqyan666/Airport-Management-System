import csv
import os
import sys

file_path_trips = "mock_trips.csv"
file_path_passengers = "mock_passengers.csv"
file_path_staff = "mock_staff.csv"
file_path_login =  "login.csv"
file_path_destination = "destinationData.pbix"
file_path_origin = "originData.pbix"

"""
Adding a trip to a dataset of trips. The function takes origin, destination, startDate, endDate as arguments.
Afterwards, input is being added to the file in form of row. 
"""
def addTrip(origin, destination, startDate, endDate):
   with open(file_path_trips, 'r') as file:
        reader = csv.reader(file)
        line_count = len(list(reader))

   with open(file_path_trips, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        input = [line_count, origin, destination, startDate, endDate, "false"]
        csv_writer.writerow(input)
        print(f'The following trip was scheduled {input}')


"""
Deleting a trip from a dataset of trips. The function takes a id of a trip as a argument.
Afterwards, it deletes thh given trip from the dataset.
"""
def deleteTripById(id):
    with open(file_path_trips, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        del data[id]
        print(f'Trip with id {id} was deleted')

    with open(file_path_trips, 'w', newline='') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerows(data)

"""
Displays all trips
"""
def displayTrips():
    with open(file_path_trips, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

"""
Displays all canceled trips
"""
def displayCanceledTrips():
    with open(file_path_trips, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print("List of canceled trips: ")
        for i in range (count):
            if data[i][5] == "true":
                print(data[i])            
    with open(file_path_trips, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


"""
Canceling a trip from a dataset of trips. The function takes a id of a trip as a argument.
Afterwards, it deletes sets the status of the given trip to "canceled" in the dataset.
"""
def cancelTripById(id):
    with open(file_path_trips, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        if id > 0 and  id < len(data):
            data[id][5] = "true"
            print(f'Trip with id {id} was canceled')    
    with open(file_path_trips, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Searching a trip in a dataset of trips. The function takes origin as an argument.
Afterwards, the function prints all trips with the given origin.
"""
def searchTripByOrigin(origin):
    with open(file_path_trips, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of trips with an origin {origin}:')
        for i in range (count):
            if data[i][1] == origin:
                print(data[i])            
    with open(file_path_trips, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Searching a trip in a dataset of trips. The function takes destination as an argument.
Afterwards, the function prints all trips with the given destination.
"""
def searchTripByDestination(destination):
    with open(file_path_trips, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of trips with a destination {destination}:')
        for i in range (count):
            if data[i][2] == destination:
                print(data[i])            
    with open(file_path_trips, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Adding a passenger to a dataset of passengers. The function takes first name, last name, email, gender, nation as arguments.
Afterwards, input is being added to the file in form of row. 
"""
def addPassenger(firstName,lastName,email,gender,nation):
    with open(file_path_passengers, 'r') as file:
        reader = csv.reader(file)
        line_count = len(list(reader))

    with open(file_path_passengers, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        input = [line_count,firstName,lastName,email,gender,nation]
        csv_writer.writerow(input)
        print(f'The following passenger was added {input}')

"""
Deleting a passenger from a dataset of passengers. The function takes a id of a passenger as an argument.
Afterwards, it deletes the given passenger from the dataset.
"""
def deletePassengerById(id):
    with open(file_path_passengers, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        del data[id]
        print(f'Passenger with id {id} was removed')

    with open(file_path_passengers, 'w', newline='') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerows(data)

"""
Searching a passenger in a dataset of passengers. The function takes first name as an argument.
Afterwards, the function prints all passengers with the given first name.
"""
def searchPassengerByName(firstName):
    with open(file_path_passengers, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of passengers with a name {firstName}:')
        for i in range (count):
            if data[i][1] == firstName:
                print(data[i])            
    with open(file_path_passengers, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Searching a passenger in a dataset of passengers. The function takes last name as an argument.
Afterwards, the function prints all passengers with the given last name.
"""
def searchPassengerByLastName(lastName):
    with open(file_path_passengers, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of passengers with a last name {lastName}:')
        for i in range (count - 1):
            if data[i][2] == lastName:
                print(data[i])            
    with open(file_path_passengers, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Searching a passenger in a dataset of passengers. The function takes nationality as an argument.
Afterwards, the function prints all passengers with the given nationality.
"""
def searchPassengerByNation(nation):
    with open(file_path_passengers, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of passengers from {nation}:')
        for i in range (count):
            if data[i][5] == nation:
                print(data[i])            
    with open(file_path_passengers, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Adding a staff member to a dataset of staff. The function takes first name, last name, email, gender as arguments.
Afterwards, input is being added to the file in form of row. 
"""
def addStaff(firstName,lastName,email,gender):
    with open(file_path_staff, 'r') as file:
        reader = csv.reader(file)
        line_count = len(list(reader))

    with open(file_path_staff, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        input = [line_count,firstName,lastName,email,gender]
        csv_writer.writerow(input)
        print(f'The following staff member was added {input}')


"""
Deleting a staff member from a dataset of staff. The function takes a id of a staff member as an argument.
Afterwards, it deletes the given staff member from the dataset.
"""
def deleteStaffById(id):
    with open(file_path_staff, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        del data[id]
        print(f'Staff member with id {id} was removed')

    with open(file_path_staff, 'w', newline='') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerows(data)

"""
Deleting a staff member from a dataset of staff. The function takes a first name and a last name of a staff member as  arguments.
Afterwards, it deletes the given staff member from the dataset.
"""
def deleteStaffByName(firstName, lastName):
    with open(file_path_staff, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        for i in range(count):
            if data[i][1] == firstName and data[i][2] == lastName:
                print(f'Staff member with id {i} was removed')
                del data[i]
                return
       

    with open(file_path_staff, 'w', newline='') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerows(data)

"""
Searching a staff member in a dataset of trips. The function takes first name and last name asarguments.
Afterwards, the function prints all staff members with the given names.
"""
def searchStaffByName(firstName, lastName):
    with open(file_path_staff, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        count = len(data)
        print(f'List of staff members with a  name {firstName} {lastName}:')
        for i in range (count - 1):
            if data[i][1] == firstName and data[i][2] == lastName:
                print(data[i])            
    with open(file_path_staff, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

"""
Displays all members of the staff
"""
def displayStaff():
    with open(file_path_staff, 'r') as file:
        reader = csv.reader(file)
        print("List of staff members: ")
        for row in reader:
            print(row)

"""
Accesses a PowerBI document that presents data on the occurrences of flights originating from a specified location.
"""
def tripOriginStatistics():
    power_bi_file_path = file_path_origin

    if os.path.exists(power_bi_file_path):
        os.startfile(power_bi_file_path)
    else:
        print("File doesn't exist")

"""
Accesses a PowerBI document that presents data on the occurrences of flights arriving in a specified location.
"""
def tripDestinationStatistics():
    power_bi_file_path = file_path_destination

    if os.path.exists(power_bi_file_path):
        os.startfile(power_bi_file_path)
    else:
        print("File doesn't exist")

"""
User inputs the username and password, if those match the ones in the datasets, login is succesfull
"""
def login(username, password):
    with open(file_path_login, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        if data[0][0] == username and data[0][1] == password:
            print(f'User with a username {username} just logged in:')
        else: 
            print("Program stopped")
            sys.exit()

    with open(file_path_login, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
