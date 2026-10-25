### Django AI Chat Bot

A lightweight, responsive web application that integrates an AI language model into a Django backend to deliver intelligent, real-time conversational experiences. 

### Features

* Asynchronous chat handling with Django views.
* Persistent chat history stored via the Django ORM.
* Secure environment variable handling for API credentials.

### Prerequisites

Ensure you have the following installed on your system: 

* Python (3.9 or higher)
* pip (Python package installer)

### Getting Started

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd your-repo-name
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install the required dependencies:
pip install -r requirements.txt
4. Configure your environment variables:
Create a .env file in the project root directory (next to manage.py) and add your configurations:
API_KEY=your_llm_api_key_here
API_BASE_URL=your_llm_api_url_here
AI_MODEL=your_llm_api_model_name_here

5. Run database migrations:
python manage.py migrate
6. Start the development server:
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000 to interact with the chatbot. 

### Project Structure

* config/ - The main Django project configuration directory.
* chats/ - The application app containing views, models, and chat logic.
* templates/ - HTML structures for the chat interface.