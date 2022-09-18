from pickle import NONE
from flask import Flask, render_template, request, session, redirect, url_for
import requests, json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
# from web3 import Web3

# FIREBASE CONFIG
cred = credentials.Certificate(r'env\nft-marketplace-mustb2b-firebase-adminsdk-uu5ru-78e423d239.json')
default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'nft-marketplace-mustb2b.appspot.com'})
db = firestore.client()

# FLASK CONFIG
app = Flask(__name__)
app.config["SECRET_KEY"] = "nft-marketplace-mustb2b"

# WEB3 CONFIG
# web3 = Web3(Web3.HTTPProvider("https://polygon-mumbai.infura.io/v3/649dce30cf974f4a9ad9329bcb7fb59a"))
# print(web3.isConnected())

# PINATA CONFIG
url = "https://api.pinata.cloud/data/testAuthentication"
header = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJlYzgzNmI0OC05NTNlLTQ2ZWYtODkzMy1mMDU0NjYwMjQ2ZTYiLCJlbWFpbCI6InByYW5hdmNvc21vczRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImYzMmVmMDY0MzZmMzVlMjA2ZGJkIiwic2NvcGVkS2V5U2VjcmV0IjoiMWYxMTY0OTliYjVmZTM2OGUwMDk2Y2ZjNWIxOWQyOWNmZjI5ZTlhMzU2MTZlMDljZjNlMzY2M2U0ZjcyYWM3ZiIsImlhdCI6MTY2MjgzMzg5N30.l-2R-1EiPyLVPQDGd3acostkRMuNCFW9am1byyYvHNo' }
jsonheader = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJlYzgzNmI0OC05NTNlLTQ2ZWYtODkzMy1mMDU0NjYwMjQ2ZTYiLCJlbWFpbCI6InByYW5hdmNvc21vczRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImYzMmVmMDY0MzZmMzVlMjA2ZGJkIiwic2NvcGVkS2V5U2VjcmV0IjoiMWYxMTY0OTliYjVmZTM2OGUwMDk2Y2ZjNWIxOWQyOWNmZjI5ZTlhMzU2MTZlMDljZjNlMzY2M2U0ZjcyYWM3ZiIsImlhdCI6MTY2MjgzMzg5N30.l-2R-1EiPyLVPQDGd3acostkRMuNCFW9am1byyYvHNo', 'Content-Type': 'application/json'}


# DEFAULT
@app.route("/")
def selectUserType():
    return render_template("selectusertype.html")

# LOGIN
@app.route("/<select>/login", methods=["GET", "POST"])
def login(select):
    if session.get("uid") != None and session.get("cid") != None:
        session.pop("uid")
        session.pop("cid")
    if session.get("uid") != None and select == "booth":
        return redirect("/selectbooth")
    if session.get("cid") != None and select == "customer":
        return redirect("/metaverse")
    if request.method == "GET":
        return render_template("login.html", type=select)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            response = requests.post(
                url="https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBwVRHYyOnRC3zNdHfxzq8kjhaI7rTiHGI", 
                data={"email":email,"password":password,"returnSecureToken":True}
            )
            idToken = json.loads(response.text)["idToken"]
            expiresIn = json.loads(response.text)["expiresIn"]
            print(response.text)
            uid = json.loads(response.text)["localId"]
            if select == "booth":
                session["uid"] = uid
                try:
                    session.pop("cid")
                except:
                    pass
                return redirect("/selectbooth")
            if select == "customer":
                session["cid"] = uid
                try:
                    session.pop("uid")
                except:
                    pass
                return redirect("/metaverse")
            else:
                return redirect(f"/{select}/login")

        except:
            return redirect(f"/{select}/login")

# SIGNUP
@app.route("/<select>/signup", methods=["POST"])
def signup(select):
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            user = auth.create_user(email=email, password=password)
            if select == "booth":
                session["uid"] = user.uid    
                return redirect("/selectbooth")
            if select == "customer":
                session["cid"] = user.uid
                return redirect("/metaverse")
            else:
                return redirect("/")
        except:
            return "Failed to create user"

# SIGNOUT
@app.route("/signout")
def signout():
    try:
        session.pop("uid")
    except:
        pass
    try:
        session.pop("cid")
    except:
        pass
    return redirect("/")

# SELECT BOOTH
@app.route("/selectbooth")
def selectBooth():
    if session.get("uid") == None:
        return redirect("/")
    return render_template("selectbooth.html")

# CONNECT WALLET
@app.route("/connectWallet/<url>")
def connect(url):
    if session.get("uid") == None and session.get("cid") == None:
        return redirect("/")
    return render_template("connectWallet.html", address=url)

# FILE UPLOAD
@app.route("/createNFT", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("createNFT.html")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            # send file to ipfs storage
            url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
            files=[
            ('file',(file.filename,file.read(),'application/octet-stream'))
            ]
            response = requests.request("POST", url, headers=header, files=files)
            print("Starting")
            ipfsHash = json.loads(response.text)["IpfsHash"]
            print("done")

            if ipfsHash == None:
                return redirect("/nftbooth")
            # send metadata to contract
            url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
            payload = json.dumps({"pinataContent": {"name": request.form["name"], "image": ipfsHash, "description": request.form["description"]}})
            response = requests.request("POST", url, headers=jsonheader, data=payload)
            jsonIpfsHash = json.loads(response.text)["IpfsHash"]
            print("done done")
            if jsonIpfsHash == None:
                return redirect("/nftbooth")
            return redirect(url_for('.mintnft', name=request.form["name"], metadataURI=f"https://gateway.pinata.cloud/ipfs/{jsonIpfsHash}", imageuri=f"https://gateway.pinata.cloud/ipfs/{ipfsHash}", price=request.form["price"]))
    return "awww snap! something went wrong"


# NFT BOOTH
@app.route("/nftbooth")
def nftbooth():
    if session.get("uid") == None and session.get("cid") == None:
        return redirect("/")
    return render_template("nftbooth.html")

# VIEW NFT
@app.route("/nftbooth/<id>")
def nftview(id):
    if session.get("uid") == None and session.get("cid") == None:
        return redirect("/")
    return render_template("viewnft.html", id=id)
    
# MINT NFT ROUTE
@app.route("/mintnft")
def mintnft():
    return render_template("mintnft.html", name=request.args['name'], metadataURI=request.args['metadataURI'], imageuri=request.args['imageuri'], price=request.args['price'])

# BUY NFT
@app.route("/buynft/<id>")
def buynft(id):
    return render_template("buynft.html", id=id)

# METAVERSE
@app.route("/metaverse")
def metaverse():
    if session.get("cid") == None:
        return redirect("/customer/login")
    data = db.collection("booths").get()
    dictarr = []
    for i in data:
        dictarr.append(json.dumps(i.to_dict()))
    return render_template('metaverse.html', dictarr=dictarr, len=len(dictarr))

# NFT MARKETPLACE
@app.route("/nft_marketplace/<address>")
def nftmarketplace(address):
    return render_template("nftmarketplace.html", address=address)

# YOUR NFTS
@app.route("/yournfts")
def yournfts():
    return render_template("yournfts.html")

if(__name__ == "__main__"):
    app.run(debug=True)