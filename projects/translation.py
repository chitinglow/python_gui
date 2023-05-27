# import goslate
# inserted_text = "Python is so powerful"
# new_gs = goslate.Goslate()
# new_gs.translate(inserted_text, 'es')

# from translate import Translator
# translator = Translator(from_lang='english', to_lang='spanish')
# translation = translator.translate("This is a translation")
# print(translation)
#

from textblob import TextBlob

adding_blob = TextBlob("Easy to translate")
adding_blob.translate(to='ar')