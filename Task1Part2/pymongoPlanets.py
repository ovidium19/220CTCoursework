#import csv
#f=open('c:/Student/220CT/planets.csv','r')
#reader=csv.DictReader(filter(lambda row: row[0]!="#",f)) #eliminate all comments
#l=list(reader)
#f.close()
##convert all numeric values to floats - proves how easy it is to do it
#with mongoDB compared to an RDBMS
#for doc in l:
#    for key in doc.keys():
#        try:
#            doc[key]=float(doc[key])
#        except ValueError:
#            continue
######################################################################  
        
import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.exoplanets

#results = db.exoplanets.insert_many(l)


#Prints all planets found by Imaging, prints name, jmass, eqt and tradur
#cursor=db.exoplanets.find(
#    {"pl_discmethod":"Imaging"})
#for doc in cursor:
#    print("name: " + doc["pl_hostname"],end=" ")
#    print("jupiter_mass: " +str(doc["pl_massj"]),end=" ")
#    print("pl_eqt: "+str(doc["pl_eqt"]),end=" ")
#    print("pl_trandur: "+str(doc["pl_trandur"]),end=" ")
#    print()



#prints the average eqt for all planets, grouped by method of discovery
cursor=db.exoplanets.aggregate([
    {"$match": {"pl_eqt": {"$exists":True,"$ne":""}}},
    {"$group": {"_id":"$pl_discmethod", "avg_temp": {"$avg": "$pl_eqt"}}}
    ])
for doc in cursor:
    print(doc)




