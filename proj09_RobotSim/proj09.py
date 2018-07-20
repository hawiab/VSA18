# proj09: Simulating robots
# Name:
# Date:

import math
import random
import proj09_visualize
# import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # defining width, height, and creating the floor
        self.width = width
        self.height = height
        self.floor = self.createtiles(width, height)

    # this function creates a list of dirty tiles
    def createtiles(self, width, height):
        listoftiles = []
        for x in range(width):
            for y in range(height):
                listoftiles.append([x,y,"dirty"])
        return listoftiles

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #getting the position
        x = int(pos.getX())
        y = int(pos.getY())
        #
        for tile in self.floor:
            if tile[0] == x and tile[1] == y:
                tile[2] = "clean"
        return self.floor

    def isTileCleaned(self, x, y):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        x = int(pos.getX())
        y = int(pos.getY())
        for tile in self.floor:
            if tile[0] == x and tile[1] == y:
                if tile[2] == 'clean':
                    return True
                else:
                    return False
        raise NotImplementedError

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        numtiles = self.width*self.height
        return numtiles

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        counter = 0
        for tile in self.floor:
            if tile[2] == 'clean':
                counter = counter + 1
        return counter

    def getRandomPosition(self, width, height):
        """
        Return a random position inside the room.

        returns: a Position object.
        """

        randomx  = random.randint(0, width)
        randomy = random.randint(0,height)
        randcoord = Position(randomx, randomy)
        return randcoord

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        for Robot in self.floor:
            if Robot in pos:
                return True
            else:
                return False

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room.cleanTileAtPosition(self.position)
        if speed > 0:
            self.speed = speed
        self.direction = int(360*random.random())
        self.position = getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError



# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if Robot.isPositionInRoom == False:
            self.direction = self.direction + 180
        if Robot.isTileCleaned(self.position) == True:
            self.position = Robot.getRobotDirection(self, self.direction, self.speed)
        else:
            Robot.cleanTileAtPosition(self, self.position)
            self.position = Robot.getRobotDirection(self, self.direction, self.speed)
        return self.position

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    robots = []
    counter = 0
    room = RectangularRoom(width, height)
    while num_trials != 0:
        anim = proj09_visualize.RobotVisualization(num_trials,width,height)
        if num_robots > 0:
            while counter <= num_robots:
                if robot_type == 'standard':
                    room = RectangularRoom(width, height)
                    stanrobot = StandardRobot(room, speed)
                    robots.append(stanrobot)
                    counter = counter + 1
        if min_coverage * room.getNumTiles() == room.getNumCleanedTiles():
            num_trials = num_trials - 1
        anim.done()

# === Problem 4

#
# 2) How long does it take two robots to clean 80% of rooms with dimensions


# def showPlot1():
#     """
#     Produces a plot showing dependence of cleaning time on number of robots.
#     """
#     raise NotImplementedError
#
# def showPlot2():
#     """
#     Produces a plot showing dependence of cleaning time on room shape.
#     """
#     raise NotImplementedError
#
# # === Problem 5
#
# class RandomWalkRobot(Robot):
#     """
#     A RandomWalkRobot is a robot with the "random walk" movement strategy: it
#     chooses a new direction at random after each time-step.
#     """
#     raise NotImplementedError
#
#
# # === Problem 6
#
# # For the parameters tested below (cleaning 80% of a 20x20 square room),
# # RandomWalkRobots take approximately twice as long to clean the same room as
# # StandardRobots do.
# def showPlot3():
#     """
#     Produces a plot comparing the two robot strategies.
#     """
#     raise NotImplementedError
#
avg = runSimulation(10,1.0,15,20,0.8,2,'standard')