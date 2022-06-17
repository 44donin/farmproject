
from pymongo import MongoClient
from pymongo.common import clean_node

from deep_translator import GoogleTranslator

def GetTranslated(text,language_code):
    Translated = GoogleTranslator(source='auto',target=language_code)
    return Translated.translate(text)

    

def GetExpertSuggestion(district,crop,language):
    client = MongoClient('mongodb+srv://tesairo:saiteja@doninfarmerinitiative.forxd.mongodb.net/doninfarmerinitiative?retryWrites=true&w=majority')
    database = client['doninfarmerinitiative']
    collection = database['information']
    name = str(district).title()
    crop_name = str(crop).lower()
    title_array = []
    info_local_lang_array = []
    info_array = []
    for info in collection.find({'district':name,'0':{"$regex":".*" + crop_name +".*"}}):
        title = None
        result = None
        if(str(info["2"]) == "nan"):
            result = info['1'].replace('\n','')
        else:
            title = info['1']
            result = info['2'].replace('\n','')
        if(title == None):
            title = "No Title" 
        title_array.append(title)
        info_local_lang_array.append(GetTranslated(result,GoogleTranslator.get_supported_languages(as_dict=True)[language]))
        info_array.append(result)  
    data = {
        "titles" : title_array,
        "information_in_local_languages" : info_local_lang_array,
        "information" : info_array,
        "language_code" : GoogleTranslator.get_supported_languages(as_dict=True)[language]
    }
    return data
    
