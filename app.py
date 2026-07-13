from flask import Flask, render_template, request, jsonify
from calculator import calculate_energy
from rag import search_knowledge
from agents import EnergyAgent
from watsonx_client import WatsonxClient

app = Flask(__name__)

agent = EnergyAgent()
watson = WatsonxClient()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    reply = get_response(user_message)

    return jsonify({"reply": reply})


def get_response(message):

    msg = message.lower()

    # Energy Calculator
    if "calculate" in msg or "consumption" in msg or "units" in msg:

        result = calculate_energy(75, 10)

        return f"""
Energy Consumption Report

Appliance : Fan
Power      : 75 Watts
Usage      : 10 Hours/Day

Daily Consumption : {result['daily_units']} Units
Monthly Consumption : {result['monthly_units']} Units
Estimated Monthly Cost : ₹{result['monthly_cost']}

Recommendation:
Use energy-efficient appliances to reduce electricity usage.
"""

    # Agent Response
    if any(word in msg for word in ["bill", "solar", "ac"]):
        return agent.process_query(msg)

    # Knowledge Base (RAG)
    if any(word in msg for word in ["electricity", "led", "light", "refrigerator", "fridge", "save"]):
        return search_knowledge(msg)

    # Watsonx AI Simulation
    return watson.generate_response(message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)