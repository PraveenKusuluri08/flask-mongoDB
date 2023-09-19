from app import *
from routes import userBluePrint,chatBlueprint
from flask import jsonify

app.register_blueprint(userBluePrint)

app.register_blueprint(chatBlueprint)


    
@app.route("/t")
def t():
    return jsonify(message="Test endpoint")

print(app.url_map)

if __name__=="__main__":
    print(f"socket connection established")
    socketIO.run(app,port=5000,debug=True)
    # app.run(host="0.0.0.0",port=5000,debug=True)