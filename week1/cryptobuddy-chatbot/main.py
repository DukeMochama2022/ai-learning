import json

def load_crypto_data(filename):
    with open(filename,'r') as file:
        return json.load(file)
    
def crypto_chatbot(crypto_db):
    bot_name = "CryptoBuddy"
    print(f" Hey there! I'm {bot_name} — your friendly crypto sidekick!")
    print(" Ask me about trending coins, sustainability, or long-term growth!")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_query=input("You: ").lower()
        
        if user_query in ['exit','quit', 'end']:
            print(f"{bot_name} Keep grinding, invest wisely. Goodbye for now!")
            break
        
        elif "sustainable" in user_query:
            recommend=max(crypto_db,key=lambda x: crypto_db[x] ["sustainability_score"])
            print(f"{bot_name}: Invest in {recommend} It's eco-friendly and has a longterm potential!\n")
            
        elif "trending" in user_query or "rising" in user_query:
            trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            print(f"{bot_name}: These coins are trending up : {', '.join(trending)}\n")

        elif "long-term" in user_query or "growth" in user_query:
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                    print(f"{bot_name}: {coin} is trending up and has a top-tier sustainability score!\n")

        elif "energy" in user_query or "efficient" in user_query:
            eco_friendly = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
            print(f"{bot_name}: These coins use low energy : {', '.join(eco_friendly)}\n")

        else:
            print(f"{bot_name}: Hmm... I didn't catch that. Try asking about sustainability, price trends, or energy use.\n")

    print(" Disclaimer: Crypto is risky — always do your own research!")

# Run the chatbot
if __name__ == "__main__":
    crypto_data = load_crypto_data("data.json")
    crypto_chatbot(crypto_data)     
    