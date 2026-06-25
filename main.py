from RealtimeSTT import AudioToTextRecorder

def on_text(text):
    print(text)

if __name__ == '__main__':
    recorder = AudioToTextRecorder(model="base", language="en")
    print("Speak into your mic...")
    while True:
        recorder.text(on_text)