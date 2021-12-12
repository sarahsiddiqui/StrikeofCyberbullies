import os
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

from pygame import * 
init()
size = width, height = 1000, 700
screen = display.set_mode(size)

#initializing variables required before game loop
score = 0
bully_width = 70
bully_height = 70
food_width = 70
food_height = 70

#define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (205, 145, 145)
DARK_BROWN = (110, 50, 50)
RED = (255, 35, 35)
DARK_RED = (195, 0, 0)
ORANGE = (194, 63, 0)
YELLOW = (255, 220, 117)
DARK_GREEN = (0, 109, 58)
BLUE = (0, 47, 166)
DARK_BLUE = (55, 0, 155)
PURPLE = (217, 176, 255)
DARK_PURPLE = (101, 0, 188)
DARK_PINK = (255, 0, 127)

#states in the Game
STATE_MENU = 0
STATE_GAME = 1
STATE_HELP = 2
STATE_QUIT = 3 
STATE_INTERMISSION = 4

#define fonts
titleFont = font.SysFont("Didot", 78) ##Creates a larger sized font for any title
bodyFont = font.SysFont("Didot", 40)  ##Creates a fairly normal sized font for any information given to the user
smallFont = font.SysFont("Didot", 25) ##Creates a smaller sized font for any any extra information given to the user

#define images
##Backgrounds
roomPic = image.load("Room.jpeg")                                             ##creates the variable roomPic for the menu background
laptopPic = image.load("Computer.jpeg")                                       ##creates the variable laptopPic for the image of the help area background
socialmediaPic = image.load("RainbowGameBackground.jpeg")                     ##creates the variable socialmediaPic for the image of the game background
socialmediaPic = transform.scale(socialmediaPic, (width, height))             ##makes the socialmediaPic the same size as the screen
endGamePic = image.load("YellowAndBlueGameBackground.jpeg")                   ##creates the variable endGamePic for the image of the game background
endGamePic = transform.scale(endGamePic, (width, height))                     ##makes the endGamePic the same size as the screen
bullyPic = image.load ("Cyberbully.jpeg")                                     ##creates the variable bullyPic for the image of the bully
bullyPic = transform.scale(bullyPic, (bully_width, bully_height))             ##makes the variable bullyPic with the same bully dimentions
helplessUserPic = image.load ("SadComputer.png")                              ##creates the variable helplessUserPic for the image of the food
helplessUserPic = transform.scale(helplessUserPic, (food_width, food_height)) ##makes the variable helplessUserPic have the food dimentions

# FUNCTION(S) FOR MENU
# --------------------

#Menu Page
def drawMenu(screen, button, mx, my, state): ##With the help of Mr. Van Rooyen's code
    screen.blit(roomPic, Rect(0, 0, 1000, 700))                               ##draws the image on the screen
    text = titleFont.render("Strike of the Cyberbullies" , 1, DARK_BLUE)      ##writes the name of the game
    screen.blit(text, Rect(190,130,400,100))                                  ##displays the title at the top of the screen
    blockWidth = width//4.5                                                   ##creates the width of the blocks
    blockHeight = height//10.5                                                ##creates the height of the blocks  
    ##creates a related list for the rectangles
    rectList = [Rect(blockWidth, blockHeight+200, blockWidth, blockHeight),   ##for the game choice
                Rect(blockWidth, 3*blockHeight+200, blockWidth, blockHeight), ##for the help choice
                Rect(blockWidth, 5*blockHeight+200, blockWidth, blockHeight)] ##for the quit choice
    menuStateList = [STATE_GAME, STATE_HELP, STATE_QUIT]                      ##creates a related list for each state of the game
    titleList = ["Play Game", "Help", "Quit Game"]                            ##creates a related list for the labels of the rectangle
    for i in range(len(rectList)):
        rect = rectList[i]                                  ##to get the current rectangle
        draw.rect(screen, YELLOW, rect)                     ##displays the rectangle on the screen
        text = bodyFont.render(titleList[i] , 1, BLACK)	    ##displays the labels
        textWidth, textHeight = bodyFont.size(titleList[i]) ##ensures all rectanlges have the same font size
        useW = (blockWidth - textWidth)//2                  ##used for centering the width
        useH = (blockHeight - textHeight)//2                ##used for centering the height
        ##getting a centered Rectangle
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)           ##displays it on the screen
        if rect.collidepoint(mx, my): 
            draw.rect(screen, BLACK, rect, 2) ##outlines the rectlangle where the mouse is facing
            if button == 1:                   ##when the button is clicked, the user gets transported to their desired state
                state = menuStateList[i]  
    return state



