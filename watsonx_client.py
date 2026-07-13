class WatsonxClient:

    def generate_response(self, prompt):

        return f"""
IBM watsonx.ai Simulation

User Query:
{prompt}

AI Recommendation:
Based on the available energy knowledge and AI reasoning,
the recommended approach is to reduce unnecessary power
consumption, use energy-efficient appliances, and monitor
daily electricity usage.
"""