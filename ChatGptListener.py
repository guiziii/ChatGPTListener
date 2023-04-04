import openai
import speech_recognition as sr
import pyttsx3
import webbrowser
import os

url = 'https://www.google.com'
urlY = 'https://www.youtube.com'
urlDevAzure = 'https://dev.azure.com/'
urlDocReact = 'https://react.dev/'
urldolar='https://www.google.com/search?q=dolar'
urlMui = 'https://mui.com/material-ui/getting-started/overview/'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
openai.api_key = "<OPENAI_API_KEY>"
engine = pyttsx3.init()

def volume_down():
  os.system('amixer -D pulse sset Master 5%-')

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language='pt-BR')
    except:
        print("Skipping unknown error")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response["choices"][0]["text"]


def speak_text(text, Falar):
    if Falar == True:
        engine.setProperty('rate', 280)
        engine.say(text)
        engine.runAndWait()

def main():
    Falar = True

    while True:
        print("\nDiga 'Ronaldo' para conversar com o Chat GPT")

        with sr.Microphone() as source:

            recognizer = sr.Recognizer()
            audio = recognizer.listen(source, phrase_time_limit=5, timeout=1000)
            try:
                transcription = recognizer.recognize_google(audio, language='pt-BR')
                print(transcription)

                if transcription.lower() == 'ronaldo reiniciar computador':
                    os.system("shutdown /r")

                if transcription.lower() == 'ronaldo pode falar':
                    Falar = True;

                if transcription.lower() == 'ronaldo não falar':
                    Falar = False;

                if transcription.lower() == 'volume médio':
                    print(" -> Diminuindo volume")
                    volume_down()

                if transcription.lower() == 'abra o controle':
                    print(" -> Abrindo painel de controle")
                    os.system('control')

                if transcription.lower() == 'abra o sublime':
                    os.system('sublime')

                if transcription.lower() == 'abra o google':
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(url)

                if transcription.lower() == 'documentação do react':
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(urlDocReact)

                if transcription.lower() == 'abra o youtube':
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(urlY)

                if transcription.lower() == 'documentação material':
                    speak_text('Abrindo página de documentação do Material-UI',Falar)
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(urlMui)

                if transcription.lower() == 'valor do dólar':
                    speak_text('Abrindo página de pesquisa do dólar',Falar)
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(urldolar)

                if transcription.lower() == 'abra a azure':
                    print(" -> Abrindo navegador")
                    webbrowser.get(chrome_path).open(urlDevAzure)

                if transcription.lower() == 'desligar alarme':
                    print(" -> Desligando alarmes")
                    os.system('Taskkill /F /IM AlarmsNotificationTask.exe')

                if transcription.lower() == 'ronaldo':
                    filename = "input.wav"

                    speak_text('Pergunte qualquer coisa',Falar)

                    print("Say your question")

                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=5, timeout=15)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said {text}")

                        if text == 'esquece':
                            print("Cancel command")
                            raise SyntaxError("Erro de sintaxe")

                        # Generate the response
                        response = generate_response(text)
                        print(f"Chat GPT-3 says: {response}")

                        # Read response using GPT-3
                        speak_text(response,Falar)
            except Exception as e:
                print("An error occurred: {}".format(e))


if __name__ == "__main__":
    main()
