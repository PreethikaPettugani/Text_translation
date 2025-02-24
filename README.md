# Text_translation
This repository contains a Python script that translates text from English into multiple target languages using Hugging Face's Marian Machine Translation models. The implementation leverages the powerful transformers library and supports translations into Spanish, French, German, and Chinese.
# Requirements
* Python 3.7 or above
* Transformers
* LangChain (for prompt templates)
* python-doten
# Acknowledgments
* **Hugging Face**: For providing state-of-the-art machine translation models.
* **LangChain**: For tools that help with prompt management.
# Code Overview
* **TranslationChain** Class:
Encapsulates the initialization of the MarianMT model and tokenizer. It includes a translate method that takes input text, processes it, and returns the translated text.
* **create_translation_chain** Function:
Determines the correct translation model for the target language by referring to the language_models dictionary.
* **translate_text_to_multiple_languages** Function:
Iterates over a list of target languages, creates a translation chain for each, and returns a dictionary of translations.
* **Prompt Template**:
Although not used directly in the translation process, the script sets up a LangChain PromptTemplate that can be expanded for more advanced prompt management in the future.

  
