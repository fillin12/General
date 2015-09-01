

import random
import time

class Fish( object ):
    
          # 4 Letter Code: [ Fish,           possible points,  level, ( good or bad ) ] 
    fish = {      "BASS" : [ "1 Bass",               ( 5, 10 ),      1, "Good" ], \
                  "CATF" : [ "1 Catfish",            ( 7, 15 ),      1, "Good" ], \
                  "TUNA" : [ "3 Tuna",               ( 25, 100 ),    3, "Good" ], \
                  "GUPY" : [ "0 Guppy",              ( 1, 5 ),       0, "Good" ], \
                  "HRNG" : [ "0 Herring",            ( 3, 6 ),       0, "Good" ], \
                  "JELY" : [ "2 Jellyfish",          ( -10, 3 ),     2, "Bad" ], \
                  "STUR" : [ "3 Sturgeon",           ( 75, 175 ),    3, "Good" ], \
                  "MACK" : [ "2 Mackerel",           ( 5, 10 ),      2, "Good" ], \
                  "CUDA" : [ "2 Barracuda",          ( -20, 5 ),     2, "Bad" ], \
                  "PUFR" : [ "1 Pufferfish",         ( -5, 5 ),      1, "Bad" ], \
                  "MARL" : [ "3 Marlin",             ( 75, 175 ),    3, "Good" ], \
                  "SAIL" : [ "3 Sailfish",           ( 100, 200 ),   3, "Good" ], \
                  "GRWS" : [ "4 Great White Shark",  ( -75, 600 ),   4, "Good" ], \
                  "STRY" : [ "1 Sting Ray",          ( -10, 5 ),     1, "Bad" ], \
                  "TGRF" : [ "4 Tiger Fish",         ( -50, 550 ),   4, "Good" ], \
                  "ORCA" : [ "4 Orca",               ( -5, 550 ),    4, "Good" ], \
                  "CTHU" : [ "5 Cthulu",             ( -800, 2000 ), 5, "Good" ], \
                  "KRAK" : [ "5 Kraken",             ( -900, 3000 ), 5, "Good" ], \
                  "MOBY" : [ "5 White Whale",        ( -1000, 3500), 5, "Good" ], \
                  "BLUE" : [ "2 Blue Gill",          ( 1, 15),       2, "Good" ]     }

            

    def __init__( self, species = "BASS" ):

        self.__species = Fish.fish[ species ][ 0 ]
        self.__points = Fish.fish[ species ][ 1 ]
        self.__level = Fish.fish[ species ][ 2 ]
        
                
    def __str__( self ):

        return "{}".format( self.__species )
    

    def __repr__( self ):

        return "{}".format( self.__species )
    
        
    def points( self ):
        """ Returns the points earned for catching this fish """

        points = int( random.uniform( self.__points[ 0 ], self.__points[ 1 ] ) )
                      
        return points
                      

    def catch( self, adjustment = 0 ):

        """Assigns catch probabilities for fish. Can be adjusted up or down
        to make the fish easier or harder to come by"""

        catch_list = [ False, False, False, False, False, False ]
        
        chance = int( random.uniform( 0, 101 ) ) # ranges from 0 to 100

        if self.__level >= 0:
            if chance > (10 - adjustment ): # 90% chance to catch level 0's w/ 0 adjust
                catch_list[ 0 ] = True

        if self.__level >= 1:
            if chance > (25 - adjustment ): # 75% chance to catch level 1's w/ 0 adjust
                catch_list[ 1 ] = True

        if self.__level >= 2:
            if chance > (40 - adjustment ): # 60% chance to catch level 2's w/ 0 adjust
                catch_list[ 2 ] = True

        if self.__level >= 3:
            if chance > (80 - adjustment ): # 20% chance to catch level 3's w/ 0 adjust
                catch_list[ 3 ] = True
                      
        if self.__level >= 4:
            if chance > (93 - adjustment ): # 7% chance to catch level 4's w/ 0 adjust
                catch_list[ 4 ] = True

        if self.__level >= 5:
            if chance > (99 - adjustment ): # 1% chance to catch level 5's w/ 0 adjust
                catch_list[ 5 ] = True

        return catch_list[ self.__level ]


    