# FUNCTIONS FOR HELP AREA
# -----------------------

#Rules
def createRules ():
    startX_pos, startY_pos = 100, 340 ##starting position for the rules
    width, height = 400, 100          ##width and the height for the rules
    text = bodyFont.render(" -  Drag mouse to move up and down" , 1, DARK_GREEN, WHITE)	                    ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos, width, height))                                          ##displays the rule
    text = bodyFont.render(" -  Go through the wall doors to earn points" , 1, DARK_BROWN, WHITE)           ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos+50, width, height))                                       ##displays the rule underneath the first
    text = bodyFont.render(" -  Touching a bully costs points" , 1, DARK_PURPLE, WHITE)                     ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos+100, width, height))                                      ##displays the rule underneath the the previous rule      
    text = bodyFont.render(" -  Hitting a wall costs a life" , 1, BLUE, WHITE)                              ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos+150, width, height))                                      ##displays the rule underneath the previous rule
    text = bodyFont.render(" -  Touch another user to add more points" , 1, ORANGE, WHITE)                  ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos+200, width, height))                                      ##displays the rule underneath the previous rule
    text = bodyFont.render(" - You have three lives" , 1, DARK_RED, WHITE)	                            ##writes the rule
    screen.blit(text, Rect(startX_pos, startY_pos+250, width, height))                                      ##displays the rule underneath the previous rule
    text = bodyFont.render(" - If points are lost and score reaches zero, game over" , 1, DARK_PINK, WHITE) ##writes the rule        
    screen.blit(text, Rect(startX_pos, startY_pos+300, width, height))                                      ##displays the rule
 
#Help Page  
def drawHelp(screen, button, mx, my, state, i):    
    screen.blit(laptopPic, Rect(0, 0, 1000, 700))     ##draws the image on the screen 
    text = titleFont.render("How to Play" , 1, BLACK) ##writes the title of the page    
    screen.blit(text, Rect(355, 70, 400, 100))        ##displays the title of the page
    ##writes and displays the background information
    text = bodyFont.render("You are being cyberbullied." , 1, DARK_PURPLE, WHITE) 
    screen.blit(text, Rect(250, 170, 400, 100))
    text = bodyFont.render("Escape the bullies and get to an adult who you can talk to." , 1, DARK_PURPLE, WHITE)	
    screen.blit(text, Rect(100, 220, 400, 100))    
    createRules () ##displays the rules functions created earlier
    ##displays the game components
    screen.blit(bullyPic, Rect(900, i, bully_width, bully_height))            ##image of bully
    drawLives (935, i - 80)                                                   ##image of the lives
    screen.blit(helplessUserPic, Rect(900, i - 200, food_width, food_height)) ##image of the food
    drawLives (935, i - 250)                                                  ##image of the lives
    drawDoor (900, i - 400)                                                   ##image of the door
    drawLives (935, i - 450)                                                  ##image of the lives
    screen.blit(UserPic, Rect(910, i-550, userRad, userRad))                  ##image of user
    ##used when the user wants to go back to the menu
    text = smallFont.render("<< Right Click to Go Back to Menu", 1, DARK_PINK, WHITE)	
    screen.blit(text, Rect(10, 20, 400, 100))      
    if button == 3:
        state = STATE_MENU
    return state


