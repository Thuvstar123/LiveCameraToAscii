## Function

This a very simple and short program that is able to convert the live camera feed into an ASCII grayscale image.

It's done by making a grayscale version of each frame, then converting the frame into a 2D list containing rows of pixels
and their respective grayscale values.
Next we use 64 of the many characters in **Paul Bourke's** ASCII grayscale representation. 
Since there are 256 distinct grayscale values, but only 64 grayscale ASCII representations, we take mod 4 of the original
grayscale value.
We effectively then use a range of values for a single ASCII grayscale representation - a many to one relationship.
Finally we simply print out every row once converted and concatenated.

## Purpose

This was just a fun past time project and didn't (expectedly) take long.
It was also made to make sure that if I were to use it again for another project, it would mean I wouldn't have to code
it all again!

## Run Program

Ensure that OpenCV is installed as a library on your IDE. 

If it is not installed, type into terminal:

*pip install opencv-python*

Next, simply run the program and adjust the amount of pixels you want to capture to the left or right of the frame.
This is because different screen resolutions may cause one-line rows of pixels to take up 2 lines, which will mess up the 
image.
