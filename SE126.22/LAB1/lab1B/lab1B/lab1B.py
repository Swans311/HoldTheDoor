#David Swansey SE126.22 LAB 1B
#variable dictionary
#answer= answer while loop control
#roomcap= room capacity
#attending= people attending
#overage= more attending than room cap
#under= more room cap than attending
#general setup

#fire violation program
#accepts room capacity from user
#accepts people attending from user
#calculates if it is okay for all those people to be in a small and enclosed area
#how many people must be excluded if there is an overage
#as many rooms as they want
#only accepts lowercase y or n
roomcap=0
attending=0
overage=0
under=0
print("Welcome to the fire infraction checker...")

def initialize(): #did not end up using here
    given= "l"
    while given != "y" or given != "Y" or given != "n" or given != "N":
        given= input("Would you like to check a room? [y/n] :")
        if given == "y" or given == "Y" or given == "N" or given == "n":
            return given
#answer = initialize()
answer= "y"
while answer == "y" or answer == "Y":  # or answer == "n" or answer == "N"
    roomcap= int(input("\nHow many people can fit in the room?: ")) #how many people can fit inside the meeting hall
    attending= int(input("\nHow many people are going to be in the room?: ")) #how many people want to attend the meeting
    if attending > roomcap: #if there are too many people
        overage= attending - roomcap #math
        print("\nThere are", overage, "more people than there should be.")
        print("FIRE INFRACTION") #don't make me call Smokey the Bear
    elif roomcap > attending: #if there can be people added
        under= roomcap - attending #more math
        print("\nThere are", under, "people that can still fit into the meeting")
        print("NO INFRACTIONS")
    elif roomcap == attending: #even amount of going vs can fit
        print("\nThere is an equal amount of people to capacity")
        print("Don't add anyone else and there won't be an issue")
    answer=input("\n Would you like to check another room? [y/n]:") #possibly re-enter while loop
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N": #if you punks want to enter something that is NOT an acceptable response
            answer=input("\n Would you like to check another room? [y/n]:") #keep asking
    if answer != "n" and answer != "N"and answer != "y" and answer != "Y":
            answer= input("\n Would you like to check another room? [y/n]") #keep asking
    elif answer == "y" or answer == "Y":
            answer= "y" #we will accept that as an answer
    elif answer == "n" or answer == "N":
            input("Thanks for coming, have a fire free day.") #pre-goodbye message
            answer= "n" #acceptable answer, exit loop
print("Have fun and be safe") #goodbye