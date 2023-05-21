import sounddevice
from scipy.io.wavfile import write

seconds = int(input('How many seconds you need to record:  '))
print("Recording Started...")

recording = sounddevice.rec((seconds*44100), channels=2)

sounddevice.wait()
file_name = input('Give the name to save: ')
write(file_name, 44100, recording)
print("Recording Finished")