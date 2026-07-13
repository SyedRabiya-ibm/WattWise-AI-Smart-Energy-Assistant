class EnergyAgent:

    def process_query(self, user_query):

        user_query = user_query.lower()

        if "bill" in user_query:
            return "Energy Optimization Agent: Use LED bulbs, switch off unused appliances and monitor your monthly consumption."

        elif "solar" in user_query:
            return "Renewable Energy Agent: Solar panels can significantly reduce electricity bills and carbon emissions."

        elif "ac" in user_query:
            return "Cooling Efficiency Agent: Keep AC temperature between 24°C and 26°C and clean filters regularly."

        elif "calculate" in user_query:
            return "Energy Calculator Agent: Calculating appliance energy consumption."

        else:
            return "General Energy Agent: Providing smart energy saving recommendations."