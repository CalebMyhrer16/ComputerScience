def begin_adventure(): #You started your adventure first interaction
    print("You wake up in the middle of the night in a place you can not remember:")
    print("1. Get out of bed and look around ")
    print("2. Wait in bed and see what happens")

    choice = input("> ")# the users choice

    if choice == "1":
        look_around()
    elif choice == "2":
        wait_bed()
    else:
        print("Invalid choice, redo")
        begin_adventure() # restarts function if invalid input thats not 1 or 2

def look_around(): #function that shows what happens when you press 1 secound interaction
    print("as you get up too look around you see a door")
    print("1. open the door")
    print("2. try to look through the cracks")

    choice_2 = input("> ")

    if choice_2 == "1":
        open_door()
    elif choice_2 ==  "2":
        look_cracks()
    else:
        print("Invalid choice, redo")
        look_around() # restarts function if invalid input thats not 1 or 2

def wait_bed(): # function for option 2 third interaction
    print("as you are sitting on your bed a shiny light hits your eye")
    print("1. reach your hand out and try to grab it ")
    print("2. decide to head to the door ")

    choice_3 = input("> ")

    if choice_3 == "1":
        reach_out()
    elif choice_3 == "2":
        look_around()
    else:
        print("Invalid choice, try again")
        wait_bed() # restarts function if invalid input thats not 1 or 2

def open_door(): # function for looking around fourth interaction
    print("You slowly open the door and as the darkness of the room evaporates you see a 6 foot 4 nonchalant dreadhead stands before you")
    print("1. Try to run away")
    print("2. challenge him to shadow boxing in exchange for your freedom")
    
    choice_4 = input("> ")

    if choice_4 == "1":
        try_run()
    elif choice_4 == "2":
        shadow_box()
    else:
        print("Invalid choice, try again")
        open_door() # restarts function if invalid input thats not 1 or 2

def look_cracks(): #  function for looking through the cracks fifth interaction
    print("as you look through the cracks in the door you see an eye meeting yours and you jump back")
    print("1. open the door")
    print("2. head back to bed")

    choice_5 = input("> ")

    if choice_5 == "1":
        open_door()

    elif choice_5 == "2":
        wait_bed()

    else:
        print("Invalid choice, try again")
        look_cracks() # restarts function if invalid input thats not 1 or 2

def reach_out(): # function for reaching out sixth interaction/interaction
    print("you grab the glowing light in the palm of your hand and then the light quickly iluminates the door and  a window")
    print("1. open the door")
    print("2. open the window")

    choice_6 = input("> ")

    if choice_6 == "1":
        open_door()

    elif choice_6 == "2":
        open_window()
    else:
        ("Invalid choice, try again")
        reach_out() # restarts function if invalid input thats not 1 or 2

def try_run(): # function quickest ending first ending
    print("SLAM!!! you run into a mirror and get knocked out, THE END, THE MIRROR ENDING, do you want to play again for more endings")
    print("1. yes")
    print("2. no")

    ending_1 = input("> ")

    if ending_1 == "1":
        begin_adventure()
    elif ending_1 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        try_run()

def shadow_box(): # function shadow box seventh function/interaction
    print(" as you start to shadow box him you notice that there copying your actions and then you realize you are THE 6 FOOT 4 NONCHALANT DREAD HEAD!!!")
    print("1. take in the aura points")
    print("2. try not to focus on that and break down the mirror and see what behind it")

    choice_7 = input("> ")

    if choice_7 == "1":
        print("takes in aura points nonchalant like but then gets back to work")
        break_down()

    elif choice_7 == "2":
        break_down()
    
    else:
        print("Invalid choice, try again")
        shadow_box() # restarts function if invalid input thats not 1 or 2

def open_window(): # function of opening the window eigth function/interaction
    print("you open the window and creep out of it quietly and then all of the sudden you look up and see a 2020 silverado truck")
    print("1. try to break in the truck")
    print("2. head back inside to see whats behind that door")
    print("3. try to run away")

    choice_8 = input("> ")

    if choice_8 == "1":
        truck_time()
    elif choice_8 == "2":
        open_door()
    elif choice_8 == "3":
        run_away()
    else:
        print("Invalid choice, try again")# restarts function if invalid input thats not 1, 2, or 3
        open_window()

