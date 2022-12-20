import json
import ssl
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

context = ssl.create_default_context()

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

def englishtofrench(english_text):
    try:
        response = language_translator.translate(text=english_text, model_id="en-fr")
        translation = response.get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    except:
        return ""

def frenchtoenglish(french_text):
    try:
        response = language_translator.translate(text=french_text,model_id="fr-en")
        translation = response.get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except:
        return ""

    

print(english_to_french(None))