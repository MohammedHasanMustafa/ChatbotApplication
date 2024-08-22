# HM AI Chatbot

## Overview

HM AI is an interactive chatbot application built using Streamlit and the Google Generative AI API. It provides users with real-time responses to their questions, leveraging advanced AI language models to generate informative and structured answers.

## Features

- **Real-Time Interaction**: Users can submit questions and receive immediate responses from the chatbot.
- **AI-Powered Responses**: Utilizes the Google Generative AI API to generate accurate and relevant answers based on user queries.
- **Dynamic UI**: Streamlit-based user interface with a clean design, including an input field for questions and display areas for answers.
- **Reset Functionality**: Option to clear the current question and answer to start fresh.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- langchain_google_genai
- Google API Key

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/hm-ai-chatbot.git
   cd hm-ai-chatbot

pip install streamlit langchain_google_genai

2. **Set Up Google API Key**

Replace "YOUR_GOOGLE_API_KEY" in the code with your actual Google API key.

**Run the Application**

streamlit run app.py

### Usage
**Ask a Question:** Enter your question in the text input field and click "Submit."
**View Response:** The chatbot will display the answer below the input field.
**Reset:** Click the "Reset" button to clear the current question and answer.

### Code Overview

**app.py:** Main application file containing the Streamlit UI and logic to interact with the Google Generative AI API.

**get_ai_response(user_question):** Function to send user questions to the AI model and retrieve responses.

**submit_question():** Updates the question and generates a response, clears the input field after submission.

**Streamlit Widgets:** Manages user inputs and displays results, including a text input field and buttons for submitting and resetting.

### Configuration
**Google API Key:** Ensure you have a valid Google API key and set it in the code for the chatbot to function properly.

###Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.
