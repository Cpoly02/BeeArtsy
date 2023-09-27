# BeeArtsy
BeeArtsy is a web application created for artists to quickly retrieve images for drawing references. This project was made using Python and Flask. 

# Description
This website uses user-inputted information to make requests to two APIs. The images are gathered and then displayed to the user one by one in between a timed interval in which the user is expected to draw the image. By using APIs, the user is granted the freedom 
of entering any subject type they would like and should receive varied results each search. During the practice poriton of the application, the user is able to skip to previous or upcoming images and can pause/resume the timer. Once finished, the user will 
be brought to a final page where all the images they recieved will be displayed for easy viewing. 

# Getting Started 
## Dependencies 
* Python
* Flask
* Numpy
* Requests

## API Keys 
To properly run this website, you need to acquire the API keys from Pexels and Unsplash. 
* [Pexels](https://www.pexels.com/api/)
* [Unsplash](https://unsplash.com/documentation#creating-a-developer-account)

## Inputting keys 
After acquiring the keys, go to the project folder api/keys.py and paste your keys inside the correspending string. 
<p align="center">
  <img src="https://github.com/Cpoly02/BeeArtsy/assets/90474907/48daa601-1da9-46c7-955e-d28a00ff3fcb"/>
</p>

## Run the web app 
To run the website, go to main.py and run the application in your IDE. This will launch the development server and you should be able to access the application by inputting the address printed to the terminal. 
<p align="center">
  <img src="https://github.com/Cpoly02/BeeArtsy/assets/90474907/daaa5a64-8f1b-424d-b59a-adc5e393b170"/>
</p>
