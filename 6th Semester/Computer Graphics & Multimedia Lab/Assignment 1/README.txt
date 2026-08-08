OpenGL Assignment – Magenta Window
Assignment Title

Creating a Magenta Colored OpenGL Window with a Custom Window Name and Keyboard Control

Objective

The objective of this assignment is to create an OpenGL window using GLFW and GLAD that:

Displays a magenta-colored background.
Uses the student's full name as the window title.
Closes when the user presses the first letter of their name.
Student Information

Name: Raiyan Rahim Fahad
Window Closing Key: F

Requirements

The program must:

Initialize GLFW.
Create an OpenGL 3.3 Core Profile window.
Set the window title to Raiyan Rahim Fahad.
Set the background color to magenta.
Detect keyboard input.
Close the window when the R key is pressed.
Implementation
Window Title

The window title was changed to:

GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "Raiyan Rahim Fahad", NULL, NULL);
Magenta Background

The magenta background is created using:

glClearColor(1.0f, 0.0f, 1.0f, 1.0f);
Keyboard Input

The program closes when the R key is pressed:

if(glfwGetKey(window, GLFW_KEY_R) == GLFW_PRESS)
    glfwSetWindowShouldClose(window, true);
Expected Output

When the program runs:

The window title will be Raiyan Rahim Fahad.
The window will have a magenta background.
Pressing R will close the window.
Technologies Used
C++
OpenGL 3.3
GLFW
GLAD
Visual Studio Code
Conclusion

This assignment demonstrates the basic setup of an OpenGL application using GLFW and GLAD. It also demonstrates how to change the window title, set a background color, and handle keyboard input.