allow_advanced = "false"

asciiFile = open("./values/ascii.txt","r")
asciiText = asciiFile.readlines()
for line in asciiText:
    print(ascii(line))
print("")
print ("Toilet Paper Calculator")
print ("github.com/Kah00ted/tpcalculator")
print("")


custom = input("Use advanced mode?(y/N) ")
print ("")
if (custom == "y"):
    if (allow_advanced == "true"):
        print ("yay")
    else:
        print ("Sorry, advanced mode is currently unavalable.")
else:
    rolls = input("How many rolls of tp do you have? ")
    print ("")
    spr = input("How many squares are on each roll? ")
    sprFile = open("./values/spr.txt","a")
    sprFile.write("\n" + spr)
    sprFile.close()
    print ("")
    upd = input("How many times do you use the bathroom daily? ")
    updFile = open("./values/upd.txt","a")
    updFile.write("\n" + upd)
    updFile.close()
    print ("")
    pih = input("How many people live in your household? ")
    print ("")
    spw = input("How many squares do you use each time you wipe? ")
    spwFile = open("./values/spw.txt","a")
    spwFile.write("\n" + spw)
    spwFile.close()
    print ("")
    wpu = input("How many times do you wipe per bathroom use? ")
    wpuFile = open("./values/wpu.txt","a")
    wpuFile.write("\n" + wpu)
    wpuFile.close()

totalSquares = (int(rolls) * int(spr))
spu = (int(spw) * int(wpu)) #squares per bathroom use
spp = (spu * int(upd)) #squares per person daily
sud = (spp * int(pih)) #total squares used daily
daysLeft = (totalSquares / sud)
print ("")
print ("You have a " + str(int(daysLeft)) + " day supply of tp")