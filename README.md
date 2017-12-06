# 490_project
My project forConfers cs490 research project. Components include Raspberry Pi, BerryIMU, and Chuck.

The project senses rapid movements and/or tilt (depending on the mode its in) and interprets the data. 
Then, the program will interpret a command to be sent wirelessly to my laptop (over a python pseudo 
netcat connection) where my receiving program shall execute the command and create/adjust sounds
synthesized or fed to the chuck program. :ok_hand:

#What is all this??
    project_accel.py:
        - one of the main projects, detects accelerometer sensor readings and sends off command
            to run chuck to listener
            
    project_tilt.py:
        - one of the main projects, detects tilt readings in degrees, maps them to ranges from -80 to
            130 degrees into a note to be executed. Must have netcat listener on receiving system and
            chuck running in headless mode by running chuck --loop

    netcat directory:
        - contains netcat class that is used by project scripts to send off instructions
        - should be either used by the project scripts themselves, or imported from python interpreter
            (
              calling from interpreter use cases are for setting up a listener to execute commands
              or for sending off commands via buffer variable buf, interactive user input was removed
              for script functionality
            )
    
    laptop-side directory:
        - contains: wav files that chuck runs for punches, chuck scripts that are translated to chuck
            opcodes and run by the chuck vm
        - should be either used by calling the .ck scripts from the project .py files, or fed to chuck 
            vm directly to test out :ok_hand:
            
    pi-side directory:
        - contains ozzmaker default scripts that initialize the sensors and display data (we modify 
            these scripts as seen in project_accel.py and project_tilt.py)
            
    LSM9DS0.py:
        - contains important register and peripheral memory addresses used by project scripts
    
    data_collection.py/data_collection_tilt.py:
        - modified project scripts to only detect sensor readings and write out to a file for latter
            proccessing
            
    test.py:
        - testing network connection from client to listener
        
#TODO
 
    
#IMPROVEMENTS
- idk wait a bit come back and write more
- allow seamless switching between the 2 modes
- use some audio software to get rid of trail of silence before and after punch noise
- fine tune difference between punch and not reg. movement (velocity of changing tilt to note)
