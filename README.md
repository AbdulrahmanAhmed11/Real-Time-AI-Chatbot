# Real-Time-AI-Chatbot
A real-time, command-line AI assistant built with Python and the Cohere API. Features conversational memory and strict English-only responses via system preambles.

# 🤖 Terminal-Based AI Chatbot (Python & Cohere)

## 📌 Project Overview
This repository contains a Real-Time Command Line Interface (CLI) AI Chatbot built using Python and the **Cohere API**. The project demonstrates how to integrate Large Language Models (LLMs) into a local terminal environment, maintain conversational context (chat history), and enforce specific behavioral constraints using system preambles.

## 📸 Project Demonstration
 <img width="1708" height="838" alt="image" src="https://github.com/user-attachments/assets/a1b5e04c-b16c-4da6-9a1e-0a3283219e45" />



---

## ✨ Core Features
* **Real-Time Interaction:** Continuous, loop-based conversation directly within the terminal.
* **Contextual Memory:** The bot retains the history of the current session, allowing for natural, follow-up questions.
* **Language Forcing (System Preamble):** The model is strictly instructed via a backend preamble to respond only in professional English, regardless of the user's input language.
* **Robust Error Handling:** Wrapped API calls in `try-except` blocks to prevent the application from crashing during network drops or API timeouts.

---

## 🐛 Bug Discovery & Debugging Log
During the development of this local environment, several critical API and environment issues were diagnosed and resolved:

1. **Environment & Path Resolution (`'pip' is not recognized`)**
   * **Issue:** Initial attempts to install dependencies failed due to missing Python PATH variables in the standard Windows CMD.
   * **Solution:** Migrated the project environment to **Anaconda**, utilizing `conda activate` to ensure isolated and reliable package management.

2. **Model Deprecation (HTTP 404 Errors)**
   * **Issue:** The API returned errors indicating that specific models (`command-r` and `command-r-plus`) were deprecated and removed from Cohere's servers.
   * **Solution:** Dynamically adapted the payload to test active models.

3. **Token Padding Explosion (`<PAD><PAD>...`)**
   * **Issue:** Calling a base text-generation model (`command`) via the `co.chat()` endpoint resulted in the model outputting raw internal padding tokens instead of human-readable text.
   * **Solution:** Refactored the API call by removing the hardcoded `model` parameter entirely. This forced the Cohere SDK to automatically route the request to their most stable, default conversational model, instantly resolving the token issue and restoring fluid interaction.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Environment:** Anaconda (Conda Virtual Environments)
* **AI Provider:** Cohere (Python SDK)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/Terminal-AI-Chatbot.git](https://github.com/YourUsername/Terminal-AI-Chatbot.git)
   cd Terminal-AI-Chatbot
