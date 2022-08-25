""""
    translate english to french
    """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ded2bfca-3556-497c-a568-db1eec8fb986')


def englishToFrench(englishText):
    """"
    translate english to french
    """
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation["translations"][0]["translation"]
    return frenchText


def frenchToEnglish(frenchText):
    """"
    translate french to english
    """
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation["translations"][0]["translation"]
    return englishText

if __name__ == "__main__":
    print(englishToFrench("Hello world"))
    print(frenchToEnglish("Bonjour le monde"))
