# UMBC Parking Simulator: a text-based simulator that shows how many parking spots are available after a certain time.
#                           Because commuter parking is frustrating and I wanted to show others how stressful it is.
#
# Concepts practiced:
#   - Python classes
#   - utilizing Python libraries
#
# Some issues to fix:
#   - doesn't account for times when classes aren't in session (e.g. early mornings/late evenings, weekends, holidays)
#   - improve white space for a more aesthetically pleasing output
#   - change variable names so they all follow a consistent form (camel case)
#
# Future plans:
#   - do a cute little ascii animation of parking lot being filled
#       - show list being populated with 'X' in random indices
#       - display hours going by
#       - progress bar will no longer be needed once this is implemented
#   - implement a gui app ?!?

import parkinglots
import time
import random
import sys

# if false, keep looking for parking
isParked = False

# used when running simulator
lotlist = [parkinglots.commons, parkinglots.lot1, parkinglots.lot3, parkinglots.lot4, parkinglots.circlestadium, parkinglots.circlepahb, parkinglots.circleapart, parkinglots.lot22, parkinglots.lot23, parkinglots.lot25, parkinglots.stadium, parkinglots.lot27, parkinglots.lot29]

# used for when user is choosing a lot to pick in (indices correspond to their input)
mainlots = [parkinglots.commons, parkinglots.lot1, parkinglots.lot3, parkinglots.lot4, None, None, parkinglots.lot22, parkinglots.lot23, parkinglots.lot25, parkinglots.lot29]
circlelots = [parkinglots.circlestadium, parkinglots.circlepahb, parkinglots.circleapart]
stadiumlots = [parkinglots.stadium, parkinglots.lot27]

lotmenu = "\nPick a parking lot:\n\t1. Commons Garage\n\t2. Lot 1\n\t3. Lot 3\n\t4. Lot 4\n\t5. On the circle\n\t6. Stadium Lot\n\t7. Lot 22\n\t8. Lot 23\n\t9. Lot 25\n\t10. Lot 29\n\nWhere would you like to park? "

circlemenu = "\nThe circle's huge. Pick an area:\n\t1. In between Park Rd and Stadium Lot\n\t2. Next to Performing Arts & Humanity Building\n\t3. By the dorms & apartments\n\nWhere would you like to park? "

stadiummenu = "\nStadium lot has different areas. Pick one:\n\t1. In the parking lot\n\t2. Up the hill (Lot 27)\n\nWhere would you like to park? "

# get a new random seed every time program starts up
random.seed(time.clock());

# populate parking lots based on an rng
def populate(campuslot, isEarly):

    # saving time by not even bothering if lot is already full
    if (campuslot.isFull == True):
        return

    # just using some arbitrary number to use in rng
    earlyspots = campuslot.max - (campuslot.max / 5)

    if (isEarly == True):
        parked = random.randint(0, earlyspots)
    else:
        parked = random.randint(earlyspots, campuslot.max)

    # parking cars in random spots for that authentic feel
    for i in range(0, parked):
        spot = random.randint(0, campuslot.max - 1)
        # if there's already an 'X' at that index, move on
        if (campuslot.lot[spot] == 'X'):
            i += 1
        else:
            campuslot.lot[spot] = 'X'

# populates entire lot array with X's
def forcefill(campuslot):
    for i in range(0, campuslot.max):
        campuslot.lot[i] = 'X'

    campuslot.isFull = True

def openspot(lot):
    isParked = True
    print("\nYou got a spot!\n")
    parkcar(lot)
    printlot(lot)
    # sys.exit(0)

def nospots(lot):
    print("\n" + lot.name + " is full.\n")
    printlot(lot)

