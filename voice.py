from TTS.api import TTS
import os
import time

print("=" * 50)
print("🎙️ XTTS v2 - USER INTERACTIVE MODE")
print("=" * 50)

# Load model (optimized for CPU if no GPU found)
print("\n🔄 Loading Model... Please wait...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
print("✅ Model Loaded Successfully!")

while True:
    # 1. Get Text Input
    print("\n" + "=" * 50)
    print("📝 Enter text to convert (or type 'exit' to quit):")
    user_text = input("> ").strip()
    
    if user_text.lower() == 'exit':
        print("\n👋 Goodbye!")
        break
    
    if not user_text:
        continue

    # 2. Language Selection
    print("\n📋 Supported Language Codes:")
    print("   - hi (Hindi)    - en (English)  - es (Spanish)")
    print("   - fr (French)   - de (German)   - ja (Japanese)")
    print("   - ko (Korean)   - zh-cn (Chinese)")

    lang_code = input("\nLanguage Code [default: hi]: ").strip().lower() or "hi"

    # Quick fix for users entering '1' instead of 'hi'
    if lang_code == "1":
        lang_code = "hi"

    # 3. Voice Selection
    speaker_wav = "sample.wav" 
    if not os.path.exists(speaker_wav):
        print(f"❌ Error: {speaker_wav} not found! Please place a sample.wav in the folder.")
        break

    output_file = "output.wav"

    # 4. Generate with Performance Monitoring
    print(f"\n🎵 Generating speech in '{lang_code}'... Please wait...")
    start_time = time.time()

    try:
        tts.tts_to_file(
            text=user_text,
            speaker_wav=speaker_wav,
            language=lang_code,
            file_path=output_file
        )
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        print("-" * 50)
        print(f"✅ Voice Generated Successfully!")
        print(f"⏱️  Processing Time: {processing_time:.2f} seconds")
        print(f"💾 Saved as: {output_file}")
        print("-" * 50)

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Hint: Check if the language code is correct and text is not too long.")

