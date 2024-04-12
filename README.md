# robo-api
This Django application provides a REST API endpoint for executing test cases defined in Robot Framework format. It allows you to programmatically trigger and manage test automation from external tools or applications.

### Features
- Accepts test cases in JSON format via a POST request to the /testai/tests/v1/execute endpoint.
- Parses the JSON data to extract test case titles and steps.
- Dynamically generates a Robot Framework test suite based on the extracted steps.
- Executes the generated test suite using Robot Framework.
- Returns the test execution results (pass/fail) in a JSON response.

### Installation

1. Clone this repository.
2. Create a virtual environment:

        python -m venv venv
        source venv/bin/activate  # For Linux/macOS
        venv\Scripts\activate.bat  # For Windows

3. Install dependencies:
    
        pip install -r requirements.txt

4. Apply database migrations:

        cd core
        python manage.py migrate

5. Run the Django development server:

        python manage.py runserver

### Usage
1. Test Case Format:

    The API expects an array of test cases in JSON format, with each test case containing the following properties:

    - `title`: (string) Name of the test case.

    - `steps`: (list of dictionaries) Each dictionary represents a step to be executed in the test case. The dictionary should have a single key:
    
        - `description`: (string) The Robot Framework command for the step.

Example JSON payload:

    {
        "tests": [
            {
                "title": "Test Google Search",
                "steps": [
                    { "description": "Open Browser browser='chrome'" },
                    { "description": "Go To url='https://google.com'" }
                ]
            }
        ]
    }

2. API Endpoint:
    - Method: POST
    - URL: `http://localhost:8000/testai/tests/v1/execute` (assuming you're running the development server on port 8000)

3. Sending Test Request:

    Use tools like `curl` or Postman to send a POST request with the JSON payload to the API endpoint.

            curl -X POST http://localhost:8000/testai/tests/v1/execute -H "Content-Type: application/json" -d '{ ... your JSON payload ... }'

4. Response:

    The API will return a JSON response containing the test execution results, including the test case title and its status (pass/fail).