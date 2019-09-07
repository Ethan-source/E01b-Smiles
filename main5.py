#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800 #sets the X axis parameters of the scree
SCREEN_HEIGHT = 600 #sets the Y axis parameters 
SCREEN_TITLE = "Smiley Face Example"

class Faces(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True) 

        self.x = SCREEN_WIDTH / 2   #Divides the screen width by half
        self.y = SCREEN_HEIGHT / 2  #divdes the screen height by half

        arcade.set_background_color(open_color.white) #Sets the backgorund color as white

    def on_draw(self): #command that draws the face
        """ Draw the face """
        arcade.start_render() #nothing renders without this 
        face_x,face_y = (self.x,self.y) 
        smile_x,smile_y = (face_x + 0,face_y - 10) #Draws the coordinates of the smile 
        eye1_x,eye1_y = (face_x - 30,face_y + 20) #These are the coordinates of the left eye
        eye2_x,eye2_y = (face_x + 30,face_y + 20) #These are the coordinates of the right eye
        catch1_x,catch1_y = (face_x - 25,face_y + 25) #draws the dimensions in the left eye
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #draws the dimensions in the right eye

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #Draws the yellow filled portion of the smiley
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #draws tne outline of the smiley face
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #draws the left eye
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black) #draws the right eye
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #Draws the gray dot in the eye
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) #Draws the gray dot in the right eye
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #Draws the smile


    def on_mouse_motion(self, x, y, dx, dy): #Def is a command where you put your own arguments in, and in this case on_mouse_motion tells the code to follow the cursor on the x and y planes.
        """ Handle Mouse Motion """
        self.x = x #follows the cursor on the x axis
        self.y = y #follows the cursor on the y axis 



window = Faces()
arcade.run() #nothing will run without this, it opens the arcade