import csv
from datetime import date
f=open("c:/Student/220CT/Task4/autosData/autos.csv",'r')
reader=csv.DictReader(f)
l=list(reader)
print(type(l[0]["dateCreated"]))
for doc in l:
    doc.pop("name",None)
    doc.pop("nrOfPictures",None)
    doc.pop("offerType",None)
    doc.pop("seller",None)
    doc.pop("abtest",None)
    created=doc["dateCreated"][:doc["dateCreated"].find(" ")]
    seen=doc["lastSeen"][:doc["lastSeen"].find(" ")]
    aDate=list(map(int,seen.strip().split("-")))
    bDate=list(map(int,created.strip().split("-")))
    a=date(aDate[0],aDate[1],aDate[2])
    b=date(bDate[0],bDate[1],bDate[2])
    doc["adTime"]=(a-b).days
    doc.pop("dateCreated",None)
    doc.pop("dateCrawled",None)
    doc.pop("lastSeen",None)
    
    
    
f.close()
keys=sorted(l[0].keys())
with open('autosTest4.csv','wt') as f:
    dict_writer = csv.DictWriter(f,keys)
    dict_writer.writeheader()
    for doc in l:
        dict_writer.writerow(doc)
