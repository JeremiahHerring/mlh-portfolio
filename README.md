```markdown
# Portfolio Site

Welcome to my portfolio site! This document provides instructions on how to set up and run the application locally.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Getting Started

Follow these steps to set up your local environment:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone [<repository_url>](https://github.com/JeremiahHerring/mlh-portfolio)
cd mlh-portfolio
```

### 2. Create a Virtual Environment

Create a virtual environment to manage your project's dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

- **On macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 4. Install the Requirements

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set the Flask Environment Variables

Set the Flask environment to development and specify the application entry point. This is usually done in your terminal:

- **On macOS and Linux:**
  ```bash
  export FLASK_ENV=development
  export FLASK_APP=app/__init__.py
  ```

- **On Windows (Command Prompt):**
  ```cmd
  set FLASK_ENV=development
  set FLASK_APP=app\__init__.py
  ```

- **On Windows (PowerShell):**
  ```powershell
  $env:FLASK_ENV="development"
  $env:FLASK_APP="app\__init__.py"
  ```

### 6. Run the Application

Now you can run the Flask application:

```bash
flask run
```

Your portfolio site should now be running at `http://127.0.0.1:5000/`. You can open this URL in your web browser to view your site.

## Additional Information

Feel free to explore the code, and don’t hesitate to reach out if you have any questions or feedback!

```
