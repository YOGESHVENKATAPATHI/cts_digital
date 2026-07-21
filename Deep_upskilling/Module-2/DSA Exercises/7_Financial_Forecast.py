def calculate_future_value(current_value, growth_percentage, duration_years):
    if duration_years == 0:
        return current_value

    return calculate_future_value(
        current_value + current_value * growth_percentage / 100,
        growth_percentage,
        duration_years - 1
    )

initial_investment = 5000.0
annual_growth_rate = 7.5
investment_period = 10

print("--- Financial Forecast Projection ---")
print(f"Initial Investment: ${initial_investment}")
print(f"Annual Growth Rate: {annual_growth_rate}%")
print(f"Investment Period: {investment_period} Years")

projected_value = calculate_future_value(
    initial_investment,
    annual_growth_rate,
    investment_period
)

print("\\nProjected Future Value = ${:,.2f}".format(projected_value))