# Monochrome-Converter-OpenCV
Monochrome-Converter-OpenCV is a repository with a Python script that takes an image input from the user and converts it to grayscale using OpenCV. The user is prompted to enter the file path of the input image and the desired file path to save the converted image. The converted image is displayed in a window titled "Grayscale". The user is then prompted to press the 's' key to save the converted image to the specified file path, or any other key to close the window and exit the program.

The code first takes input from the user for the file path of the input image and the desired file path to save the converted image. It then reads in the input image using cv2.imread() and converts it to grayscale using the flag 0. The cv2.resize() function is used to resize the image to a specified size of 1000x600 pixels. The converted grayscale image is then displayed in a window titled "Grayscale" using cv2.imshow().

The user is prompted to press the 's' key to save the converted image to the specified file path. If the 's' key is pressed, the converted image is saved to the specified file path using cv2.imwrite(). If any other key is pressed, the window is closed and the program exits using cv2.destroyAllWindows().

This code can be used as a template for converting images to grayscale and saving the converted images to a desired file path. The user input prompts can be modified as necessary to suit specific use cases.




