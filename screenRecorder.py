import cv2
import numpy as np
import pyaudio
import av
import pyautogui

# Set the video and audio parameters
VIDEO_CODEC = 'mpeg4'
VIDEO_FPS = 30
VIDEO_WIDTH, VIDEO_HEIGHT = pyautogui.size()

AUDIO_FORMAT = pyaudio.paInt16
AUDIO_CHANNELS = 2
AUDIO_RATE = 44100
AUDIO_CHUNK_SIZE = 1024

# Create the video writer object
video_writer = cv2.VideoWriter('screen_recording.avi', cv2.VideoWriter_fourcc(*VIDEO_CODEC), VIDEO_FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))

# Create the audio recorder object
audio_recorder = pyaudio.PyAudio()
audio_stream = audio_recorder.open(format=AUDIO_FORMAT, channels=AUDIO_CHANNELS, rate=AUDIO_RATE, input=True, frames_per_buffer=AUDIO_CHUNK_SIZE)

# Start the screen capture loop
while True:
    # Capture the screen content
    screen_content = np.array(pyautogui.screenshot())
    
    # Encode the screen content and write it to the video file
    video_writer.write(screen_content)
    
    # Record the audio stream and add it to the video file
    audio_data = audio_stream.read(AUDIO_CHUNK_SIZE)
    audio_frame = av.AudioFrame.from_ndarray(np.fromstring(audio_data, np.int16), format='s16', layout='stereo', rate=AUDIO_RATE)
    video_writer.write(audio_frame)
    
# Release resources
video_writer.release()
audio_stream.stop_stream()
audio_stream.close()
audio_recorder.terminate()
