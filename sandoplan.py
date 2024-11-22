# Define dictionary of features mapped to motivations and concerns
motivations_and_concerns = {
    "efficiency": [
        "Automated workflows", "Task prioritization automation", "Process optimization",
        "Operational bottleneck identification", "Automated scheduling", "Employee task assignment optimization"
    ],
    "growth": [
        "Lead generation automation", "Personalized customer experiences", "Sales funnel optimization",
        "Marketing content automation", "Customer segmentation", "Market expansion strategies"
    ],
    "cost_savings": [
        "Expense tracking automation", "Operational cost analysis", "Inventory management automation",
        "Supplier cost optimization", "Payroll automation", "Financial forecasting", "Optimized staffing levels"
    ],
    "security": [
        "Data encryption", "Fraud detection", "Compliance tracking", "Access control management",
        "Threat monitoring and alerts", "Risk assessment automation"
    ],
    "scalability": [
        "Cloud infrastructure management", "Automated scalability based on traffic", "Load balancing",
        "Data backup and recovery automation", "Scalable customer support tools", "Multi-location support"
    ],
    "complexity": [
        "Simplified project management", "Employee onboarding automation", "Integrated software platforms",
        "User-friendly dashboards", "Automated reporting", "Centralized data management"
    ]
}

# Function to ask questions dynamically based on previous answers
def ask_question(question, options, previous_answers):
    print(question)
    print("1. Yes")
    print("2. No")
    response = input("Please select an option (1 or 2): ")

    if response == "1":
        previous_answers.append(options)
    return previous_answers

# Function to recommend features based on motivations and concerns
def get_recommended_features(motivations_concerns):
    recommended_features = []
    for concern in motivations_concerns:
        recommended_features.extend(motivations_and_concerns.get(concern, []))
    return list(set(recommended_features))  # Remove duplicates

# Questions related to motivations and concerns
questions = [
    ("Are you primarily concerned with improving efficiency in your operations?", "efficiency"),
    ("Is growth a primary driver for your business this year?", "growth"),
    ("Are cost savings and optimizing your budget a concern for you?", "cost_savings"),
    ("How concerned are you about the security of your business data and processes?", "security"),
    ("Is your company planning to scale, or do you need to accommodate more users/customers?", "scalability"),
    ("Are you looking to reduce the complexity of your operations or employee management?", "complexity")
]

# Collect answers from the client
previous_answers = []
for question, category in questions:
    previous_answers = ask_question(question, category, previous_answers)

# Get and display the relevant features based on motivations and concerns
recommended_features = get_recommended_features(previous_answers)

# Display the result to the client
if recommended_features:
    print("\nBased on your responses, here are some features we can create for you:")
    for feature in recommended_features:
        print(f"- {feature}")
else:
    print("Thank you for your responses! It seems we currently don't have any features that fit your needs.")
