# 🐘 Elephant Carpaccio - Extreme Programming Solution

Our solution in Streamlit for the Elephant Carpaccio problem during the Coding Dojo event hosted by XPUG Trento.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42-red?style=for-the-badge&logo=streamlit)

This repository contains a solution to the **Elephant Carpaccio** exercise using **Extreme Programming (XP)** principles. The challenge was to decompose a simple problem into **10-20 user stories**, completing them over **4 sprints** (each lasting 8 minutes, followed by a 2-minute showcase). Our implementation was built using **Streamlit** for an interactive web interface. 🚀

---

## 📜 Problem Statement
The goal was to build a pricing system that:
- Takes **two user inputs**: `price per item` and `number of items`.
- Computes the **final price** considering:
  - **Tax rates** based on the selected state.
  - **Discounts** that increase with the order value.
- Ensures that after each sprint, a **working and presentable version** was available.

---

## 🚀 Our Solution
🔹 **Tech Stack**: Python & Streamlit  
🔹 **Development Approach**: Extreme Programming with iterative improvements  
🔹 **Core Features**:
- 🏷️ **User Input**: Price & quantity selection
- 🌎 **State-Based Tax Calculation**
- 🎯 **Dynamic Discounting**
- 📊 **Live Price Update in UI**
- ⚡ **Fully Functional after Every Sprint!**

---

## 🛠 Installation & Usage
```bash
# Clone the repository
git clone https://github.com/ericsua/CodingDOJO_XPUG.git
cd CodingDOJO_XPUG

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 📌 User Stories Example
1️⃣ User enters a price per item and quantity.  
2️⃣ The system calculates the subtotal.  
3️⃣ The user selects a state; the system applies the correct tax rate.  
4️⃣ If the total exceeds a certain threshold, a discount is applied.  
...

✅ Each step was completed in small increments over multiple sprints!

---

👨‍💻 Developed with passion using **Extreme Programming** & **Streamlit** 🚀

