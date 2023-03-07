import pvporcupine
import pyaudio
import numpy as np

api_key = 'btcm2GWGR3F5pVYFhJp5baI9pv7wPAdnQZ/SBLbrtchZewhRXqcCrw=='

porcupine = pvporcupine.create(
  access_key=api_key,
  keywords=['picovoice', 'bumblebee']
)

CHUNK = 512 # Buffer size
FORMAT = pyaudio.paInt16 # Audio format
CHANNELS = 1 # Mono sound
RATE = 44100 # Sample rate
p = pyaudio.PyAudio() # PyAudio object

audio = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# print('show audio devices', porcupine.show_audio_devices())
print('listening... (press Ctrl+C to exit)')

while True:
    pcm = stream.read(CHUNK)
    pcm = np.frombuffer(pcm, dtype=np.int16)
    
    keyword_index = porcupine.process(pcm)
    
    if keyword_index >= 0:
        if keyword_index == 0:
            print('picovoice')
        elif keyword_index == 1:
            print('bumblebee')
            break
        else:
            print('unknown keyword')
            
stream.stop_stream()
stream.close()
porcupine.delete()