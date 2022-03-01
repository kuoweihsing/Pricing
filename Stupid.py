from flask import Flask, request, redirect, render_template
import datetime

# 載入pymongo套件
import pymongo
from bson.objectid import ObjectId

# 連線到資料庫
client=pymongo.MongoClient("mongodb+srv://wekuo1:Kuo5258357341@cluster0.ryu0s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# 寫入資料到資料庫
db=client.price
collection=db.users

# 建立app，設定靜態檔案路徑
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/")

app.secret_key="any string but secret"

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/pricer", methods = ["GET"])
def pricer():
    return render_template("pricer.html")

@app.route("/save_price", methods = ["GET"])
def save_price():
    now_time = datetime.datetime.now()

    id=request.args.get("id", "")

    size=request.args.get("size", "")
    
    keyword=request.args.get("keyword", "")
    
    price_momo=request.args.get("price_momo", "")
    formula_momo=request.args.get("formula_momo", "")
    url_momo=request.args.get("url_momo", "")
    note_momo=request.args.get("note_momo", "")
    
    price_shopee=request.args.get("price_shopee", "")
    formula_shopee=request.args.get("formula_shopee", "")
    url_shopee=request.args.get("url_shopee", "")
    note_shopee=request.args.get("note_shopee", "")
    campaign=request.args.get("campaign_select", "")

    price_other=request.args.get("price_other", "")
    formula_other=request.args.get("formula_other", "")
    url_other=request.args.get("url_other", "")
    note_other=request.args.get("note_other", "")

    threshold=request.args.get("threshold", "")

    # 寫入資料到資料庫
    collection.insert_one({
        "done_time":now_time,
        "processor":id,
        "item_size":size,
        "item_keyword":keyword,
        "price_momo":price_momo,
        "formula_momo":formula_momo, 
        "url_momo":url_momo,
        "note_momo":note_momo,
        "price_shopee":price_shopee,
        "formula_shopee":formula_shopee, 
        "url_shopee":url_shopee,
        "note_shopee":note_shopee,
        "campaign":campaign,
        "price_other":price_other,
        "formula_other":formula_other, 
        "url_other":url_other,
        "note_other":note_other,
        "threshold":threshold,
        "auditted":"n"
    })
    return redirect("/pricer")

@app.route("/auditor", methods = ["GET"])
def auditor():
    data=collection.aggregate([
    {"$match":{"auditted":"n"}},
    {"$sample":{"size":1}}])
    
    _id=""
    done_time=""
    item_size=""
    item_keyword=""
    price_momo=""
    formula_momo=""
    url_momo=""
    note_momo=""
    price_shopee=""
    formula_shopee=""
    url_shopee=""
    note_shopee=""
    campaign=""
    price_other=""
    formula_other=""
    url_other=""
    note_other=""
    threshold=""

    for doc in data:
        _id=doc["_id"]
        done_time=doc["done_time"]
        item_size=doc["item_size"]
        item_keyword=doc["item_keyword"]
        price_momo=doc["price_momo"]
        formula_momo=doc["formula_momo"]
        url_momo=doc["url_momo"]
        note_momo=doc["note_momo"]
        price_shopee=doc["price_shopee"]
        formula_shopee=doc["formula_shopee"]
        url_shopee=doc["url_shopee"]
        note_shopee=doc["note_shopee"]
        campaign=doc["campaign"]
        price_other=doc["price_other"]
        formula_other=doc["formula_other"]
        url_other=doc["url_other"]
        note_other=doc["note_other"]
        threshold=doc["threshold"]

    return render_template("auditor.html", _id=_id,done_time=done_time, item_size=item_size, item_keyword=item_keyword, price_momo=price_momo,
        formula_momo=formula_momo, url_momo=url_momo, note_momo=note_momo, price_shopee=price_shopee, formula_shopee=formula_shopee, url_shopee=url_shopee, note_shopee=note_shopee,
        campaign=campaign, price_other=price_other, formula_other=formula_other, url_other=url_other, note_other=note_other, threshold=threshold)

@app.route("/save_audit", methods = ["GET"])
def save_audit():
    object_id=request.args.get("object_id", "")
    audit_time=datetime.datetime.now()

    audit_id=request.args.get("audit_id", "")

    opinion_size=request.args.get("opinion_size", "")
    audit_size=request.args.get("audit_size", "")

    opinion_keyword=request.args.get("opinion_keyword", "")
    audit_keyword=request.args.get("audit_keyword", "")

    opinion_size_momo=request.args.get("opinion_size_momo", "")
    opinion_price_momo=request.args.get("opinion_price_momo", "")
    audit_price_momo=request.args.get("audit_price_momo", "")
    opinion_formula_momo=request.args.get("opinion_formula_momo", "")
    audit_formula_momo=request.args.get("audit_formula_momo", "")
    opinion_url_momo=request.args.get("opinion_url_momo", "")
    audit_url_momo=request.args.get("audit_url_momo", "")
    opinion_note_momo=request.args.get("opinion_note_momo", "")
    audit_note_momo=request.args.get("audit_note_momo", "")

    opinion_size_shopee=request.args.get("opinion_size_shopee", "")
    opinion_price_shopee=request.args.get("opinion_price_shopee", "")
    audit_price_shopee=request.args.get("audit_price_shopee", "")
    opinion_formula_shopee=request.args.get("opinion_formula_shopee", "")
    audit_formula_shopee=request.args.get("audit_formula_shopee", "")
    opinion_url_shopee=request.args.get("opinion_url_shopee", "")
    audit_url_shopee=request.args.get("audit_url_shopee", "")
    opinion_note_shopee=request.args.get("opinion_note_shopee", "")
    audit_note_shopee=request.args.get("audit_note_shopee", "")
    opinion_campaign=request.args.get("opinion_campaign", "")

    opinion_size_other=request.args.get("opinion_size_other", "")
    opinion_price_other=request.args.get("opinion_price_other", "")
    audit_price_other=request.args.get("audit_price_other", "")
    opinion_formula_other=request.args.get("opinion_formula_other", "")
    audit_formula_other=request.args.get("audit_formula_other", "")
    opinion_url_other=request.args.get("opinion_url_other", "")
    audit_url_other=request.args.get("audit_url_other", "")
    opinion_note_other=request.args.get("opinion_note_other", "")
    audit_note_other=request.args.get("audit_note_other", "")
    audit_threshold=request.args.get("opinion_threshold")

    collection.update_one({
        "_id":ObjectId(object_id)},{
            "$set":{
                "audit_time":audit_time,
                "audit_id":audit_id,
                "opinion_size":opinion_size,
                "audit_size":audit_size,
                "opinion_keyword":opinion_keyword,
                "audit_keyword":audit_keyword,
                "opinion_size_momo":opinion_size_momo,
                "opinion_price_momo":opinion_price_momo,
                "audit_price_momo":audit_price_momo,
                "opinion_formula_momo":opinion_formula_momo,
                "audit_formula_momo":audit_formula_momo,
                "opinion_url_momo":opinion_url_momo,
                "audit_url_momo":audit_url_momo,
                "opinion_note_momo":opinion_note_momo,
                "audit_note_momo":audit_note_momo,
                "opinion_size_shopee":opinion_size_shopee,
                "opinion_price_shopee":opinion_price_shopee,
                "audit_price_shopee":audit_price_shopee,
                "opinion_formula_shopee":opinion_formula_shopee,
                "audit_formula_shopee":audit_formula_shopee,
                "opinion_url_shopee":opinion_url_shopee,
                "audit_url_shopee":audit_url_shopee,
                "opinion_note_shopee":opinion_note_shopee,
                "audit_note_shopee":audit_note_shopee,
                "opinion_campaign":opinion_campaign,
                "opinion_size_other":opinion_size_other,
                "opinion_price_other":opinion_price_other,
                "audit_price_other":audit_price_other,
                "opinion_formula_other":opinion_formula_other,
                "audit_formula_other":audit_formula_other,
                "opinion_url_other":opinion_url_other,
                "audit_url_other":audit_url_other,
                "opinion_note_other":opinion_note_other,
                "audit_note_other":audit_note_other,
                "audit_threshold":audit_threshold,
                "auditted":"y"
                }
        })

    return redirect("/auditor")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__=="__main__":
    app.run(host="172.29.246.182")