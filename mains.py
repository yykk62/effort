print ("Effort Calculator ")
print ("    DEMO ____by____ YYKK#0062 ")
print (" Slide Jjk Cards ")
##Var's
end_effort = 0
added_style = 0
added_wellness = 0

current_effort = float(input("Current Effort: "))
base_value = float(input("Base Value: "))
mystic = str(input("you want to add Mystic? (y/n) "))
frame = str(input("you want to add Frame? (y/n) "))
dye = str(input("you want to add Dye? (y/n) "))
##IF Statements
if mystic.upper() == "N" and dye.upper() == "Y":
    ##base value * 0.2 ( regular dye )
    added_style = base_value * 0.2
    added_wellness = added_style * 0.25
    end_effort = current_effort + added_style + added_wellness
    print("Added Style Points: " + str(added_style))
    print("Added Wellness Points: " + str(added_wellness))
    print("Effort: " + str(end_effort))
if mystic.upper() == "Y" and frame.upper() == "Y":
    ## Mystic AND Frame
    added_style = base_value * 1.5
    added_wellness = added_style * 0.25
    end_effort = current_effort + added_style + added_wellness
    print ("Mystic Added")
    print ("Added Style Points: " +str(added_style))
    print ("Added Wellness Points: " +str(added_wellness))
    print ("Effort: " +str(end_effort))
elif mystic.upper() == "Y" or frame.upper() == "Y":
    ##Mystic OR Frame
    added_style = base_value * 0.75
    added_wellness = added_style * 0.25
    end_effort = current_effort + added_style + added_wellness
    print ("Added Style Points: " +str(added_style))
    print ("Added Wellness Points: " +str(added_wellness))
    print ("Effort: " +str(end_effort))

end = str(input("End? (Press any Button) "))

