from flask import Flask, request
import os 


app = Flask(__name__)

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"


@app.route("/user", methods=["GET"])
def getUser():
    name = request.args.get('name')
    print(name)
    return f'username:{name}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)