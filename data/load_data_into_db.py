import pymongo

client = pymongo.MongoClient("mongodb+srv://mongouser:cse6242@cluster0-tlpzm.mongodb.net/test?retryWrites=true&w=majority")
db = client["cse6242project"]

collection = db["job_skill_set"]

print(db)
