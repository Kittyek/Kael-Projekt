def listen_to_user():
    try:
        import speech_recognition as sr

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            print("[Speech] Lausche deiner Stimme...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="de-DE")
            print(f"🗣 Antwort: Ich habe verstanden: {text}")
        except sr.UnknownValueError:
            print("[Speech] Konnte nichts verstehen.")
        except sr.RequestError as e:
            print(f"[Speech] Anfrage fehlgeschlagen: {e}")

    except Exception as e:
        print("[Speech] (Simulation) Lausche... (auf Replit deaktiviert)")
