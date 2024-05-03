# Remote-Controlled-Car
Using the Raspberry Pi GPIO pins and Python, I created a remote controlled car connected to my keyboard.  
I used PyGame for the keyboard input
# Process
## Planning
### To create this car, I first made a general layout of the components as follows: 
![Layout](https://github.com/Abdul-Taha/Remote-Controlled-Car/assets/159376482/fcac7501-1324-468a-bbb3-0db8b3b0c474)
### I took measurements of all my parts and their screw holes and proceeded to model a 2D sketch in AutoCAD:
![AutoCAD File](https://github.com/Abdul-Taha/Remote-Controlled-Car/assets/159376482/758df620-05f2-4656-8d6b-f5be96cada5d)
## Assembling
### To create the body, I laser cut my design out of wood and screwed everything together. I added a mounting for a speaker as I have future plans of adding my chatbot to the robot. As for the wiring, I used some tutorials on how to interface with the motor controller I was using, the L298N.
## Issues
### The biggest issue I faced was power. Though I had a 7.4 V battery, I was unable to drive both motors. This could have implied several issues, but I decided to go with the straight-forward solution of attaching a more powerful battery. This was the cheapest solution, as I already had a 14.8 V Lipo battery on standby. Some other issues I had were implementing the driving functionality, as though I could make the basic functions to drive, but when I attached them to my keys, the program was unable to register multiple keys simultaneously, making for an unpleasant driving experience. Luckily, this was not too difficult to solve, and I have future plans to improve the controls.
https://github.com/Abdul-Taha/Remote-Controlled-Car/assets/159376482/b459180e-b035-4571-98cb-0f3564dabfb4
## Demo
https://github.com/Abdul-Taha/Remote-Controlled-Car/assets/159376482/62d8f591-0682-4e2b-9efc-8ead270df75f

