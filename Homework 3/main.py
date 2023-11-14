import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS 

DB_PATH = "./HW3.db"

# api 
app = Flask(__name__)
CORS(app, resources=r'/api/*')

#utils
def gen_response(data):
    response = {
            "data": data
        }
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#users CRUD
def get_user(id):
    query = f"""SELECT username, role, created_at
    FROM users where id='{id}'"""
    
    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    user_details = list(cursor.execute(query))
    if len(user_details) != 0:
        user_details = user_details[0]
    connection.close()
    return user_details

def create_user(username, role):
    query = f"""INSERT INTO users(username, role)
    VALUES('{username}', '{role}')"""

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def update_user(id, username, role):
    query = f"""UPDATE users
    SET username = '{username}', role = '{role}' where id='{id}' """

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def delete_user(id):
    query = f"""DELETE FROM users
    where id='{id}'"""

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

#follows CRUD
def get_user_followers(id):
    query = f"""SELECT  following_user_id , followed_user_id
    FROM follows where following_user_id='{id}'"""
    
    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    user_details = list(cursor.execute(query))
    if len(user_details) != 0:
        user_details = user_details[0]
    connection.close()
    return user_details

def get_user_following(id):
    query = f"""SELECT  following_user_id , followed_user_id
    FROM follows where followed_user_id='{id}'"""
    
    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    user_details = list(cursor.execute(query))
    if len(user_details) != 0:
        user_details = user_details[0]
    connection.close()
    return user_details

def create_follows(following_user_id, followed_user_id):
    query = f"""INSERT INTO follows(following_user_id, followed_user_id)
    VALUES('{following_user_id}', '{followed_user_id}')"""

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

    #PATCH has no sense for this table

def delete_follows(following_user_id, followed_user_id):
    query = f"""DELETE FROM follows
    where following_user_id='{following_user_id}' and followed_user_id='{followed_user_id}'"""

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    
#post CRUD
def get_post(id):
    query = f"""SELECT *
    FROM posts where id='{id}'"""
    
    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    user_details = list(cursor.execute(query))
    if len(user_details) != 0:
        user_details = user_details[0]
    connection.close()
    return user_details

def create_post(title, body, user_id, status):
    query = f"""INSERT INTO posts(title, body, user_id, status)
    VALUES('{title}', '{body}', '{user_id}', '{status}')"""

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def update_post(id, title, body, status):
    query = f"""UPDATE users
    SET title = '{title}', body = '{body}', status = '{status}' where id='{id}' """

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def delete_post(id):
    query = f"""DELETE FROM posts
    where id='{id}'"""

    connection = sqlite3.connect(DB_PATH, timeout= 3.0)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

@app.route("/api/users", methods=["GET", "POST", "PATCH", "DELETE"])
def users():
    try:
        if request.method == "GET":
            body = request.json 
            user_details = get_user(body["id"]);
            return gen_response(user_details), 200
        
        if request.method == "POST":
            body = request.json 
            create_user(body["username"], body["role"])
            return gen_response("ok"), 200
        
        if request.method == "PATCH":
            body = request.json 
            update_user(body["id"], body["username"], body["role"])
            return gen_response("ok"), 200
        
        if request.method == "DELETE":
            body = request.json 
            delete_user(body["id"]);
            return gen_response("ok"), 200
        
    except Exception as e:
        response = {
                "data": None,
                "error": f"Failed to get users. Reason: {e}"
            } 
        response = jsonify(response)
        response.headers.add("Access-Control-Allow-Origin", "*") 
        return response,

@app.route("/api/follows", methods=["GET", "POST", "PATCH", "DELETE"])
def follows():
    try:
        if request.method == "GET":
            body = request.json
            if(body["type"]=="followers"):
                followers = get_user_followers(body["id"]);
                return gen_response(followers), 200
            else:
                following = get_user_following(body["id"]);
                return gen_response(following), 200
            return gen_response("Bad type"), 400
        
        if request.method == "POST":
            body = request.json 
            create_follows(body["following_user_id"], body["followed_user_id"])
            return gen_response("ok"), 200
        
        if request.method == "PATCH":
            return gen_response("PATCH not implemented"), 501
        
        if request.method == "DELETE":
            body = request.json 
            delete_follows(body["following_user_id"], body["followed_user_id"]);
            return gen_response("ok"), 200
        
    except Exception as e:
        response = {
                "data": None,
                "error": f"Failed to get users. Reason: {e}"
            } 
        response = jsonify(response)
        response.headers.add("Access-Control-Allow-Origin", "*") 
        return response, 500

@app.route("/api/posts", methods=["GET", "POST", "PATCH", "DELETE"])
def posts():
    try:
        if request.method == "GET":
            body = request.json 
            user_details = get_post(body["id"]);
            return gen_response(user_details), 200
        
        if request.method == "POST":
            body = request.json 
            create_post(body["title"], body["body"], body["user_id"], body["status"])
            return gen_response("ok"), 200
        
        if request.method == "PATCH":
            body = request.json 
            update_post(body["title"], body["body"], body["status"])
            return gen_response("ok"), 200
        
        if request.method == "DELETE":
            body = request.json 
            delete_post(body["id"]); #Was status for noting a post as deleted instead of deleting it? change function
            return gen_response("ok"), 200
        
    except Exception as e:
        response = {
                "data": None,
                "error": f"Failed to get users. Reason: {e}"
            } 
        response = jsonify(response)
        response.headers.add("Access-Control-Allow-Origin", "*") 
        return response, 500

if __name__ == "__main__":
    # app.run(debug=True) is problematic
     app.run(host="0.0.0.0", port=8080, threaded = True)
    
