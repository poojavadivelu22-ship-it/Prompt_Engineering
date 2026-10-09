#  Prompt Engineering Dashboard

##  Project Overview

The Prompt Engineering Dashboard is a web application built using Python and Streamlit. It helps users understand and experiment with different prompt engineering techniques using the Google Gemini API.

Users can enter a task, select a prompting technique, and generate an AI response.

## Live Demo
http://localhost:8501/


##  Objectives

* To understand different prompt engineering techniques.
* To generate AI responses using the Gemini API.
* To compare different prompting methods.
* To provide a simple and user-friendly interface.

##  Technologies Used

* **Python** – Programming language
* **Streamlit** – Web application interface
* **Google Gemini API** – AI response generation
* **Google GenAI SDK** – Connecting the application to Gemini

##  Features

* Simple and interactive dashboard
* Multiple prompting techniques
* User input for custom tasks
* Adjustable response settings
* Displays the generated prompt
* Generates AI-powered responses

##  Prompting Techniques

1. **Zero-Shot Prompting** – Generates an answer without examples.
2. **One-Shot Prompting** – Uses one example to guide the response.
3. **Few-Shot Prompting** – Uses multiple examples to guide the response.
4. **Chain-of-Thought (CoT)** – Encourages structured problem-solving.
5. **Manual CoT** – Uses predefined steps to solve a task.
6. **Tree-of-Thought (ToT)** – Considers different possible approaches.

##  Project Structure

```text
Prompt Engineering/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
└── README.md
```

##  Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd "Prompt Engineering"
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Set the Gemini API Key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

In Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your actual API key. Do not upload the key to GitHub.

### Step 7: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

##  API Key Security

* Store the Gemini API key securely.
* Never publish the API key in your source code or GitHub repository.
* For Streamlit Cloud deployment, configure `GEMINI_API_KEY` in the app's Secrets settings.

##  Future Enhancements

* Add more prompting techniques.
* Allow users to compare responses.
* Save previous prompts and responses.
* Add response download functionality.
* Improve the dashboard design.

##  Conclusion

The Prompt Engineering Dashboard provides a simple way to learn and experiment with prompt engineering techniques. By integrating the Google Gemini API with Streamlit, users can explore how different prompts influence AI-generated responses.