class Fisher( object ):

    def __init__( self, name, level = 0, points = 0 ):

        self.__name = name
        self.__level = level
        self.points = points

    def __str__( self ):

        return "{}: Level: {} Points: {}".format( self.__name, self.__level, self.points )

    def __repr__( self ):

        return "{}: Level: {} Points: {}".format( self.__name, self.__level, self.points )

    def level_up( self ):
        """Adds one level when earned in-game"""
        
        self.__level += 1

    def get_level( self ):
        """Retrieves the level of the fisher"""

        return self.__level

    def get_points( self ):
        """Retrieves the points of the fisher"""

        return self.points

    def get_name( self ):
        """Retrieves the name of the fisher"""

        return self.__name
        


##############################################################################################
### Carpet Fishing!
##############################################################################################

debug = False
if debug:
    instruct_the_gamer = False
    target_points = 200
    game_length = "Test"
    print( "#############################################################################" )
    print( "################################ DEBUG ON ###################################" )
    print( "#############################################################################" )


def get_score():
    """Retrieves the score"""
    
    score =  ( ( target_points / game_time ) / total_trawls ) 
    return score


def display_stats():

    """ Displays player statistics"""
    
    print()
    print( "{:>40}: {}".format( "Stats for", fisher_name ) )
    print( "{:>40}: {}".format( "Level", fisher.get_level() ) )
    print( "{:>40}: {}".format( "Points", fisher.points ) )
    print( "{:>40}: {}".format( "Trawling Number", max_trawl_number ) )
    print( "{:>40}: {}".format( "Shifted Odds", favorable_odds ) )
    print( "{:>40}: {}".format( "Current time", current_time ) )
    print( "{:>40}: {}".format( "Your current score ", get_score() ) )
    print( "{:>40}: {}".format( "Target Points ", target_points ) )

    
def display_fishies():
    """Prints the fish and all of their statistics"""

    print()
    for fish, attributes in all_fish.items():
        for fish_level in range(0,6):
            if attributes[2] == fish_level:
                level_needed = attributes[2]
                name = attributes[0][2:]
                point_range_min = attributes[1][0]
                point_range_max = attributes[1][1]
                good_or_bad = attributes[3]
                print( "{:<20}---> Level: {}    {:>7} Fish   Point Range: {:>5} to {}".format( name, level_needed, good_or_bad, point_range_min, point_range_max ) )
                


def display_catch( catch_dict, points ):
    """ Displays all fish caught for given trawl"""

    print( "\n#### TRAWLING PAYOFF ####\n" )

    for keys, values in catch_dict.items():
        print( keys, ":", values )
    print( "\nTotal points for this trawl: ", points )
    if points < 0:
        print( "#### A trawler was damaged during this trawl! ####" )

        
def count_catch( fish ):
    """ Uses a global name to keep track of
        the amount of fish caught"""

    try:
        fish_count[ fish ] += 1
    except KeyError:
        fish_count[ fish ] = 1


def restrict( restriction ):
    
    if ( fisher.get_level() >= restriction ):
        
        if fish_restrictions[ restriction ]:
            
            if indie_restr_check( restrict_check(), restriction ):
                fish_restrictions[ restriction ] = False
                print( "\n---> You are NOT fishing level", restriction, "fish!" )
                
            else:
                print( "\n#### You don't have any restrictions svailable! ####" )
        else:
            fish_restrictions[ restriction ] = True
            print( "\n---> You have BEGUN fishing level", restriction, "fish!" )
    else:
        print( "\n#### You can't restrict that type of fish yet! You need a higher level! ####" )


def restrict_check():
    """Stops restrictions from being turned on if there's not enough. Always keeps the fish
       a-flowing"""

    fishing_bool = False 
    max_restrictions = fisher.get_level()
    fishables = 0
    while max_restrictions > -1:
        if fish_restrictions[ max_restrictions ]:
            fishables +=1
        max_restrictions -= 1
    if fishables > 1:
        fishing_bool = True

    return fishing_bool # too many restrictions if False


