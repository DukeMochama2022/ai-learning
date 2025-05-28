import json

# Load rules from the JSON file
def load_rules(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Diagnose using the rules
def diagnose(symptoms, rules):
    user_symptoms = set(symptom.lower() for symptom in symptoms)

    for rule in rules:
        rule_conditions = set(sym.lower() for sym in rule["if"])
        if rule_conditions.issubset(user_symptoms):
            return rule["then"]
    
    return "Sorry, I don't have enough information to make a suggestion."

# Main program
if __name__ == "__main__":
    rules = load_rules("rules.json")
    user_input = input("Enter your symptoms separated by commas: ")
    symptom_list = [s.strip() for s in user_input.split(",")]

    result = diagnose(symptom_list, rules)
    print(result)
