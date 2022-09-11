from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r'env\nft-marketplace-mustb2b-firebase-adminsdk-uu5ru-78e423d239.json')
default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'nft-marketplace-mustb2b.appspot.com'})
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("connectWallet.html")

if(__name__ == "__main__"):
    app.run(debug=True)
   