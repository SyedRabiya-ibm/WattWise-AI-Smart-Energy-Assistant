def calculate_energy(power, hours):
    """
    power = appliance power in watts
    hours = usage hours per day
    """

    daily_units = (power * hours) / 1000
    monthly_units = daily_units * 30

    electricity_rate = 8   # ₹ per unit

    monthly_cost = monthly_units * electricity_rate

    return {
        "daily_units": round(daily_units, 2),
        "monthly_units": round(monthly_units, 2),
        "monthly_cost": round(monthly_cost, 2)
    }