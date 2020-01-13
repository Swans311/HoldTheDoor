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
print("Welcome to the fire infraction checker...")
answer= input("Would you like to check a room? [Y/N] :")
while answer == "Y" or answer == "y":
    roomcap= int(input("\nHow many people can fit in the room?: "))
    attending= int(input("\nHow many people are going to be in the room?: "))
    if attending > roomcap:
        overage= attending - roomcap
        print("\nThere are", overage, "more people than there should be.")
        print("FIRE INFRACTION")
    elif roomcap > attending:
        under= roomcap - attending
        print("\nThere are", under, "people that can still fit into the meeting")
        print("NO INFRACTIONS")
    elif roomcap == attending:
        print("\nThere is an equal amount of people to capacity")
        print("Don't add anyone else and there won't be an issue")
    answer=input("\nWould you like to check another room? [Y/N]:")
print("Thanks for coming, have a fire free day...")