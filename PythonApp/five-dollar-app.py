from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://shimaya_db_user:TRa4gg0IAttO1tLp@cluster0.ebvrcno.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGODB_URI)

db = client["5-dollar"]
collection = db["food"]

app = Flask(__name__)

# data = [
#     {
#         "name" : "Subway",
#         "price" : 8.99,
#         "image_url" : "https://www.subway.com/en-us/-/media/northamerica/usa/howitworks/subclub/ap_hero_subclub_fourth_en_dsk.png?la=en-US&h=490&w=1280&mw=1280&hash=6EA6D9FA79DAA16EF14D949AB654BDB1"
#     },
#     {
#         "name" : "Starbucks",
#         "price" : 5.99,
#         "image_url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc04AHM_-3F1WLk3-DGTOu0FLT0FB8vKYYSQ&s"
#     },
#     {
#         "name" : "Roundtable Pizza",
#         "price" : 5.99,
#         "image_url" : "https://www.fatbrands.com/wp-content/uploads/2023/03/RTP-RTP_Pizza_OH_Pepperoni_Slice.jpg"
#     },
#     {
#         "name" : "Panda Express",
#         "price" : 10.99,
#         "image_url" : "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,f_jpg,h_418,q_65,w_600/v1/crm/PalmSpringsCA/2020/06/3511bdf68711b42d370cd30d6b2494e5_cfc7b6e3-b0aa-4d77-b689-10bf9af676a0.jpg"
#     },
# ]

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>Welcome to CS4800! Enjoy the full-stack dev!</em></h1></body></html>"

@app.route("/search/<budget>") # mapping
def search_food_items(budget):
    budget = float(budget)
    result = []
    for food in collection.find():
        if float(food['price']) <= budget:
            food["_id"] = str(food["_id"])
            result.append(food)
    print(result)
    return result

app.run(host = "0.0.0.0", port=5050)
    