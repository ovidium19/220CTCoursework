'''
import csv
f=open('c:/Student/220CT/Task4/autosTestWEKA.csv','r')
reader=csv.DictReader(f) #eliminate all comments
l=list(reader)
f.close()
#convert all numeric values to ints - proves how easy it is to do it
#with mongoDB compared to an RDBMS
for doc in l:
    for key in doc.keys():
        try:
            doc[key]=int(doc[key])
        except ValueError:
            continue
######################################################################  
'''    
import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.usedcars
#results = db.usedcars.delete_many({})
#results = db.usedcars.insert_many(l)
'''
cursor=db.usedcars.aggregate([
    {
        "$group":{
            "_id":"$price",
            "count":{"$sum":1}}}])

cursor=db.usedcars.aggregate([
    {
        "$group":{
            "_id":"$brand",
            "averageprice":{"$avg":"$price"}}}])

cursor=db.usedcars.aggregate([
    {
        "$group":{
            "_id":"$yearOfRegistration",
            "averageprice":{"$avg":"$price"}}}])

cursor=db.usedcars.aggregate([
    {"$group":{"_id":"$yearOfRegistration","count":{"$sum":1}}}])

cursor=db.usedcars.aggregate([
    {"$group":{"_id":"$gearbox","avg":{"$avg":"$price"}}}])

cursor=db.usedcars.aggregate([
    {"$group":{"_id":"$notRepairedDamage","avg":{"$avg":"$adTime"}}}])

cursor=db.usedcars.aggregate([
    {
        "$group":{
            "_id":"$brand",
            "count":{"$sum":1}}}])
'''
#Query for a list of all brands and how many cars of that brand have been sold
#each day (day1, day2, day3 etc.)
cursor=db.usedcars.aggregate([
    {"$match":{"adTime":{"$lt":20}}},
    {
        "$group":{
            "_id":{"brand":"$brand","adTime":"$adTime"},
            "count":{"$sum":1}}}])
#save the list in a csv file
import csv
keys=["adTime","brand","count"]
with open('autosQuery12.csv','wt') as f:
    dict_writer = csv.DictWriter(f,keys)
    dict_writer.writeheader()
    for doc in cursor:
        doc["adTime"]=doc["_id"]["adTime"]
        doc["brand"]=doc["_id"]["brand"]
        doc.pop("_id",None)
        dict_writer.writerow(doc)
    f.close()
