print("\tWelcome To The MPS Conversion App")

#Input Data
while True:
    usr_speed = float(input("\n\tWhat is your speed in miles per hour: "))
    if usr_speed > 0:
        break
    elif usr_speed < 0:
        print("\tSpeed cannot be negative")
    elif usr_speed == 0:
        print("\tSpeed cannot be zero")

#Logic for Conversion
mps = usr_speed*0.447
mps = round(mps,2)

#Display The Element
print("\n\tYour speed in meters per second is: {}".format(mps))
