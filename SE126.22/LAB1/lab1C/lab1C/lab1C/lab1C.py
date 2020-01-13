#David Swansey SE126.22 LAB 1C
#variable dictionary
#answer= answer while loop control
#roomcap= room capacity
#attending= people attending
#overage= more attending than room cap
#under= more room cap than attending

#general setup
roomcap=0
attending=0
overage=0
under=0
print("Welcome to the fire infraction checker...") #welcome to the game

def initialize(): #reenter and control loop
    given= "l"
    while given != "y" or given != "Y" or given != "n" or given != "N": #we dont want any other answers than y's and n's
        given= input("Would you like to check a room? [y/n] :") #reenter while loop
        if given == "y" or given == "Y" or given == "N" or given == "n":
            return given #gimme that back

def capacity(): #how many people can go
    cap=int(input("\nHow many people can fit in the room?: "))
    return cap

def attendees(): #how many people are going
    attend= int(input("\nHow many people are going to be at the meeting?: "))
    return attend #giving value back to variable

def register(c, a): # overage calc
    tot= a - c
    return tot #passing value back to variable assigned



#answer= initialize() used previously, but heard that it was easier to use this line of code and we were NOT allowed to use break
answer ="y" #enter while loop
while answer == "y" or answer == "Y": # or answer == "n" or answer == "N"
#    roomcap= int(input("\nHow many people can fit in the room?: ")) former line used
    roomcap= capacity()
#    attending= int(input("\nHow many people are going to be in the room?: ")) replaced line
    attending= attendees()
    if attending > roomcap: #less than no space available
#        overage= attending - roomcap   replaced line
        overage= register(roomcap, attending) #function math
        print("\nThere are", overage, "more people than there should be.") #get these people out of here
        print("FIRE INFRACTION")
    elif roomcap > attending: #more space available
#        under= roomcap - attending    replaced line
        under= register(attending, roomcap) #function math
        print("\nThere are", under, "people that can still fit into the meeting") #can still squeeze some people in there
        print("NO INFRACTIONS")
    elif roomcap == attending: 
        print("\nThere is an equal amount of people to capacity")
        print("Don't add anyone else and there won't be an issue") #dead even
    answer= initialize() #re-enter while loop
print("Have a fire free day kids!") 
print("Have fun and be safe") #bye kids
