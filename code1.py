


import csv
'''
with open('DataTrain.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
    
    spamwriter.writerow(["ID", "GAREN SPCAE","DOCK","CAPITAL","ROYAL MARKET","GUARDING TOWER","RIVER","RENOVATION","BEDROOM","DINING","BATHROOM","pay","SORCERER","BLESSINGS","TREE","KNIGHT KING"]) 


'''

DIC = {"ID": "0000", "GARDEN SPACE" : "1","DOCK" : "0.0","Capital" : "0.0","Royal Market":"0.0","Guarding Tower" : "0.0","River" : "0.0","Renovation":"0.0","bedroom":"0","dining rooms":"0","bathroom":"0","pay":"1","sorcerer":"1","blessings":"0","tree":"0","Knights house" : "0.0"}






csvfile = open('DataTrain.csv', 'wb') 
spamwriter = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
f = open("Bob.txt","r")
data = f.readlines()

def row(Dic):
     lst = []
     for key in DIC:
          if key in Dic:
               lst.append(Dic[key])
          else :
               lst.append(DIC[key])
     return lst
 
    
def lol1(strng):
     if "House ID" in strng:
          for word in strng:
               if word == "6e*":
                    return {"ID" : word}
     elif "There is no space for garden" in strng:
          return {"GARDEN SPACE" : "0"}
     elif "Dock" in strng:
          for word in strng:
               if word == "*.*":
                    return {"DOCK" : word}
     elif "Capital" in strng:
          for word in strng:
               if word == "*.*":
                    return {"Capital" : word}
     elif "Royal Market" in strng:
          for word in strng:
               if word == "*.*":
                    return {"Royal Market" : word}
     elif "Guarding Tower" in strng:
          for word in strng:
               if word == "*.*":
                    return {"Guarding Tower" : word} 
     elif "River" in strng:
          for word in strng:
               if word == "*.*":
                    return {"River" : word}
     elif "did not undergo renovation" in strng:
          return {"Renovation" : "0"} 
     elif "underwent renovation upon Mighty King's command" in strng:
          return {"Renovation" : "1"}
     elif "bedroom" in strng:
          for word in strng:
               if isDigit(word):
                    return {"bedroom":word}
     elif "dining rooms" in strng:
          for word in strng:
               if isdigit(word):
                    return {"dining rooms":word}
     elif "bathrooms" in strng:
          for word in strng:
               if isdigit(word):
                    return {"bathrooms":word}
     elif "King couldn't pay his visit to the house" in strng:
          return {"pay":"0"}
     elif "Sorcerer couldn't curse this house" in strng:
          return {"sorcerer" :"0"}
     elif "blessings" in strng:
          for word in strng:
               if isdigit(word):
                    return {"blessings":word}
     elif "Holy tree stands tall beside the house" in strng:
          return {"tree":"1"}
     elif "Distance from Knight's house" in strng:
          for word in strng:
               if word == "*.*":
                    return {"Knights house" : word} 

dic = {}
for line in data:
     if line == "" and dic != {}:
          spamwriter.writerow(row(dic))     
          dic = {}
          break
     #print line
     dic1 = lol1(line)
     #dic.update(dic1)



     

     
     

     
     
         


