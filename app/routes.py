from flask import Blueprint,request,jsonify
from app.nlp import handle_user_input

chatbot_routes = Blueprint("chatbot_routes",__name__)

@chatbot_routes.route("/chat",methods=["POST"])
def chat():
    user_message = request.json.get("message","")
    if not user_message:
        return jsonify({"error":"Message cannot be empty"}),400
    response = handle_user_input(user_message)
    return jsonify({"response":response})