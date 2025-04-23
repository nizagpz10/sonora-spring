# sonora-spring
Based this code from @john-bennet 's musical fingers proyect and Aditee Gautman's "Hand Detection Tracking in Python using OpenCV and MediaPipe" article on Medium. *Sonora Spring is still in construction, new functionalities will be implemented soon.

Sonora Spring is a program design to track hand movements in order to play notes with each finger and create unique sound patterns.

Each finger tip and joint is tracked using MediaPipe's hand landmarks. Notes are triggered based on finger positions — fingers "lowered" relative to their preceding joints will play a note.

This program includes features like:
- Real-time hand tracking
- Play different audio notes with left and right hands
- Supports 8 unique sounds: `V1.wav` to `V8.wav` (that can be played uniquely on 8 fingers)

+Gesture Mapping
Left hand:
Index ↓ → V1
Middle ↓ → V2
Ring ↓ → V3
Pinky ↓ → V4

Right hand:
Pinky ↓ → V5
Ring ↓ → V6
Middle ↓ → V7
Index ↓ → V8

To exit program press 'q'

//Future functionality implementationsfor Sonora Spring include, stop all notes function to cut all sounds when right thumb is lowered 
and loop note function when left thumb is lowered. 

Thank you for being here!
-Niza

  