# FUNCTIONS FOR GAME/INTERMISSION 
# -------------------------------

#Intermission
def drawIntermission(screen, button, mx, my, state, numLives, score):
    screen.blit(endGamePic, Rect(0, 0, 1000, 700))                   ##draws the image as the background of the page       
    if numLives == 0 or score == 0:                                  ##creates the guideline for the two ways the user could die
        text = titleFont.render("GAME OVER!", 1, DARK_PINK, WHITE)   ##tells the user the reason for the intermission
        screen.blit(text, Rect(350, 300, 400, 100))                  ##displays the text
    else:                                                            ##creates the guideline that the user has not died
        if level == 2:                                               ##creates the guideline that is must be level 2 to show the information
            text = titleFont.render("Level 2!", 1, DARK_PINK, WHITE) ##tells the user the reason for the intermission
            screen.blit(text, Rect(350, 300, 400, 100))              ##displays the text
        elif level == 3:                                             ##creates the guideline that is must be level 2 to show the information
            text = titleFont.render("LEVEL 3!", 1, DARK_PINK, WHITE) ##tells the user the reason for the intermission
            screen.blit(text, Rect(350, 300, 400, 100))              ##displays the text
        else:                                                        ##creates the guideline that the user has won (the level is neither 2 or 3)
            text = titleFont.render("YOU WIN!", 1, DARK_PINK, WHITE) ##tells the user the reason for the intermission
            screen.blit(text, Rect(350, 300, 400, 100))              ##displays the text
            text = bodyFont.render("You found an adult to talk to!", 1, DARK_PINK, WHITE) ##tells the user the reason for the intermission
            screen.blit(text, Rect(200, 600, 400, 100))              ##displays the text
    ##used when the user wants to go back to the menu
    text = smallFont.render("<< Right Click to Go Back to Menu", 1, DARK_PINK, WHITE) 	
    screen.blit(text, Rect(10, 20, 400, 100))
    time.wait (5000) ##displays the page for 5 seconds
    ##ensures that there is a way for the user to go back to the menu
    if button == 3:
        state = STATE_MENU      
    event.get ()
    display.flip ()

#Levels
def drawLevels ():
    ##Lists the global variables reuqired in this function
    global running
    global level 
    global wall
    ##creates the guideline that the score is greater than the maximum score for that specific level
    if score >= maxLevelScore[level-1]: ##the to access each component, the level must be subtracted by one because the levels do not start at zero (index=level-1)
        if level == len(maxLevelScore): ##creates the guideline that the level is the length of the maxLevelScore list
            level += 1                  ##adds level by one to access the "else" portion of the drawIntermission function
            drawIntermission (screen, button, mx, my, state, numLives, score) ##draws the intermission
            level -= 1                  ##restores the changed level
            running = False             ##ends game
        else:                           ##creates the guideline for anything that did not fulfill the first one
            level += 1                  ##moves the user up one level
            if level == 2:              ##creates the guideline that the level is 2
                wall = []               ##initializing wall with new objects
                ##Wall List Variables
                wall1 = [firstbackx, wall_width, firstSpacePlace, space_height, DARK_BLUE, 0, visible] ##in the 6th element, 0 is wall and 1 means food 
                wall2 = [secondbackx, wall_width, secondSpacePlace, space_height, DARK_GREEN, 0, visible]
                wall3 = [thirdbackx, wall_width, thirdSpacePlace, space_height, DARK_PINK, 0, visible]
                ###Food List Variables
                food1 = [food1x, food_width, food1y, food_height, ORANGE, 1, visible]
                food2 = [food2x, food_width, food2y, food_height, ORANGE, 1, visible]
                food3 = [food3x, food_width, food3y, food_height, ORANGE, 1, visible]
                ##draw the components of the following level
                wall.append(wall1)
                wall.append(food1)
                wall.append(wall2)
                wall.append(food2)
                wall.append(wall3)
                wall.append(food3)                
            elif level == 3:            ##creates the guideline that the level is 3
                wall = []               ##initializing wall with new objects
                ##Wall List Variables
                wall1 = [firstbackx, wall_width, firstSpacePlace, space_height, DARK_BLUE, 0, visible] ##in the 6th element, 0 is wall and 1 means food 
                wall2 = [secondbackx, wall_width, secondSpacePlace, space_height, DARK_GREEN, 0, visible]
                wall3 = [thirdbackx, wall_width, thirdSpacePlace, space_height, DARK_PINK, 0, visible]
                ###Food List Variables
                food1 = [food1x, food_width, food1y, food_height, ORANGE, 1, visible]
                food2 = [food2x, food_width, food2y, food_height, ORANGE, 1, visible]
                food3 = [food3x, food_width, food3y, food_height, ORANGE, 1, visible]
                ##Bully List Variables
                bully1 = [bully1x, bully_width, bully1y, bully_height, PURPLE, 2, visible]
                bully2 = [bully2x, bully_width, bully2y, bully_height, PURPLE, 2, visible]
                bully3 = [bully3x, bully_width, bully3y, bully_height, PURPLE, 2, visible]  
                ###draw the components of the following level
                wall.append (wall1)
                wall.append (food1)
                wall.append (bully1)
                wall.append (wall2)
                wall.append (food2)
                wall.append (bully2)
                wall.append (wall3)
                wall.append (food3)
                wall.append (bully3)
            drawIntermission (screen, button, mx, my, state, numLives, score) ##draws the intermission 