# iterates through parking lot array and checks that amount of 'X' is less than or equal to lot's max
def checkfull(campuslot):
    sys.stdout.write("\nChecking " + campuslot.name)
    sys.stdout.flush()

    for i in range(0,3):
        time.sleep(0.3)
        sys.stdout.write('.')
        sys.stdout.flush()

    time.sleep(1)

    if (campuslot.isFull == True):
        nospots(campuslot)
        return

    counter = 0

    for spaces in campuslot.lot:
        if (spaces == 'X'):
            counter += 1

    if (counter >= campuslot.max):
        campuslot.isFull = True

    if (campuslot.isFull == False):
        openspot(campuslot)
    else:
        nospots(campuslot)

# found a non-empty lot, so now it's time to park!
def parkcar(campuslot):
    # find a spot
    parkingspot = random.randint(0, campuslot.max - 1)

    # if it's taken, find another spot
    while (campuslot.lot[parkingspot] == 'X'):
        parkingspot = random.randint(0, campuslot.max - 1)

    isParked = True
    campuslot.lot[parkingspot] = 'O'

# pretty print lot array
def printlot(campuslot):
    for i in range(0, campuslot.max):
        if (i % 20 == 0):
            sys.stdout.write('|')
        sys.stdout.write(campuslot.lot[i] + '|')
        sys.stdout.flush()
        if ((i+1) % 20 == 0):
            print("")

# parking all the virtual cars
def runsimulator(isEarly):
    for lots in lotlist:
        populate(lots, isEarly)

    sys.stdout.write("\nLet's see if you get a spot.\nParking all cars: ")
    sys.stdout.flush()

    # loading bar animation
    for i in range(0,30):
        time.sleep(0.1)
        sys.stdout.write('*')
        sys.stdout.flush()

    print("\n")

# start the day over
def restart():
    for lots in lotlist:
        for i in range(0, lots.max):
            lots.lot[i] = '_'

# an unwanted but sometimes possible occurence
def nohope():
    veryunlucky = str(input("You circled all around campus and didn't find any parking. Try again? (y/n) "))

    if (veryunlucky == "y"):
        circles = -1
        restart()
        return
    elif (veryunlucky == "n"):
        sys.exit(0)

# picking a parking lot to park in
def park(arrival, circles):
    whichLot = int(input(lotmenu))

    if (whichLot == 5):
        circlelot = int(input(circlemenu))
        parkinglot = circlelots[circlelot-1]
    elif (whichLot == 6):
        stadiumlot = int(input(stadiummenu))
        parkinglot = stadiumlots[stadiumlot-1]
    else:
        parkinglot = mainlots[whichLot-1]

    # only run simulator on first circle around campus
    if (circles == 0):
        runsimulator(arrival)
    elif (circles > 30):
        nohope()

    checkfull(parkinglot)

def main():
    # number of times circled around already
    numRuns = 0

    print("\nWelcome to the UMBC parking simulator!")
    parkTime = int(input("What time (0 - 24) are you arriving on campus? "))

    while ((parkTime < 0) or (parkTime > 24)):
        parkTime = int(input("Not a valid time.\nWhat time (0 - 24) are you arriving on campus? "))

    if (parkTime <= 9):
        isEarly = True
        print("\nWow, you're early! Hopefully you'll find prime parking today.")
    elif ((parkTime == 10) or (parkTime == 11)):
        isEarly = False
        forcefill(parkinglots.commons)
        forcefill(parkinglots.lot4)
        print("\nTraffic hold you up? That's okay; there should still be some good spots left.")
    else:
        isEarly = False
        forcefill(parkinglots.commons)
        forcefill(parkinglots.lot1)
        forcefill(parkinglots.lot3)
        forcefill(parkinglots.lot4)
        forcefill(parkinglots.circlepahb)
        forcefill(parkinglots.circlestadium)
        print("\nYou sure took your sweet time to get here. Good luck finding a spot.")

    while (isParked == False):
        park(isEarly, numRuns)
        numRuns += 1

    # checking to see if you're parked
    print("\nThanks for using the UMBC Parking Simulator! Now let's hope you get to class on time.")

main()
