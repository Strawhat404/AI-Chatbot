from flask import Blueprint, request, jsonify

# Create a blueprint for chatbot routes
chatbot_routes = Blueprint("chatbot_routes", __name__)

@chatbot_routes.route("/", methods=["GET"])
def home():
    # Serve the HTML directly or use a template engine (e.g., Jinja2)
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ethio Chatbot</title>
    </head>
    <body>
        <h1>Made in 💛love💛 with Python by Joseph Tesfaye</h1>
        <textarea id="userInput" rows="4" cols="50"></textarea><br>
        <button onclick="sendMessage()">Send</button>
        <p id="chatResponse"></p>
        <script>
            async function sendMessage() {
                const userInput = document.getElementById("userInput").value;

                try {
                    const response = await fetch("/chat", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ message: userInput }),
                    });

                    const data = await response.json();
                    document.getElementById("chatResponse").innerText = data.response;
                } catch (error) {
                    document.getElementById("chatResponse").innerText = "Error: Unable to fetch response!";
                    console.error("Fetch error:", error);
                }
            }
        </script>
    </body>
    </html>
    """

@chatbot_routes.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    data = request.get_json()
    user_message = data.get("message", "")

    # Example chatbot response logic
    bot_response = f"You said: {user_message}"

    # Return the response as JSON
    return jsonify({"response": bot_response})
