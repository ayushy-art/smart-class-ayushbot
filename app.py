from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "assignment" in incoming_msg:
        msg.body("Assignment is due Friday.")
    elif "feedback" in incoming_msg:
        msg.body("Thanks for your feedback.")
    else:
        msg.body("Hey! I’m your class chatbot. Ask me about assignments, exams, or share feedback.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)