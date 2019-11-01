#https://www.python-course.eu/python3_class_and_instance_attributes.php
# add the comment for test brach, can it be seen?

class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @staticmethod
    def RobotInstances():
        return Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    y = Robot()
    print(x.RobotInstances())
    #print(Robot.RobotInstances())
    #print(y.RobotInstances())
    #print(Robot.RobotInstances())
    #x = Robot()
    #print(x.RobotInstances())
    #print(Robot.RobotInstances())