#Score Box
def drawScores (score):                                        ##a function to display the user's progress
    scoreBoxHeight = 30                                        ##height of score box
    scoreBoxWidth = 350                                        ##width of score box
    scoreRatio = scoreBoxWidth//int(maxLevelScore[level-1])    ##width of score box divided by score 0 is the ratio that all of the score numbers must be multiplied with
    scoreWidth = score * scoreRatio                            ##the width of rectangle to display the user's score
    text = bodyFont.render("Score", 1, BLACK)                  ##labels the image as the score
    screen.blit(text, Rect(500, 650-scoreBoxHeight, 400, 100)) ##displays the text
    draw.rect (screen, YELLOW, (360, 680-scoreBoxHeight, scoreBoxWidth, scoreBoxHeight))   ##displays the target score
    draw.rect (screen, ORANGE, (360, 680-scoreBoxHeight, scoreWidth, scoreBoxHeight))      ##displays the user's progress
    draw.rect (screen, BLACK, (360, 680-scoreBoxHeight, scoreBoxWidth, scoreBoxHeight), 4) ##outlines the target    
    
#Lives   
def drawLives (x, y): ##a function to display the number of lives in the game through hearts
    draw.polygon (screen, RED, ((x,y), (x-3,y-7), (x-12,y-7), (x-15,y), (x-15,y+12), (x,y+21), (x+15,y+12), (x+15,y), (x+12,y-7), (x+3,y-7)))      ##draws a heart
    draw.polygon (screen, BLACK, ((x,y), (x-3,y-7), (x-12,y-7), (x-15,y), (x-15,y+12), (x,y+21), (x+15,y+12), (x+15,y), (x+12,y-7), (x+3,y-7)), 2) ##outlines the heart

#Scoreboard
def drawScoreboard (numLives): 
    scoreboardY = height - scoreboard_height ##Used to calculate the starting "y" position of the scoreboard
    ##displays the background of the scoreboard
    draw.rect(screen, PURPLE, (0, scoreboardY, width, scoreboard_height))
    draw.rect(screen, DARK_PURPLE, (0, scoreboardY, width, scoreboard_height), 2)  
    ##used when the user wants to go back to the menu
    text = smallFont.render("<< Right Click to go to Menu", 1, DARK_PINK, WHITE)
    screen.blit(text, Rect(10, 660, 400, 100)) 
    ##displays the score
    drawScores (score)     
    ##displays the number of user's lives
    if numLives >= 1: 
        drawLives (895, 660) 
        if numLives >= 2:
            drawLives (935, 660)            
            if numLives == 3:
                drawLives (975, 660)

