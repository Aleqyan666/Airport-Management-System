import administrator as ad
import sys

isRunning = True
options = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
]
count = 0


def main():
    global count
    if count == 0:
        print("Enter the username")
        uname = input()
        print("Enter the password")
        password = input()
        ad.login(uname, password)
        count += 1
    print("A: Add a trip")
    print("B: Delete a trip")
    print("C: Display list of trips")
    print("D: Display list of canceled trips")
    print("E: Cancel a trip")
    print("F: Search Trip using origin")
    print("G: Search Trip using destination")
    print("H: Add a passenger")
    print("I: Delete a passenger")
    print("J: Search a passenger by first name")
    print("K: Search a passenger by lastt name")
    print("L: Search a passenger by nationality")
    print("M: Add a staff member")
    print("N: Delete a staff member")
    print("O: Delete a staff member using name")
    print("P: Search a staff member by full name ")
    print("Q: Terminate/Exit the program")
    print("R: Display list of staff members")
    print("S: Show the most frequent places left")
    print("T: Show the most popular places visited")

    command = input()

    if command == "A":
        print("Enter the origin")
        origin = input()
        print("Enter the destination")
        destination = input()
        print("Enter the starting date of the flight in mm/dd/yyyy format")
        startDate = input()
        print("Enter the ending date of the flight in mm/dd/yyyy format")
        endDate = input()
        ad.addTrip(origin, destination, startDate, endDate)

    elif command == "B":
        print("Enter the trip id")
        id = input()
        ad.deleteTripById(id)

    elif command == "C":
        print("List of trips")
        ad.displayTrips()

    elif command == "D":
        print("List of canceled trips")
        ad.displayCanceledTrips()

    elif command == "E":
        print("Enter a id of a trip to cancel")
        id = input()
        ad.cancelTripById(id)

    elif command == "F":
        print("Enter origin of a trip")
        origin = input()
        ad.searchTripByOrigin(origin)

    elif command == "G":
        print("Enter destination of a trip")
        destination = input()
        ad.searchTripByDestination(destination)

    elif command == "H":
        print("Enter a first name")
        firstName = input()
        print("Enter a last name")
        lastName = input()
        print("Enter a email")
        email = input()
        print("Enter the gender M or F")
        gender = input()
        print("Enter the nationality(example: Russia)")
        nation = input()
        ad.addPassenger(firstName, lastName, email, gender, nation)

    elif command == "I":
        print("Enter a id of a passenger to delete")
        id = input()
        ad.deletePassengerById(id)

    elif command == "J":
        print("Enter a first name to search")
        firstName = input()
        ad.searchPassengerByName(firstName)

    elif command == "K":
        print("Enter a last name to search")
        lastName = input()
        ad.searchPassengerByLastName(lastName)

    elif command == "L":
        print("Enter a nationality to search(example: Russia)")
        nation = input()
        ad.searchPassengerByNation(nation)

    elif command == "M":
        print("Enter a first name")
        firstName = input()
        print("Enter a last name")
        lastName = input()
        print("Enter a email")
        email = input()
        print("Enter the gender")
        gender = input()
        ad.addStaff(firstName, lastName, email, gender)

    elif command == "N":
        print("Enter a id of a staff member to delete")
        id = input()
        ad.deleteStaffById(id)

    elif command == "O":
        print("Enter a first name")
        firstName = input()
        print("Enter a last name")
        lastName = input()
        ad.deleteStaffByName(firstName, lastName)

    elif command == "P":
        print("Enter a first name")
        firstName = input()
        print("Enter a last name")
        lastName = input()
        ad.searchStaffByName(firstName, lastName)

    elif command == "R":
        print("List of staff members")
        ad.displayStaff()

    elif command == "S":
        print("Most frequent places left")
        ad.tripOriginStatistics()

    elif command == "T":
        print("Most popular placed arrived")
        ad.tripDestinationStatistics()

    elif command == "Q":
        print("Programmed stopped")
        sys.exit()

    elif command not in options:
        print("Invalid action. Please choose any uppercase letter from A-T")


while isRunning:
    main()
