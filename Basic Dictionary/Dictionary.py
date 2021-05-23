import json
from difflib import get_close_matches,SequenceMatcher
#Now loading dictionary data with json
file=open('data.json')
dictionary=json.load(file)
def translate(word):
    #Handeling case and stripping
    w=word.lstrip().rstrip().lower()
    word_list=dictionary.keys()
    if w in word_list:
        return dictionary[w]
    #Now for special cases where word like Texas is there but not text
    elif w.title() in word_list:
        return dictionary[w.title()]
    #Now for handeling country name like USA,BD etc
    elif w.upper() in word_list:
        return dictionary[w.upper()]
    #If word not directly then find closest one
    elif len(get_close_matches(w,word_list))>0:
        #Now we will ask the user if it's the desired word
        pred=get_close_matches(w,word_list)[0]   
        #print(pred)
        yon=input("Did you mean "+pred+"instead, if yes press y otherwise press n")
        if yon.lower()=='y':
            return dictionary[pred]
        elif yon.lower()=='n':
            return "The word doesn't exist in the dictionary"
        else:
            return "We didn't understand your entry"
    else:
        return 'The word doesnot exist in the dictionary'
    


#Now inputting data
output=translate(input('Enter the word: '))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)