import time
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def search_google(search_query, driver):
    # Abrir una nueva pestaña
    driver.execute_script("window.open('');")
    # Cambiar el enfoque a la nueva pestaña
    driver.switch_to.window(driver.window_handles[-1])
    # Navegar a Google y realizar la búsqueda
    driver.get("https://www.google.com/")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    speak("La búsqueda ha sido realizada. Abriendo resultados en una nueva pestaña.")

def recognize_speech():
    recognizer = sr.Recognizer()

    # Configuración del navegador
    driver = webdriver.Chrome()  # Asegúrate de tener Chrome y el ChromeDriver instalados

    while True:
        with sr.Microphone() as source:
            print("Diga 'buscar' seguido de su consulta, o 'salir' para terminar:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Reconocer la consulta
            query = recognizer.recognize_google(audio, language="es-EC")
            print(f"Ha dicho: {query}")

            if "buscar" in query.lower():
                # Eliminamos la palabra 'buscar' de la consulta
                search_query = query.lower().replace("buscar", "").strip()
                search_google(search_query, driver)
            elif "salir" in query.lower():
                speak("Saliendo del programa.")
                break
            else:
                speak("No he detectado una opción válida en su consulta.")

        except sr.UnknownValueError:
            print("No se pudo reconocer lo que dijo.")
        except sr.RequestError:
            print("No se pudo conectar con el servicio de reconocimiento de voz.")

if __name__ == "__main__":
    recognize_speech()





