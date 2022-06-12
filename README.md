# PinballMachine
This is a Python pinball machine created by Carol and Emily.
We used the turtle library in Python to create our project.
Our game starts when the ball on the right side of the board is launched. The player can change the velocity of the initial launch by pressing the space key where more presses will generate a faster launch. The color of the launcher also shows how fast the ball will move where the colors progresses in the following order: green, yellow, orange, red.
The ball will first move up the tube at a constant velocity and curve over to the main board where all of the obstacles and flippers are. There, gravity will act on it and pull it down the board at a constant acceleration. This acceleration is not equal to 9.81 m/s^2 because our board is tilted at a 10º angle.
When the ball hits an obstacle that is completely black, it will bounce back without losing any momentum. Since the black obstacles are fixed in place, this type of collision will only cause the direction of the ball's motion to change.
When the ball hits an obstacle with a red surface, it will bouce back with a faster velocity. This is because the red and black obstacles have an internal spring that will cause the ball to gain kinetic energy and thus have a faster velocity.
The game is over when the ball falls past the flippers or into one of the two chutes on the left and right sides of the main board.
The game can be continued when the player uses the flippers to keep the ball up. The player should not press the flippers too many times and should only press each of them one time only when using it to keep the ball up.
The score will be calculated from the number of obstacles you hit where hitting different obstacles will generate different scores.
