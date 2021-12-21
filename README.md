# StrikeofCyberbullies

Animated graphics of the games were created using the python library pygame. The game was divided into four main states; STATE_MENU, STATE_GAME, STATE_HELP, STATE_QUIT, STATE_INTERMISSION; each defined prior to the initialization of variables and the game loop. The function image.load() was utilized to incorporate online images into the game. Time was kept track of while running using time.Clock().

User must get through the wall doors to earn points by dragging mouse up and down. Touching a 'bully' costs points, touching a 'helpless user' increases points. Hitting a wall costs one of the three lives alloted. Game over if all points are lost and score reaches zero, or if all lives are lost.


