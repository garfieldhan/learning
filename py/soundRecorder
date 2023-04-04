import pyaudio
import wave

# Audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# System audio device index
system_device_index = 0

# Microphone device index
mic_device_index = 1

# Output file name
output_file = "output.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open streams for recording system audio and microphone audio
system_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                       input_device_index=system_device_index, frames_per_buffer=CHUNK)

mic_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                    input_device_index=mic_device_index, frames_per_buffer=CHUNK)

# Start recording
frames = []
for i in range(0, int(RATE / CHUNK * 10)):
    system_data = system_stream.read(CHUNK)
    mic_data = mic_stream.read(CHUNK)
    frames.append(system_data)
    frames.append(mic_data)

# Stop streams
system_stream.stop_stream()
system_stream.close()

mic_stream.stop_stream()
mic_stream.close()

# Save the recorded audio to a WAV file
wf = wave.open(output_file, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

# Terminate PyAudio
p.terminate()