#Doors
def drawDoor (startX, startY):
    space = wall_width // 10                                                                              ##space between each side of the door
    door_width = ((wall_width *3) // 7) + 1                                                               ##creates the door's width
    door_height = space_height - (space*2)                                                                ##created the door's height
    draw.rect(screen, BROWN, (startX, startY, wall_width, space_height))                                  ##door frame
    draw.rect(screen, BLACK, (startX, startY, wall_width, space_height), 2)                               ##outline of door frame
    draw.rect(screen, DARK_BROWN, (startX, startY + space, door_width, door_height))                      ##left door
    draw.rect(screen, BLACK, (startX, startY + space, door_width, door_height), 2)                        ##outline of left door
    draw.rect(screen, DARK_BROWN, (startX + door_width + space, startY + space, door_width, door_height)) ##right door
    draw.rect(screen, BLACK, (startX + door_width + space, startY + space, door_width, door_height), 2)   ##outline of right door
    
#Food
def drawFood (colour, x, y, w, h, visibility):
    if visibility == 1:                                ##Creates the guideline that the food is visible
        screen.blit(helplessUserPic, Rect(x, y, w, h)) ##draws image of the food
        draw.rect(screen, colour, (x, y, w, h), 3)     ##outlines the image
        
#Bully
def drawBully (colour, x, y, w, h, visibility):
    if visibility == 1:                             ##Creates the guideline that the bully is visible
        screen.blit(bullyPic, Rect(x, y, w, h))     ##draws image of the bully
        draw.rect (screen, colour, (x, y, w, h), 3) ##outlines the image

#Game Page
def drawGame(screen, button, mx, my, state, firstbackx, secondbackx, thirdbackx, numLives): 
    ##Draws Background
    screen.blit(socialmediaPic, Rect(0, 0, 1000, 700)) ##draws the background image on the screen
    drawScoreboard (numLives)                          ##draws the scoreboard
    ##Walls
    for i in range (0, len(wall)):                     ##creates a for loop for the length of the wall list
        if wall[i][5] == 0:                            
            draw.rect(screen, wall[i][4], (wall[i][0], 0, wall[i][1], screen_height)) ##wall1
    ##Draws Functions
    for i in range (0, len(wall)):                                                             ##draws the functions in relation to which wall type the user comes across
        ##the fifth element is the wallType
        if wall[i][5] == 0:                                                                    ##creates the guideline that the wallType is a wall (the wallType for a wall is 0)  
            ##draws the function corresponding to the wallType
            drawDoor (wall[i][0], wall[i][2])                                                  ##inside the function are the x and y coordinates of the space
        elif wall[i][5] == 1:                                                                  ##creates the guideline that the wallType is food (the wallType for food is 1) 
            ##draws the function corresponding to the wallType
            drawFood (wall[i][4], wall[i][0], wall[i][2], wall[i][1], wall[i][3], wall[i][6])  ##inside (in order) are the colour, x coordinate, y coordinate, width of the image, height of the image, and the visibility
        elif wall[i][5] == 2:                                                                  ##creates the guideline that the wallType is a wall (the wallType for a wall is 0) 
            ##draws the function corresponding to the wallType
            drawBully (wall[i][4], wall[i][0], wall[i][2], wall[i][1], wall[i][3], wall[i][6]) ##inside (in order) are the colour, x coordinate, y coordinate, width of the image, height of the image, and the visibility
    ##Character
    draw.circle(screen, BLACK, mouse, userRad)  
    ##Used when the user wants to go back to the menu
    if button == 3:
        state = STATE_MENU
    return state 
running = True
myClock = time.Clock()

# initializing (and reinitializing) variables
state = STATE_MENU
screen_height = 600
scoreboard_height = height - screen_height
level = 1
speed = 10
numLives = 3
## Score Variables
maxLevelScore = [20, 40, 60]
## Mouse Variables
mousex = 100
my = 0
mx = mousex 
## Visibility Variables
visible = 1
invisible = 0
## Wall Variables
firstbackx = width 
secondbackx = width+333
thirdbackx = width+666
wall_width = 70
stateWall = 0
hitWallType = 0
## Food Variables
#Note: The following is called food because the user gains points when 'eating' them, but the purpose of them is to teach the user to help others that are being cyberbullies
food1x = firstbackx + wall_width + 61
food2x = secondbackx + wall_width + 61
food3x = thirdbackx + wall_width + 61
food1y = 100
food2y = 200
food3y = 300
food_width = 70
food_height = 70
## Bully Variables
bully1x = firstbackx + wall_width + 162
bully2x = secondbackx + wall_width + 162
bully3x = thirdbackx + wall_width + 162
bully1y = 300
bully2y = 100
bully3y = 200
bully_width = 70
bully_height = 70
## Space Variables
space_height = 100
firstSpacePlace = (random.randint(0, screen_height-space_height))
secondSpacePlace = (random.randint(0, screen_height-space_height))
thirdSpacePlace = (random.randint(0, screen_height-space_height))
## User's Variables
userRad = 15
userRight = mx + userRad
userLeft = mx - userRad
userTop = my - userRad
userBottom = my + userRad
## wall List Variables
#Note: The following lists are all related lists that have the same indexes to make the code easier to understand and more efficient
###Wall List Variables
wall1 = [firstbackx, wall_width, firstSpacePlace, space_height, DARK_BLUE, 0, visible] 
wall2 = [secondbackx, wall_width, secondSpacePlace, space_height, DARK_GREEN, 0, visible]
wall3 = [thirdbackx, wall_width, thirdSpacePlace, space_height, DARK_PINK, 0, visible]
###Food List Variables
food1 = [food1x, food_width, food1y, food_height, ORANGE, 1, visible] 
food2 = [food2x, food_width, food2y, food_height, ORANGE, 1, visible]
food3 = [food3x, food_width, food3y, food_height, ORANGE, 1, visible]
###Bully List Variables
bully1 = [bully1x, bully_width, bully1y, bully_height, DARK_PURPLE, 2, visible]
bully2 = [bully2x, bully_width, bully2y, bully_height, DARK_PURPLE, 2, visible]
bully3 = [bully3x, bully_width, bully3y, bully_height, DARK_PURPLE, 2, visible]
## Creates the Large List
wall = []
wall.append (wall1)
wall.append (wall2)
wall.append (wall3)
wallIndex = 0 ##variable to help with the index of the wall

# Game Loop
while running: ##Some parts are taken from Mr. Van Rooyen's code for a game loop
    button = 0
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos          
            button = e.button
        elif e.type == MOUSEMOTION:
            mx,my = e.pos
            mouse = []
            mx = mousex ##this is the x position that the mouse will always be in during the game
            mouse.append(mx)
            mouse.append(my)
    if state == STATE_MENU:                                                                            ##creates the guideline that the state is the menu
        state = drawMenu(screen, button, mx, my, state)                                                ##makes the state the menu function
    elif state == STATE_HELP:                                                                          ##creates the guideline that the state is the help area
        state = drawHelp(screen, button, mx, my, state)                                                ##makes the state the help function
    elif state == STATE_GAME:                                                                          ##creates the guideline that the state is the game
        state = drawGame(screen, button, mx, my, state, firstbackx, secondbackx, thirdbackx, numLives) ##makes the state the game function
        for i in range (0, len(wall)):          ##causes the wall to move 
            wall[i][0] -= speed                 ##subtracts the x value of each list by the speed
            if wall[i][0] + wall[i][1] <= 0:    ##creates the guideline that the x-value related variables in the list become negetive (and off of the screen)
                wall[i][0] = width - wall[i][1] ##brings the wall back to the right side of the screen      
                wall[i][6] = visible            ##makes the object visible
        ##defines the variables of the user using the user's currect y position
        userTop = my - userRad 
        userBottom = my + userRad
        ##defines the top and bottom of the spaces using the wall listand the wallIndex
        spaceTop = wall[wallIndex][2]               ##the y position of the list
        spaceBottom = spaceTop + wall[wallIndex][3] ##this is the sum of the spacetop and the height
        ##defines the left and right of the wall using the wall list and the wall index 
        wallLeft = wall[wallIndex][0]                       ##This is the starting x position
        wallRight = wall[wallIndex][0] + wall[wallIndex][1] ##This is the starting x position plus the width
        wallType = wall[wallIndex][5]                       ##the fifth element is the wallType, which is there to differentiate between each of small the lists
        if stateWall == 0:           ##creates the guidline that the stateWall must be zero 
            if wallLeft < userRight: ##if the user has entered the object
                stateWall = 1        ##resets the variable
        else:                        ##if the stateWall is one
            if userLeft > wallRight: ##if the user can passed through the object
                if hitWallType == 0: ##if the user hit an object
                    if wallType == 0:                       ##referring to the door
                        score += 4                          ##adds to the score by four
                        drawScores (score)                  ##updates the score function
                        drawLevels ()                       ##runs it through the draw levels function
                        if score == maxLevelScore[2]:       ##in case the new score is the maximum score
                            state = STATE_INTERMISSION      ##brings in to the intermission function that will display the new level to the user
                    elif wallType == 1:                   ##referring to the food
                        wall[wallIndex][6] = invisible    ##after the user touches the food, the food should disappear
                        score += 6                        ##adds to the by six 
                        drawScores (score)                ##updates the score function
                        drawLevels ()                     ##runs it through the draw levels function
                        if score == maxLevelScore[2]:     ##in case the new score is the maximum score
                            state = STATE_INTERMISSION    ##brings into the intermission function that will display the new level to the user                      
                    elif wallType == 2:                 ##referring to the bully
                        wall[wallIndex][6] = invisible  ##after the user touches the bully, the bully should disappear
                        score -= 6                      ##deducts score by six         
                        if score == 0:                  ##in case the score is zero
                            state = STATE_INTERMISSION  ##brings it to the intermission to display the game is over
                        drawScores (score)              ##updates the score function 
                else: ##if the user did not hit a object
                    if wallType == 0:                   ##referring to the door
                        numLives -= 1                   ##deducts the number of lives
                        if numLives == 0:               ##in case the number of lives is zero
                            state = STATE_INTERMISSION  ##brings into the intermission to display the game is over
                    ##the following is for a coherent if statement
                    elif wallType == 1:                 ##referring to the food
                        pass
                    elif wallType == 2:                 ##referring to the bully
                        pass
                wallIndex += 1             ##to check for the next portion of the list
                if wallIndex == len(wall): ##creates the guideline that the index has reached the end of the list
                    wallIndex = 0          ##resets the index
                ##resets variables
                stateWall = 0
                hitWallType = 0
            else:
                if (spaceTop < userTop and userBottom < spaceBottom): 
                    pass
                else:
                    hitWallType = 1   ##resets the hitWallType as one
    elif state == STATE_INTERMISSION: ##creates the guidline that the state is the intermission area
        state = drawIntermission(screen, button, mx, my, state, numLives, score)  ##draws the intermission section of the code     
    else: ##if the user is in none of the listed states, the game quits
        running == False
    event.get()    
    display.flip()
    myClock.tick(60)                     # waits long enough to have 60 fps
quit()