def indie_restr_check( boolean, fish_level ):
    """Used to make sure that restrictions can be turned back off"""
    
    if not boolean: # if too many restrictions
        if not fish_restrictions[ fish_level ]: # and the restriction is on
            fishing_bool = True # this restriction can be turned off
    if boolean: # if enough restrictions are off
        fishing_bool = True
    if not boolean:
        if fish_restrictions[ fish_level ]:
            fishing_bool = False

    return fishing_bool
        

all_fish = Fish.fish

zero_fish = []
one_fish = []
two_fish = []
three_fish = []
four_fish = []
five_fish = []


for codes in all_fish.keys(): # Creates lists of fish codes divided by levels
    
    fish_level = all_fish[ codes ][ 2 ]

    fish = Fish( codes )
    
    if fish_level == 0:
        zero_fish.append( fish )
    if fish_level == 1:
        one_fish.append( fish )
    if fish_level == 2:
        two_fish.append( fish )
    if fish_level == 3:
        three_fish.append( fish )
    if fish_level == 4:
        four_fish.append( fish )
    if fish_level == 5:
        five_fish.append( fish )


#################################
### IMPORTANT VALUES


max_trawl_number = 10        # Max number of trawls (in beginning)
level_cost = 100             # Starting cost for leveling up
increase_odds_cost = 100     # Starting cost for odds increase
favorable_odds = 0           # The odds adjustment! A larger value makes it easier to catch fish
add_trawls_cost = 100        # cost for more trawls
total_trawls = 0

fish_restrictions = [ True, True, True, True, True, True ]

print()
print( "{:<10}{}".format ( "","################################################" ) )
print( "{:<10}{}".format ( "","########## WELCOME TO CARPET FISHING! ##########" ) )
print( "{:<10}{}".format ( "","################################################" ) )


if debug:
    fisher_name = "Bob"
else:
    fisher_name = input( "\nBefore we begin, please enter your name: " )
    
fisher = Fisher( fisher_name, level = 0 )

while True:
    if debug:
        break
    help_for_gamer = input( "\nDo you need instructions to play this game? Y or N: " )
    if help_for_gamer.lower() == "y":
        instruct_the_gamer = True
        break
    elif help_for_gamer.lower() == "n":
        instruct_the_gamer = False
        break
    else:
        print( "\nThat's not a proper answer. Cast again", fisher_name,"cause time's a wastin'!" )
        continue

if instruct_the_gamer:
    print( "\n\nThis game is all about fake economics of fishing!",\
           "\nIt is your goal to end this game with as many points per trawl as possible",\
           "\nbefore you reach the target points",\
           "\nThat goal can be",\
           "\n\nShort: 1,000,000 points",\
           "\nMedium: 10,000,000 points",\
           "\nor Long: 100,000,000 points.",\
           "\n(None of these lengths are actually very long)",\
           "\n\nYou achieve these points by trawling for fish!",\
           "\nYou will start out fishing small level 0 fish and as you fish more, you will be able to fish larger fish!",\
           "\nThe larger the fish the riskier it can get because larger fish are dangerous!",\
           "\nYou can lose large amounts of points from large fish but they also allow you to gain the most.",\
           "\nThe larger they are, the less frequently you are likely to catch them.",\
           "\nTo help you with these problems, you can buy upgrades with your points to help you gain points faster.",\
           "\nThere will be more instructions in the game for that.",\
           "\nFor now, pick a game length!" )

while True:
    if debug:
        break
    game_goal = input( "\nEnter your desired game length (s = small, m = medium, l = large): " )
    if game_goal.lower() == "s":
        target_points = 1000000
        game_length = "Short"
        break
    elif game_goal.lower() == "m":
        target_points = 10000000
        game_length = "Medium"
        break
    elif game_goal.lower() == "l":
        target_points = 100000000
        game_length = "Long"
        break
    else:
        print( "\nFishermen can't understand that sort of language. Give it another go!" )

