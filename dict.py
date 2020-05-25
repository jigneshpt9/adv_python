import json
import pickle

if __name__ == '__main__':
   dict = { 'a': 1, 'b':2, 'c':3 }
   str = json.dumps(dict)
#   print(type(str))
 

   with open("dictw",'wb') as file:
      pickle.dump(dict,file)

   with open("dictw", 'rb') as file:
      dict2=pickle.load(file) 
      print(type(dict2))
