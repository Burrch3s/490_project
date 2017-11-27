# 490_project
My project forConfers cs490 research project. Components include Raspberry Pi, BerryIMU, and Chuck.

The project senses rapid movements and/or tilt (depending on the mode its in) and interprets the data. 
Then, the program will interpret a command to be sent wirelessly to my laptop (over a python pseudo 
netcat connection) where my receiving program shall execute the command and create/adjust sounds
synthesized or fed to the chuck program. :ok_hand:

#TODO

- finish first mode: interpret sudden acceleration into punches in chuck
    solder berryIMU
    collect sensor data
    present data and correlate data to gesture/movement
    
- finish second mode: interpret tilt/rotation into increase in freq./amplitude
    (Pi side)
    detect then compile command into chuck program adjustment
    (Laptop side)
    execute chuck cmd and file
    
#IMPROVEMENTS
- solder berryIMU together, get battery pack for Pi to make it a crappy wearable (lol)
- idk wait a bit come back and write more
- write the second mode and allow seamless switching between the 2
- use some audio software to get rid of trail of silence before and after punch noise
- fine tune difference between punch and not reg. movement
