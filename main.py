import omise
import uuid
from flask import *
from flask import Flask,flash,json,jsonify,request,current_app,render_template,make_response,url_for,redirect,session,abort,send_from_directory,g # Session input for user 
omise.api_secret = 'skey_5ov0wgvkh2zpg7qh9tl'
# token   created from the token creator 
omise.api_public = "pkey_5ov0wg43quxwx1xsm8s"
PUBLIC_KEY = "pkey_5ov0wg43quxwx1xsm8s"
SECRET_KEY = "skey_5ov0wgvkh2zpg7qh9tl"
app = Flask(__name__)

@app.route("/")
def payment():
     return render_template("payment2.html",key=PUBLIC_KEY)

@app.route("/charge", methods=["POST"])
def charge():
  
    email = request.form.get("email")
    token = request.form.get("omiseToken")
    source = request.form.get("omiseSource")
    customer = request.form.get("omiseCustomer")
    order_id = uuid.uuid4()
    amount=2500
    print(request.form.get("omiseToken"))
    
    '''
    global charge 
    charge = omise.Charge.create(
      amount=amount,
      currency="thb",
      description=str(order_id),
      card=token,
      return_uri="https://roboreactor.com/login",
    )
    print(charge.status)  # Get the status into the function payment
    global charges
    charges = omise.Charge.retrieve(charge.id)
    print(charges.status)
    '''
if __name__ =="__main__":
      
       app.run(debug=True,threaded=True,host="0.0.0.0",port=8030) 