def break_down(): # ninth function/interaction
    print("as you break down the mirror you see that behind it is a blue minecraft nether portal but you also see a window")
    print("1. head back to see whats on the other side of that window")
    print("2. jump through and see whats on the other side")

    choice_9 = input("> ")
    
    if choice_9 == "1":
        open_window()
    elif choice_9 == "2":
        portal_time()
    else:
        print("Invalid choice, try again")
        break_down() # restarts function if invalid input thats not 1 or 2

def run_away():#secound ending
    print("as you run away every thing gets dizzier and more wonky and then you have lost your breath, THE END, You have got the , ANYHTING BUT FORD ENDING, would you like to play again?")
    print("1. yes")
    print("2. no")

    ending_2 = input("> ")

    if ending_2 == "1":
        begin_adventure()
    elif ending_2 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        run_away()

def truck_time(): #tenth function/interaction
    print("you are succsesfully able to break into the car as you finish hot wiring it you wonder if you should put on some music")
    print("1. turn on the radio")
    print("2. keep it off")

    choice_10 = input("> ")

    if choice_10 == "1":
        radio_on()
    elif choice_10 == "2":
        keep_off()
    else:
        ("Invalid choice, try again")
        truck_time()

def portal_time(): # the elevnth function/interaction
    print("after jumping through the portal you see an uncanny version of minecraft and Jack Black is Steve")
    print("1. spam jack black with lots of emails of you disliking the minecraft movie")
    print("2. go get some wood")

    choice_11 = input("> ")

    if choice_11 == "1":
        print("jack black replied nicely so you go get wood")
        get_wood()
    elif choice_11 == "2":
        get_wood()
    else:
        ("Invalid choice, try again")
        portal_time()

def radio_on(): # the twelth function/interaction
    print("you turn on the radio and all of the sudden KSI's trash new song starts playing you keep trying to turn it off but then by accident the car goes wild and slams right into Greg paul")
    print("1. get out and see if greg is okay")
    print("2. turn off the KSI song and keep driving")

    choice_12 = input("> ")

    if choice_12  == "1":
        greg_good()
    elif choice_12 == "2":
        keep_driving()
    else:
        ("Invalid choice, try again")
        radio_on()

def keep_off(): # the third ending
    print("you decide that its probably not worth getting off focus and see greg paul in the distance you quickly manuver around him and drive until you see pure sunlight, THE END, THE GOOD CLEAN AND FREE ENDING, do you want to play again")
    print("1. yes")
    print("2. no")

    ending_3 = input("> ")

    if ending_3 == "1":
        begin_adventure()
    elif ending_3 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        keep_off()

def get_wood(): # the thirteenth function/interaction
    print("you start to mine for wood and as the block drops you pick it up and realize its greg paul")
    print("1. ask why greg is lookin like a wood block")
    print("2. see what greg has to say")

    choice_13 = input("> ")

    if choice_13 == "1":
        print("greg says its because he likes his cheese drippy bruh and then asks if you want to know what he is trying to tell you")
        greg_says()
    elif choice_13 == "2":
        greg_says()
    else:
        ("Invalid choice, try again")
        get_wood()

def greg_good(): # the fourteenth function/interaction
    print("You walk out off the car and see greg is unharmed standing there he thanks you for stopping and tells you direction to leave but he also warns you that he has no idea what is ahead of you")
    print("1. keep going till you escape whatever this place is")
    print("2. go back into town")

    choice_14 = input("> ")

    if choice_14 == "1":
        keep_going()
    elif choice_14 ==  "2":
        head_back()
    else:
        ("Invalid choice, try again")
        greg_good()

def greg_says(): #the fifteenth function/interaction
    print("greg paul starts to talk about how someone hits him in a car and now is asking for your help")
    print("1. help him")
    print("2. he can deal with his own problems")

    choice_15 = input("> ")

    if choice_15 == "1":
        help_greg()
    elif choice_15 == "2":
        ditch_greg()
    else:
        ("Invalid choice, try again")
        greg_says()

def keep_driving(): # the fourth ending
    print("you keep driving but then you see a 6 foot 4 dreadhead in the road that makes your car blowup , THE END, DONT MESS WITH GREG ENDING, want to play again?")
    print("1. yes")
    print("2. no")

    ending_4 = input("> ")

    if ending_4 == "1":
        begin_adventure()
    elif ending_4 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        keep_driving()


def keep_going(): #the sixteenth function/interaction
    print("you keep going and find that greg was a big fat liar and there was no monster their but you see a fork in the road one path going left and another going right")
    print("1. left")
    print("2. right")

    choice_16 = input("> ")

    if choice_16 ==  "1":
        left()
    elif choice_16 == "2":
        right()
    else:
        ("Invalid choice, try again")
        keep_going()

