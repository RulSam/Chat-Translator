from googletrans import Translator


def text_translator(text='Hello friend', scr='en', dest='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=scr, dest=dest)

        return translation.text

    except Exception as ex:
        return ex

def main():
    print(text_translator(text='Hello', scr='en', dest='ru'))

if __name__ == '__main__':
        main()