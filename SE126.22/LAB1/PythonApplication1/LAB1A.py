#David Swansey SE126.22 LAB 1A
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

roomcap=0
attending=0
overage=0
under=0

print("Welcome to the fire infraction checker...") #welcome
answer= input("Would you like to check a room? [Y/N] :") #enter while loop
while answer == "Y" or answer == "y": #loop start
    roomcap= int(input("\nHow many people can fit in the room?: ")) #capacity of room
    attending= int(input("\nHow many people are going to be in the room?: ")) #people going to meeting
    if attending > roomcap: 
        overage= attending - roomcap #math
        print("\nThere are", overage, "more people than there should be.") #too many people
        print("FIRE INFRACTION")
    elif roomcap > attending:
        under= roomcap - attending #math
        print("\nThere are", under, "people that can still fit into the meeting") #add more people
        print("NO INFRACTIONS")
    elif roomcap == attending:
        print("\nThere is an equal amount of people to capacity") #tied
        print("Don't add anyone else and there won't be an issue")
    answer=input("\nWould you like to check another room? [Y/N]:") #re-enter loop
print("Thanks for coming, have a fire free day...") #byeeeeeeeeeeeeeeeeeeeeeeeeeeee