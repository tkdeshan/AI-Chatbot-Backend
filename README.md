# AI-Chatbot-Backend

This is the backend for an AI-powered chatbot built using **Django**. The backend is responsible for handling requests, processing data, and interacting with the monitoring system to deliver real-time information.

# Setup Instructions

1. Clone the repository:
   
   ```bash
     git clone https://github.com/Elzian-Agro/AI-Chatbot-Backend.git
3. Create a virtual environment:

    ```bash
     python -m venv venv
5. Activate the virtual environment:
  - On Windows:

    ```bash
     venv\Scripts\activate

  - On Linux/macOS:

     ```bash
     source venv/bin/activate
7. Install dependencies:

    ```bash
     pip install -r requirements.txt
9. Add the ONNX file and the DATA file to the "model/cpu_and_mobile" folder. To dowload model go to this drive link - https://drive.google.com/drive/folders/1EcMziTB4nndKmOTW5jEkCMgBo7-eTCWU?usp=sharing
5. Run the server:

    ```bash
     python manage.py runserver