if instruct_the_gamer:
    print("\n\nAn important features of the game include the trawling points.",\
          "\nTrawling points can be positive or negative depending on the random point spread of each fish caught.",\
          "\nEach fish has a good or bad attribute that depends on its point spread: If you are more likely to",\
          "\ngain points from the fish it is a good fish, if you are likely to get a negative value it is a bad fish!",\
          "\nAll the fish and their attributes are displayed here: " )
    
    display_fishies()
            
if instruct_the_gamer:
    print( "\n\nNow that you have done that, you will be prompted for readiness!",\
           "\nWhen you're ready, enter the appropriate response, you will have 5 seconds before it starts!." )

if not debug:
    
    while True:
        readiness = input( "\nAre you ready to begin? Y or N: " )
        if readiness.lower() == "y":
            break
        else:
            print( "\nGet Ready! We're burning daylight!" )

    print( "\nYou have 5 seconds until the start! Prepare!\n" )

    clock = 5        # The countdown!
    while clock > 0:
        print( clock, end = "!! " )
        clock -= 1
        time.sleep(1)

    print( "\n\n" )
    print( "{:>55}".format( "########## BEGIN FISHING! ##########" ) )

start_time = time.time()

action_count = 0

while fisher.get_points() < target_points:

    current_time = time.time()- start_time
    fish_count = {}
    trawl_points = 0
    trawling_number = 0
    action_count += 1
    
    try:
        score = fisher.points / total_trawls
    except ZeroDivisionError: #happens when current_time initiates
        score = fisher.get_points()
        
    if instruct_the_gamer and action_count <= 1:
        print( "\n\nThis is the main menu!",\
               "\nFrom here, you have a number of options; each one indicated by its adjoined letter.",\
               "\nGO TRAWLING is how you get points! Just enter t and go!",\
               "\nAs mentioned earlier, UPGRADES allow you to trawl better at the expense of your points.",\
               "\nRESTRICTIONS is of strategic importance: you can change your ability to catch specific",\
               "\nlevels of fish at will! If you're having bad luck in one level, turn it off to shift your",\
               "\nresources to a new level!",\
               "\nPLAYER STATS displays your in-game statistics like your level, points, upgrades and some other stuff.",\
               "\nDISPLAY FISH displays the stats of a fish (useful if you're forgetful).",\
               "\nA key one to note is TOGGLE HELP which turns these instructions on and off.",\
               "\nA few important notes:",\
               "\nIMPORTANT: main menu instructions disappear after the first read (they get in the way)",\
               "\nThe main menu instructions can be brought back by toggling help OFF then ON",\
               "\nIMPORTANT: you can press q any time from the main menu to quit.",\
               "\nTry some out!" )
    
    print()
    print( "{:>40}".format( "Go Trawling: t" ) )
    print( "{:>40}".format( "Upgrades: u" ) )
    print( "{:>40}".format( "Restrictions: r" ) )
    print( "{:>40}".format( "Player stats: s" ) )
    print( "{:>40}".format( "Display Fish: f" ) )
    print( "{:>40}".format( "Toggle Help: h" ) )
    
    command = input( "\n                    Enter your command Captain: " )

    

    if command.lower() == "q":
        
        prompt = input( "\nAre you sure you want to quit? Y or N: " )
        if prompt.lower() == "y":
            print()
            print( "{:>40}".format( "You have stopped the game!" ) )
            quit()
            
        else:
            print( "\n---> That answer looks like you want to keep playing!" )

            
    elif command.lower() == "f":
        
        display_fishies()

    
    elif command.lower() == "h":
        
        if instruct_the_gamer:
            instruct_the_gamer = False
            print( "\n---> Help is OFF!" )
            
        else:
            instruct_the_gamer = True
            print( "\n---> Help is ON!" )
            action_count = 0

        
    elif command.lower() == "s":
        
        display_stats()
        
    elif command.lower() == "u": # Upgrades!

        if instruct_the_gamer:
            print( "\nHere is the spot to augment your skill! But beware!", \
                   "\nYou need to spend points to get better (hitting", target_points, "ends the game).",\
                   "\nHere's some things you can do: ", \
                   "\n\nLevel up to trawl for different fish. You CANNOT go above level 5.", \
                   "\nTurn the odds of catching ALL fish to your favor."\
                   "\nLastly, you can buy more trawls to catch even more fish!" \
                   "\n\nPrices for a purchased upgrade increase ten-fold every time you buy it.",\
                   "\nUpgrades are INFINITE (except levels), you can get as many as you want (that'll cost a lot though)",\
                   "\nALL upgrades are permanent! Even if you've made a mistake so be careful!",\
                   "\nRemember: You want to maximize points per trawl!" )
        print()
        print()
        print( "{:>50}".format( "What would you like to upgrade?" ) )
        print()
        print( "{:>44}: {}".format( "Enter L for a level up!  ", level_cost ) )
        print( "{:>44}: {}".format( "Enter O for good odds!   ", increase_odds_cost ) )
        print( "{:>44}: {}".format( "Enter T for more trawls! ", add_trawls_cost ) )
        
        upgrade = input( "\n                   Enter your desired upgrade: " )

        if upgrade.lower() == "l" and ( fisher.points >= level_cost ):
            
            if fisher.get_level() <= 4:
                fisher.points -= level_cost
                fisher.level_up()
                level_cost *= 5
                print( "\n---> You can now fish level", fisher.get_level(), "fish!" )
            else:
                print( "\n#### You cannot fish above level five! ####" )

        elif upgrade.lower() == "t" and ( fisher.points >= add_trawls_cost ):
            fisher.points -= add_trawls_cost
            max_trawl_number *= 2
            add_trawls_cost *= 5
            print( "\n---> You can now perform", max_trawl_number, "trawls!" )

        elif upgrade.lower() == "o" and ( fisher.points >= increase_odds_cost ):
            fisher.points -= increase_odds_cost
            increase_odds_cost *= 5
            favorable_odds += 5  #imporves odds by 5%
            print( "\n---> Your odds of catching fish are improved by", favorable_odds, "percent!" )
            
        else:
            print( "\n#### You didn't purchase anything! Back to the menu! ####" )

            
    elif command.lower() == "r" : # Stops fishing for certain fish

        print()
        for index in range (0, (fisher.get_level() + 1) ):
            restrict_bool = fish_restrictions[ index ]
            if restrict_bool:
                print( "---> Level", index, "fish are being caught!" )
            
            else:
                print( "---> Level", index, "fish are NOT being caught!" )
            
        
        if instruct_the_gamer:
            print( "\nFrom here, you can reallocate your given trawls for different levels of fish.",\
                   "\nFor example: if you are level 2 you can turn off level 1 fish (level 1's are more reliable",\
                   "\nbut worth less) you will focus all of your trawls on level 2 (level 2 are higher risk but worth more).",\
                   "\nRegardless of input, you will be returned to the main menu after it is entered and executed.",\
                   "\nYou will not be able to restrict all of your fish because you can't fish that way!",\
                   "\nAll of your restrictions are listed above you can NEVER have all restrictions turned on.",\
                   "\nRemember: You want the most points per trawl!" )
        try:
            
            restriction = input( "\n\nEnter the level of fish (0-5) you'd like to stop or start fishing: " )
            restriction = int( restriction )
            
            restrict( restriction )

        except ValueError:
            print( "\n#### That is not a fish's level! The clock's ticking! ####" )

        
            
    
    elif command.lower() == "t": # Go fishing...

        total_trawls += 1

 
        while ( trawling_number < max_trawl_number ):

            
            if fisher.get_level() >= 0 and fish_restrictions[0]:
                
                random.shuffle( zero_fish )
                potential_fish = zero_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds ) # Fish object usage!

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1
                


            if fisher.get_level() >= 1 and fish_restrictions[1]:

                
                random.shuffle( one_fish )
                potential_fish = one_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds )

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1


            if fisher.get_level() >= 2 and fish_restrictions[2]:
                
                random.shuffle( two_fish )
                potential_fish = two_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds )

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1


            if fisher.get_level() >= 3 and fish_restrictions[3]:
                
                random.shuffle( three_fish )
                potential_fish = three_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds )

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1


            if fisher.get_level() >= 4 and fish_restrictions[4]:
                
                random.shuffle( four_fish )
                potential_fish = four_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds )

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1


            if fisher.get_level() >= 5 and fish_restrictions[5]:
                
                random.shuffle( five_fish )
                potential_fish = five_fish[ 0 ]
                caught = potential_fish.catch( favorable_odds )

                if caught:
                    points = potential_fish.points()
                    fisher.points += points
                    trawl_points += points
                    count_catch( potential_fish )

                trawling_number += 1

        if instruct_the_gamer:
            print( "\n\n#### TRAWLING HELP ####",\
                   "\nNow that you've just trawled, you can now see the display for this specific trawl.",\
                   "\nThis will happen each time you go trawling.",\
                   "\nSome important things to note are the numbers to the left and right of the fish.",\
                   "\nThe numbers on the right indicate the amount of fish that you've caught in this trawl.",\
                   "\nThe numbers on the left indicate the level of the fish being caught.",\
                   "\nTogether, along with the points acquired from the trawl, this information can tell you how well you're doing.",\
                   "\nTry some restrictions (if you can) to change up your trawling." )
       
    else:
        print( "\n#### You're not fishing for anything! Time's a wastin'!!! ####" )

    if command.lower() == "t":
        display_catch( fish_count, trawl_points )

    print()
    print( "{:>40}: {}".format( "CURRENT POINTS", fisher.points ) )
        
    

    
