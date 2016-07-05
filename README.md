![e-Yantra Summer Internship](http://www.e-yantra.org/img/EyantraLogoLarge.png)
***
# eYSIP-2016-Autonomous-Drone
Through this project we want to make an Autonomous Drone that can travel from one point to another based on its GPS Location. This drone can be used for tracking objects and aerial photography when interfaced with an Object Tracking Camera system.

Autonomous Drone project uses the following components:
* **Flight Controller:** Ardupilot Flight Controller (APM 2.6)
* **Copter Firmware:** v3.2.1
* **Communication Protocol:** MAVLink, MAVProxy, UART
* **Ground Station System (Software):** Mission Planner v1.3.30
* **Programming Language:** (Python 2.7)
* **Companion Computer:** Raspberry Pi B+ model

##Description:
***
The latest technology currently in markets is the Drone Technology, Drones can solve a lot of purposes such as security & surveillance, mapping unreachable or hard to reach sites, aerial photography, military purposes, forest survey, etc. So, we have created a drone which is completely autonomous as well as it can be manually controlled with laptop using remote login.

##Features:
***
- **Auto Take-off and Land:** The Drone can automatically take-off to a desired height, wait at that height for a predetermined time and then land.
- **Manual control using remote-login:** User can manually control the drone using the keyboard keystrokes of the laptop using remote login with raspberry pi.
- **Autonomous flight between multiple points:** The drone can autonomously take-off complete a mission and land either at the start position or your desired position. A mission is a set of locations where you want your drone to go. The drone gets the locations from the GPS module interfaced with the APM board.
- **Indoor auto take-off and land using ultrasonic sensor:** The drone also has an Ultrasonic sensor interfaced with Raspberry Pi which can be used for take-off and land indoors, where the altitude the drone needs to reach is just few meters.
- **Failsafe:** The APM has smart failsafe features which include low battery voltage failsafe, remote signal lost. So, with these failsafe features you can either put your drone into landing mode or else if you have a GPS module you can even have Return To Launch feature and also many more options are provided.

##Key Tasks
***
> Calculations for selecting motors, propellors, flight controller, battery for a Quadcopter
> Building and assembling the drone
> Stabilizing the drone for manual as well as autonomous control
> Interfacing Raspberry Pi with APM  flight controller
> Develop python codes to achive autonomous behaviour of drone

##Documentation
***
> Detailed tutorials with actual component pictures on every module of the project have been uploaded on GitHub.

##Deliverables
***
> An Autonomous Drone
> Code and Documentation
> Tutorials explaining individual modules


##Contributors
***
  * [Akshit Gandhi](https://github.com/akshitgandhi)
  * [Keyur Rakholiya](https://github.com/keyurrakholiya)
  
## Mentors
***
  > Pushkar Raj
  > Akshat Jain
  > Rama Kumar

##License
***
This project is open-sourced under [MIT License](http://opensource.org/licenses/MIT)