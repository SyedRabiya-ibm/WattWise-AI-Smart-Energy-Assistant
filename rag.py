def load_knowledge():

    try:
        with open("energy_knowledge.txt", "r", encoding="utf-8") as file:
            knowledge = file.read()

        return knowledge

    except FileNotFoundError:
        return "Energy knowledge file not found."


def search_knowledge(query):

    knowledge = load_knowledge()

    query = query.lower()

    if "ac" in query:
        return """
        AC Energy Saving:
        Keep AC temperature between 24-26°C.
        Clean filters regularly.
        """

    elif "solar" in query:
        return """
        Solar Energy:
        Solar panels reduce electricity bills
        and provide clean renewable energy.
        """

    elif "led" in query or "light" in query:
        return """
        LED Lighting:
        LED bulbs consume less power
        and have longer life.
        """

    elif "fridge" in query or "refrigerator" in query:
        return """
        Refrigerator:
        Avoid frequent door opening.
        Maintain proper temperature.
        """

    else:
        return knowledge