end_time = time.time()
game_time = end_time - start_time

print( "\n     #### It took you", round( game_time, 3), "seconds and", total_trawls, "trawls to earn", target_points, "points! ####" )
score = fisher.points / total_trawls
print()
display_stats()
print()


##########################################################################################
### HIGH SCORES LIST
##########################################################################################


## Add high score list options for game length.

if game_length == "s":
    
    try:
        hiscore_file = open( "FishingTrawlerScoresShort.txt", "a" )
    except IOError:    
        hiscore_file = open( "FishingTrawlerScoresShort.txt", "w" )

    new_line = "{}:{}:{}".format( fisher.get_name(), round( score, 3),  game_length )

    print( new_line, file = hiscore_file )


    hiscore_file.close() # saves the file
    hiscore_file = open( "FishingTrawlerScoresShort.txt", "r" ) #reopens the new file


    scores_dict = {}

    for lines in hiscore_file:
        
        try:
            
            line_list = lines.split( ":" )
            
        except IndexError:
            continue
        

        player_score = float( line_list[1] )

        scores_dict[ player_score ] = line_list

        
    scores_list = []
    previous_score = -10000000000

    for score_keys in scores_dict:

        scores_list.append( score_keys )
        
    scores_list.sort( reverse = True )


    print( "\n                       ########## High Scores ##########\n" )
    print( "                     Rank   Name     Score          Length" )
    print()

    rank = 1
    for scores in scores_list:

        name = scores_dict[ scores ][ 0 ]
        score = scores_dict[ scores ][ 1 ]
        length = scores_dict[ scores ][ 2 ]

        if len( name ) > 6: # keeps length less than 6
            name = name[:7]
        
        printable_line = "{:>24}    {:<7}  {:<15}{}".format( rank, name, score, length.strip() )
        print( printable_line )
        rank += 1

        if rank == 11:
            break

    hiscore_file.close() # closes the file!




