from TTS.api import TTS
import os
 
print("Loading XTTS Model... Please wait")
 
# Load model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
 
print("Model Loaded Successfully!")
 
# Telugu text input
text = "नमस्कार, आज हम एक आधुनिक टेक्नोलॉजी का उपयोग कर रहे हैं जिसे टेक्स्ट टू स्पीच कहा जाता है। इस तकनीक की मदद से हम लिखे हुए शब्दों को एक प्राकृतिक आवाज़ में बदल सकते हैं। यह तकनीक शिक्षा, मनोरंजन और बिज़नेस में बहुत उपयोगी साबित हो रही है।"
 
# Your voice sample path
speaker_wav = "sample.wav"
 
# Output file
output_file = "output.wav"
 
# Generate speech
tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wav,
    language="hi",
    file_path=output_file
)
 
print("Voice Generated Successfully!")
print("Saved as output.wav")