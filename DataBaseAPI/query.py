import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["RcuetProject"]
devices_collection = mydb["Devices"]

myquery = {"room_name": "phòng ngủ"}

mydoc = devices_collection.find(myquery)
count = devices_collection.count_documents(myquery)


print(type(count))
