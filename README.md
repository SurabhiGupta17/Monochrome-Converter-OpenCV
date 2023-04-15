# Monochrome-Converter-OpenCV
Monochrome-Converter-OpenCV is a repository with a Python script that takes an image or a video input from the user and converts it to grayscale using OpenCV. 

**ImgConverter.py**
The user is prompted to enter the file path of the input image and the desired file path to save the converted image. The converted image is displayed in a window titled "Grayscale". The user is then prompted to press the 's' key to save the converted image to the specified file path, or any other key to close the window and exit the program.

The code first takes input from the user for the file path of the input image and the desired file path to save the converted image. It then reads in the input image using cv2.imread() and converts it to grayscale using the flag 0. The cv2.resize() function is used to resize the image to a specified size of 1000x600 pixels. The converted grayscale image is then displayed in a window titled "Grayscale" using cv2.imshow().

The user is prompted to press the 's' key to save the converted image to the specified file path. If the 's' key is pressed, the converted image is saved to the specified file path using cv2.imwrite(). If any other key is pressed, the window is closed and the program exits using cv2.destroyAllWindows().

This code can be used as a template for converting images to grayscale and saving the converted images to a desired file path. The user input prompts can be modified as necessary to suit specific use cases.

**VideoConverter.py**
This Python code uses the OpenCV library to convert a video file or webcam input to grayscale and save the output to a file. The user is prompted to enter the path of the video file to be converted, and the program reads the video using the OpenCV function cv2.VideoCapture(). The code then creates a VideoWriter object to save the grayscale video to a file named "output.avi".

The program then enters a loop where it reads each frame of the video using cap.read(), converts it to grayscale using cv2.cvtColor(), and displays the resulting grayscale frame using cv2.imshow(). The program also writes each original frame to the output file using output.write(). The loop continues until the user presses the 'q' key, at which point the program exits the loop and releases the video and output resources using cap.release() and output.release(), and destroys any open windows using cv2.destroyAllWindows().




