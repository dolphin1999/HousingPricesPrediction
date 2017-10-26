

from collections import OrderedDict
import csv


DIC = {"ID": "0000", "GARDEN SPACE" : "1","DOCK" : "0.0","Capital" : "0.0","Royal Market":"0.0","Guarding Tower" : "0.0","River" : "0.0","Renovation":"0","bedrooms":"0","dining rooms":"0","bathrooms":"0","pay":"1","sorcerer":"1","blessings":"0","tree":"0","Knights house" : "0.0", "Location":"No Location","farm":"0","Date Built Y" : 0, "Date Priced Y":0, "Date Priced M":0, "Date Built M":0, "Time1":0,"Time2":0,"Meridian1":1,"Meridian2":1}


LIST= sorted(DIC)
     


csvfile = open('DataTrain.csv', 'a') 
spamwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
#spamwriter.writerow(LIST)
f = open("Wood_Priests.txt","r")
data = f.readlines()

def row(Dic):
     lst = []
     for key in LIST:
          if key in Dic:
               lst.append(Dic[key])
          else :
               lst.append(DIC[key])
     return lst


def lol1(strng):
     if "House ID" in strng:
          for word in strng.split():
               if len(word) >= 2:
                    if word[0] == '6' and word[1] == 'e':
                         return {"ID" : word}
     elif "There is no space for garden" in strng:
          return {"GARDEN SPACE" : "0"}
     elif "Dock" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"DOCK" : word}
     elif "Capital" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"Capital" : word}
     elif "Royal Market" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"Royal Market" : word}
     elif "Guarding Tower" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"Guarding Tower" : word} 
     elif "River" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"River" : word}
     elif "did not undergo renovation" in strng:
          return {"Renovation" : "0"} 
     elif "underwent renovation upon Mighty King's command" in strng:
          return {"Renovation" : "1"}
     elif ("bedrooms" in strng) or ("bedroom" in strng):
          for word in strng.split():
               if word.isdigit():
                    return {"bedrooms":word}
     elif ("dining rooms"  in strng) or ("dining room" in strng):
          for word in strng.split():
               if word.isdigit():
                    return {"dining rooms":word}
     elif ("bathrooms" in strng) or ("bathroom" in strng):
          for word in strng.split():
               if word.isdigit():
                    return {"bathrooms":word}
     elif "King couldn't pay his visit to the house" in strng:
          return {"pay":"0"}
     elif "Sorcerer couldn't curse this house" in strng:
          return {"sorcerer" :"0"}
     elif ("blessings"  in strng) or ("blessing" in strng):
          for word in strng.split():
               if word.isdigit():
                    return {"blessings":word}
     elif "Holy tree stands tall beside the house" in strng:
          return {"tree":"1"}
     elif "Location of the house is" in strng:
          cnt = 0
          word1 = ""
          for word in strng.split():
               if word == ":":
                    cnt = 1
               elif cnt == 1:
                    if word1 == "":
                         word1 = word
                    else :
                         word1 = word1 + " " + word
          return {"Location":word1}

     elif "Distance from Knight's house" in strng:
          #pattern = re.compile("^[^\s]*.[^\s]*$")
          for word in strng.split():
               if len(word) >= 1:
                    if word[0].isdigit():
                         return {"Knights house" : word}
     elif "There is a small land of farm in the front" in strng:
          return {"farm":"1"}
     elif "There is a huge land of farm in the front" in strng:
          return {"farm":"2"} 
     elif "Date Built" in strng:
          i = 1
          word1 = ""
          word2 = ""
          word3 = ""
          word4 = ""
          word5 = ""
          word6 = ""
          word7 = ""
          word8 = ""
          for word in strng.split():

               if i == 4:
                    
                    l = len(word)
                    word1 = word[(l-4):l]
                    cnt1 = 0
                    for j in word:
                         if j == '/':
                              break
                         word3 = word3 + j
                    
               
               elif i == 11:
                    l = len(word)
                    word2 = word[(l-4):l]
                    cnt1 = 0
                    for j in word:
                         if j == '/':
                              break
                         word4 = word4 + j

               elif i == 5:
                    for j in word:
                         if j != ':':
                              word5 = word5 + j
                         elif j == ':':
                              word5 = word5 + '.'

               elif i == 12:
                    for j in word:
                         if j != ':':
                              word6 = word6 + j
                         elif j == ':':
                              word6 = word6 + '.'
               elif i == 6:
                    if word == "AM":
                         word7 = 1
                    else:
                         word7 = 0
               elif i == 13:
                    if word == "AM":
                         word8 = 1
                    else:
                         word8 = 0
               
               
               
               

               i =  i+1
          return {"Date Built Y" : word1, "Date Priced Y":word2, "Date Priced M":word4, "Date Built M":word3, "Time1":word5,"Time2":word6,"Meridian1":word7,"Meridian2":word8}

     
          
                    
     else:
          return {}




dic = {}
cnt = 0
for line in data:
     if line == "\n" and dic != {}:
          spamwriter.writerow(row(dic))     
          dic = {}
          #cnt = cnt+1;
          #break
          print cnt
     print line
     
     if lol1(line):
          dic1 = lol1(line)
          print dic1
          dic.update(dic1)
          print dic
     

   

     
     

     
     
         