elif game_length == "m":

    try:
        hiscore_file = open( "FishingTrawlerScoresMed.txt", "a" )
    except IOError:    
        hiscore_file = open( "FishingTrawlerScoresMed.txt", "w" )

    new_line = "{}:{}:{}".format( fisher.get_name(), round( score, 3),  game_length )

    print( new_line, file = hiscore_file )


    hiscore_file.close() # saves the file
    hiscore_file = open( "FishingTrawlerScoresMed.txt", "r" ) #reopens the new file


    scores_dict = {}

    for lines in hiscore_file:
        
        try:
            
            line_list = lines.split( ":" )
            
        except IndexError:
            continue
        

        player_score = float( line_list[1] )

        scores_dict[ player_score ] = line_list

        
    scores_list = []
    previous_score = -10000000000

    for score_keys in scores_dict:

        scores_list.append( score_keys )
        
    scores_list.sort( reverse = True )


    print( "\n                       ########## High Scores ##########\n" )
    print( "                     Rank   Name     Score          Length" )
    print()

    rank = 1
    for scores in scores_list:

        name = scores_dict[ scores ][ 0 ]
        score = scores_dict[ scores ][ 1 ]
        length = scores_dict[ scores ][ 2 ]

        if len( name ) > 6: # keeps length less than 6
            name = name[:7]
        
        printable_line = "{:>24}    {:<7}  {:<15}{}".format( rank, name, score, length.strip() )
        print( printable_line )
        rank += 1

        if rank == 11:
            break

    hiscore_file.close() # closes the file!


    
            
    
