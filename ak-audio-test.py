import sounddevice as sd
import speech_recognition as sr
import pyaudio
import time

print(sd.query_devices())

CHUNK = 1024 # Buffer size
FORMAT = pyaudio.paInt16 # Audio format
CHANNELS = 1 # Mono sound
RATE = 16000 # Sample rate
p = pyaudio.PyAudio() # PyAudio object

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

r = sr.Recognizer()
r.energy_threshold = 500 # Adjust the microphone sensitivity level
# r.operation_timeout = 1 # Set the maximum time to wait for a response from the speech recognition engine
r.pause_threshold = 0.5 # Set the minimum length of silence before a phrase is considered complete

keyword = 'start'

def on_result(results):
    for result in results:
        transcript = result.alternatives[0].transcript
        print(transcript)
        if keyword in transcript:
            print('keyword detected')
            break


# Set the recognizer language and the speech recognition engine
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # Perform noise reduction
    print("Say something!")
    while True:
        print('listening...')
        audio = r.listen(source)
        print(audio)
        try:
            text = r.recognize_google(audio) # Use Google Speech Recognition engine
            print("You said: {}".format(text))
            
            if 'start' in text and 'exercise' in text:
                print('Starting exercise...')
                time.sleep(2)
            if 'stop' in text and 'exercise' in text:
                print('Stopping exercise...')
                time.sleep(2)
            if 'pause' in text:
                print('Pausing exercise...')
                time.sleep(2)
            if  'surface' in text:
                print('Capture back surface...')
                time.sleep(2)
            if 'exit' in text:
                print('Exiting...')
                time.sleep(2)
                break
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


stream.stop_stream()
stream.close()
p.terminate()
