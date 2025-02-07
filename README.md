**TalentScout: AI-Powered Hiring Assistant**
=====================================================

**Purpose and Functionality**
-----------------------------

TalentScout is a cutting-edge AI-powered hiring assistant designed to streamline the interview process for candidates and hiring managers. This innovative tool utilizes natural language processing and machine learning algorithms to conduct comprehensive interviews, extracting essential information and evaluating candidate proficiency.

**Key Features and Components**
--------------------------------

1. **AI-Driven Interviews**: TalentScout's AI engine engages candidates in a natural conversation, asking relevant questions to gather information on their background, experience, and skills.
2. **Real-time Evaluation**: The system assesses candidate responses, providing an immediate evaluation of their proficiency and fit for the desired position.
3. **Automated Data Extraction**: TalentScout extracts relevant information from the interview transcript, including full name, email address, phone number, years of experience, desired position, current location, and tech stack.
4. **JSON Output**: The extracted data is formatted into a valid JSON object, making it easy to integrate with existing HR systems and databases.
5. **User-Friendly Interface**: The web-based interface provides an intuitive and interactive experience for both candidates and hiring managers.

**Setup and Usage Instructions**
---------------------------------

### Prerequisites

* Install Gradio and Groq libraries using `pip install gradio groq`
* Create a `.env` file with your Groq API key: `GROQ_API_KEY="your_api_key"`
* Clone the repository and navigate to the project directory

### Running the Application

1. Run `python main.py` to launch the TalentScout application
2. Interact with the chatbot by typing messages and responding to prompts
3. The system will guide you through the interview process and provide a JSON output at the end

**Technical Details**
--------------------

* Built using Python 3.x, Gradio, and Groq
* Utilizes natural language processing and machine learning algorithms for AI-driven interviews
* Supports real-time evaluation and automated data extraction
* Designed for scalability and integration with existing HR systems

**Dependencies and Prerequisites**
---------------------------------

* Gradio: `pip install gradio`
* Groq: `pip install groq`
* Python 3.x: Ensure you have the latest version of Python installed
* `.env` file with Groq API key: Create a file named `.env` in the project directory with your Groq API key