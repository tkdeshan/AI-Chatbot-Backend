# AI-Chatbot-Backend

This project is a backend server for a chatbot application, built using Django and a Simple Language Model (SLM) for text generation. The system is designed to handle user queries, generate meaningful responses, and serve them via API endpoints.

# Setup Instructions

1. Clone the repository:
   
   ```bash
     git clone https://github.com/tkdeshan/AI-Chatbot-Backend.git
2. Create a virtual environment:

    ```bash
     python -m venv venv
3. Activate the virtual environment:

    ```bash
     venv\Scripts\activate
4. Install dependencies:

    ```bash
     pip install -r requirements.txt
5. Add the ONNX file and the DATA file to the "model/cpu_and_mobile" folder. To dowload model go to this drive link - https://drive.google.com/drive/folders/1EcMziTB4nndKmOTW5jEkCMgBo7-eTCWU?usp=sharing
6. Run the server:

    ```bash
     python manage.py runserver
   
7. API request:

    ```bash
     POST '{{BASE_URL}}/api/chat/'
    
     {
      "text_input": "Hello!"
     }'
