import pymongo
import bcrypt
import requests

# client = pymongo.MongoClient("mongodb+srv://YingzhouJiang:Jyz1996!@cluster0.zkmuv24.mongodb.net/?retryWrites=true&w=majority")
# db = client['ufit_test']
# collection = db['accounts']

# print(collection.find_one({"name": "Yingzhou Jiang"}))

url = 'https://data.mongodb-api.com/app/data-lxgvr/endpoint/data/v1'
database = 'ufit_test'
collection = 'accounts'

api_key = 'J0OZyynWUPdjoXFECl9Jg0eFBWqAVTlEh4xPEeBKSMnrVFe5Jpq2oWgBKkMqEdna'
headers = {'Content-Type': 'application/json', 'Access-Control-Request-Headers': '*', 'X-API-Key': api_key}





def add_user(name, password, email):
    # Check if email already exists
    if collection.find_one({"email": email}):
        print("Email already exists")
        return False
    
    # Check if password is valid
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return False
    
    # hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        collection.insert_one({"name": name, "password": hashed_password, "email": email})
    except:
        raise Exception("Error inserting user")
    
    return True

def login(email, password):
    # hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Check if email exists
    if not collection.find_one({"email": email}):
        print("Email does not exist")
        return False
    
    user = collection.find_one({"email": email})

    # Check if password is correct
    if hashed_password != user["password"]:
        print("Incorrect password")
        return False
    
    return user