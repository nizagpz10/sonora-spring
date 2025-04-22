import cv2 #opencv library for video processing
import mediapipe as mp #media pipe for hand tracking
import pygame #pygame library for sound handling
import numpy as np #imports numpy

# Initialize mixer for audio playback
pygame.mixer.init()

# Loads voice notes
notes = {
    'V1': pygame.mixer.Sound("sonoravnotes/V1.wav"),
    'V2': pygame.mixer.Sound("sonoravnotes/V2.wav"),
    'V3': pygame.mixer.Sound("sonoravnotes/V3.wav"),
    'V4': pygame.mixer.Sound("sonoravnotes/V4.wav"),
    'V5': pygame.mixer.Sound("sonoravnotes/V5.wav"),
    'V6': pygame.mixer.Sound("sonoravnotes/V6.wav"),
    'V7': pygame.mixer.Sound("sonoravnotes/V7.wav"),
    'V8': pygame.mixer.Sound("sonoravnotes/V8.wav")
}

# Track note states
global finger_states
finger_states  = {k: False for k in notes}
trigger_states = {k: False for k in notes} #flags from off to on
playing_states = {k: False for k in notes} #is note playing? flag

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils

def stop_all_notes():
    global finger_states
    for note, playing in finger_states.items():
        if playing:
            notes[note].stop()
            playing_states[note] = False
            trigger_states[note] = False

def play_note_based_on_fingers(hand_landmarks, hand_index):
    global finger_states

    # Thumb: tip index 4, MCP knuckle index 2
    tip_y = hand_landmarks.landmark[4].y
    mcp_y = hand_landmarks.landmark[2].y
    if tip_y > mcp_y:
        stop_all_notes()
        return

    if hand_index == 0:
        # Left hand: V1-V4
        if hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and not finger_states['V1']:
            notes['V1'].play()
            finger_states['V1'] = True
        else:
            finger_states['V1'] = False

        if hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and not finger_states['V2']:
            notes['V2'].play()
            finger_states['V2'] = True
        else:
            finger_states['V2'] = False

        if hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and not finger_states['V3']:
            notes['V3'].play()
            finger_states['V3'] = True
        else:
            finger_states['V3'] = False

        if hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y and not finger_states['V4']:
            notes['V4'].play()
            finger_states['V4'] = True
        else:
            finger_states['V4'] = False

    else:
        # Right hand: V5-V8
        if hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y and not finger_states['V5']:
            notes['V5'].play()
            finger_states['V5'] = True
        else:
            finger_states['V5'] = False

        if hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and not finger_states['V6']:
            notes['V6'].play()
            finger_states['V6'] = True
        else:
            finger_states['V6'] = False

        if hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and not finger_states['V7']:
            notes['V7'].play()
            finger_states['V7'] = True
        else:
            finger_states['V7'] = False

        if hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and not finger_states['V8']:
            notes['V8'].play()
            finger_states['V8'] = True
        else:
            finger_states['V8'] = False

# Video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            play_note_based_on_fingers(hand_landmarks, idx)

    cv2.imshow('Hand Gesture Music Player', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
