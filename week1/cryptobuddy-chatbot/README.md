
#  CryptoBuddy — A Rule-Based Crypto Chatbot

**CryptoBuddy** is a simple, rule-based chatbot built with Python. It helps users explore cryptocurrency options based on trends, energy efficiency, and sustainability — without needing real-time APIs or complex machine learning.

>  This project was built for learning AI decision-making and basic chatbot logic using predefined data.

---

## 📌 Features

-  Rule-based chatbot (no AI model needed!)
-  Recommends trending cryptocurrencies
-  Suggests sustainable, energy-efficient coins
-  Engages in simple text-based conversations
-  Reads data from a JSON file

---

##  Objective

To build a chatbot that provides investment advice based on:
- **Profitability** (e.g., price trends, market cap)
- **Sustainability** (e.g., energy use, eco score)

---

##  Tools Used

| Tool/Tech | Purpose |
|-----------|---------|
| Python    | Core programming language |
| JSON      | Stores cryptocurrency data |
| Terminal / Console | Run the chatbot |
| [Optional] Jupyter Notebook or Colab | Run interactively |

---

##  Folder Structure

```
CryptoBuddy/
├── main.py              # Python chatbot logic
├── data.json     # Crypto data used by the bot
└── README.md            # This documentation
```

---

##  Setup Instructions

1. **Clone the Repo**

```bash
git clone https://github.com/your-username/cryptobuddy-chatbot.git
cd cryptobuddy-chatbot
```

2. **Run the Bot**

```bash
python main.py
```

3. **Ask Questions Like:**
```
- Which crypto is sustainable?
- What’s trending?
- Give me a long-term investment coin.
- What’s energy efficient?
```

---

##   Sample Conversation

```
🌟 Hey there! I'm CryptoBuddy — your friendly crypto sidekick!
 Ask me about trending coins, sustainability, or long-term growth!
Type 'exit' to quit.

You: Which crypto is trending?
CryptoBuddy: These coins are trending up : Bitcoin, Cardano

You: What's the most sustainable?
CryptoBuddy: Invest in Cardano! It's eco-friendly and has long-term potential!

You: exit
CryptoBuddy:  Keep learning and invest wisely. Bye for now!
```

---

##  How the Bot Works

- Uses **if-else rules** to respond to keywords in your input.
- Loads data from `crypto_data.json`.
- Applies rules to recommend coins:
  - **Trending** = coins with `price_trend: "rising"`
  - **Sustainable** = `sustainability_score >= 7` and `energy_use: "low"`

---


---

##  Screenshots

![Chatbot Screenshot](screenshot.png)


---

## 🎥 Demo Video

*A 30-second screen recording showing the chatbot in action.*

---

## 🧠 Summary (50 Words)

> CryptoBuddy mimics AI by using simple if-else rules to make decisions based on user input. It selects cryptocurrencies using logic based on price trends and sustainability scores, showing how rule-based systems can simulate intelligent behavior without machine learning.

---