def help_greg(): # the seventeenth function/interaction
    print("greg leads you to what looks like a road suddenly a car is racing towards you with a nonchalant dread head as the driver")
    print("1. stop him with you aura points")
    print("2. do nothing and let him live ")

    choice_17 = input("> ")

    if choice_17 == "1":
        stop_him()
    elif choice_17 == "2":
        do_nothing()
    else:
        ("Invalid choice, try again")
        help_greg()

def head_back(): # the fifth ending
    print("you start to drive back but suddenly you start to glow and all of the sudden you teleport into the room you started in but your stuck on top of the bed, THE END, THE BRIGHT BEGGININGS ENDING, want to try again?")
    print("1. yes")
    print("2. no")

    ending_5 = input("> ")

    if ending_5 == "1":
        begin_adventure()
    elif ending_5 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        head_back()

def ditch_greg():# the sixth ending
    print("what does he know hes just a dad of two annoying kids after walking away you live your life too the fullest and regret nothing, THE END, THE GOOD ENDING, want to try again?")
    print("1. yes")
    print("2. no")

    ending_6 = input("> ")

    if ending_6 == "1":
        begin_adventure()
    elif ending_6 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        ditch_greg

def left():# the seventh ending
    print("you keep going left but something is not right you start to glow and get teleported back above the bed where you started, THE END,  THE BRIGHT BEGGININGS ENDING, want to try again?")
    print("1. yes")
    print("2. no")

    ending_7 = input("> ")

    if ending_7 == "1":
        begin_adventure()
    elif ending_7 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        left()

def right():# the eighteenth function/interaction
    print("you keep heading right and everything seems to be ok but then you hear people around start to shout and you feel a Virtual headset on you head")
    print("1. take it off see whats out there")
    print("2. keep it on this life is better")

    choice_18 = input("> ")

    if choice_18 == "1":
        take_off()
    elif choice_18 == "2":
        print("life aint better bud this place is crazy")
        take_off()
    else:
        ("Invalid choice, try again")
        right()

def stop_him():# the eigth ending
    print("you choose to stop him before he hits you but slam the guy is knocked out and he isnt coming back slowley you look at your hands and realize your disappering and eventually POOF, THE END, THE WAS THAT ME? ENDING, want to try again")
    print("1. yes")
    print("2. no")

    ending_8 = input("> ")

    if ending_8 == "1":
        begin_adventure()
    elif ending_8 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        stop_him()

def do_nothing():# the ninteenth fuction/interaction
    print("you realize you should let them live and you quickly get out of the way then you get teleported out of this crazy world and appear in a house you look over and see the guy in the car but he has a vr headset on")
    print("1. tell him to take it off")
    print("2. yank it off him")

    choice_19 = input("> ")

    if choice_19 == "1":
        print("they are not listing your going to have to take it off them")
        yank_off()
    elif choice_19 == "2":
        yank_off()
    else:
        ("Invalid choice, try again")
        do_nothing()

def take_off():# the twenty  function/interaction
    print("you feel someone yanking it off you and then pop its off you then see a familiar face ")
    print("1. say thanks for taking it off")
    print("2. get some lunchly with bro")

    choice_20 = input("> ")

    if choice_20 == "1":
        print("you say thanks and then go gets lunchly with bro")
        lunchly_time()
    elif choice_20 == "2":
        lunchly_time()
    else:
        ("Invalid choice, try again")
        take_off()

def yank_off(): #the ninth ending
    print("as you yank it off the other person helps you take it off after that you stare at each other for a couple moments and then he asks if you want to get lunchly, THE END, THE TRUE ENDING, want to play again?")
    print("1. yes")
    print("2. no")

    ending_9 = input("> ")

    if ending_9 == "1":
        begin_adventure()
    elif ending_9 == "2":
        print("thanks for playing")
    else:
        ("Invalid choice, try again")
        yank_off()

def lunchly_time(): #the tenth ending
    print("you ask bro if you want to get lunchly he sits there and stares at you and then...., THE END, THE TRUE ENDING, want to play again?")
    print("1. yes")
    print("2. no")

    ending_10 = input(" > ")

    if ending_10 == "1":
        begin_adventure()
    elif ending_10 == "2":
        print(" thanks for playing")
    else:
        ("Invalid choice, try again")
        lunchly_time()
#Caleb Myhrer
begin_adventure()