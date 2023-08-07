from app import *
from routes import userBluePrint 
from flask import jsonify
app.register_blueprint(userBluePrint)

@app.route("/t")
def t():
    return jsonify(message="Test endpoint")

print(app.url_map)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)