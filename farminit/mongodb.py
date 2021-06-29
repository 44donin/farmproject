
from pymongo import MongoClient, collation, collection


def GetExpertSuggestion(district,crop):
    client = MongoClient('mongodb+srv://tesairo:saiteja@doninfarmerinitiative.forxd.mongodb.net/doninfarmerinitiative?retryWrites=true&w=majority')
    database = client['doninfarmerinitiative']
    collection = database['information']
    name = str(district).title()
    crop_name = str(crop).lower()
    data = []
    for info in collection.find({'district':name,'0':{"$regex":".*" + crop_name +".*"}}):
        title = None
        result = None
        if(str(info["2"]) == "nan"):
            result = info['1']
        else:
            title = info['1']
            result = info['2']        
        proffesor_suggestion = {
            "title" : title,
            "info"  : result
        } 
        data.append(proffesor_suggestion)
    return data
    