elif game_length == "l":

    try:
        hiscore_file = open( "FishingTrawlerScoresLong.txt", "a" )
    except IOError:    
        hiscore_file = open( "FishingTrawlerScoresLong.txt", "w" )

    new_line = "{}:{}:{}".format( fisher.get_name(), round( score, 3),  game_length )

    print( new_line, file = hiscore_file )


    hiscore_file.close() # saves the file
    hiscore_file = open( "FishingTrawlerScoresLong.txt", "r" ) #reopens the new file


    scores_dict = {}

    for lines in hiscore_file:
        
        try:
            
            line_list = lines.split( ":" )
            
        except IndexError:
            continue
        

        player_score = float( line_list[1] )

        scores_dict[ player_score ] = line_list

        
    scores_list = []
    previous_score = -10000000000

    for score_keys in scores_dict:

        scores_list.append( score_keys )
        
    scores_list.sort( reverse = True )


    print( "\n                       ########## High Scores ##########\n" )
    print( "                     Rank   Name     Score          Length" )
    print()

    rank = 1
    for scores in scores_list:

        name = scores_dict[ scores ][ 0 ]
        score = scores_dict[ scores ][ 1 ]
        length = scores_dict[ scores ][ 2 ]

        if len( name ) > 6: # keeps length less than 6
            name = name[:7]
        
        printable_line = "{:>24}    {:<7}  {:<15}{}".format( rank, name, score, length.strip() )
        print( printable_line )
        rank += 1

        if rank == 11:
            break

    hiscore_file.close() # closes the file!


    
    
if game_length == "Test":

    try:
        hiscore_file = open( "FishingTrawlerScoresTest.txt", "a" )
    except IOError:    
        hiscore_file = open( "FishingTrawlerScoresTest.txt", "w" )

    new_line = "{}:{}:{}".format( fisher.get_name(), round( score, 3),  game_length )

    print( new_line, file = hiscore_file )


    hiscore_file.close() # saves the file
    hiscore_file = open( "FishingTrawlerScoresTest.txt", "r" ) #reopens the new file


    scores_dict = {}

    for lines in hiscore_file:
        
        try:
            
            line_list = lines.split( ":" )
            
        except IndexError:
            continue
        

        player_score = float( line_list[1] )

        scores_dict[ player_score ] = line_list

        
    scores_list = []
    previous_score = -10000000000

    for score_keys in scores_dict:

        scores_list.append( score_keys )
        
    scores_list.sort( reverse = True )


    print( "\n                       ########## High Scores ##########\n" )
    print( "                     Rank   Name     Score          Length" )
    print()

    rank = 1
    for scores in scores_list:

        name = scores_dict[ scores ][ 0 ]
        score = scores_dict[ scores ][ 1 ]
        length = scores_dict[ scores ][ 2 ]

        if len( name ) > 6: # keeps length less than 6
            name = name[:7]
        
        printable_line = "{:>24}    {:<7}  {:<15}{}".format( rank, name, score, length.strip() )
        print( printable_line )
        rank += 1

        if rank == 11:
            break

    hiscore_file.close() # closes the file!

# The end of project 11!    
    



        



        
          
                         

