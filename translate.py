import os
from dotenv import load_dotenv
from transformers import MarianMTModel, MarianTokenizer
from langchain import LLMChain, PromptTemplate

load_dotenv()

language_models = {
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Chinese": "Helsinki-NLP/opus-mt-en-zh",
}

class TranslationChain:
    def __init__(self, model_name):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        try:
            inputs = self.tokenizer(text, return_tensors="pt")
            translated = self.model.generate(**inputs)
            print("tsranslated_output:",translated[0])
            translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
            return translated_text
        except Exception as e:
            return f"Error: {str(e)}"

translation_prompt = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following text to {language}: {text}"
)

def create_translation_chain(language):
    model_name = language_models.get(language)
    if model_name:
        return TranslationChain(model_name)
    else:
        raise ValueError(f"Translation model for language '{language}' not found")

def translate_text_to_multiple_languages(text: str, languages: list):
    translations = {}
    for language in languages:
        try:
            translation_chain = create_translation_chain(language)
            translated_text = translation_chain.translate(text)
            translations[language] = translated_text
        except Exception as e:
            translations[language] = f"Error: {str(e)}"
    return translations

if __name__ == "__main__":
    text_to_translate = "Hello, how are you?"
    target_languages = ["Spanish", "French", "German", "Chinese"]

    translations = translate_text_to_multiple_languages(text_to_translate, target_languages)
    for language, translation in translations.items():
        print(f"Translated Text ({language}): {translation}")
