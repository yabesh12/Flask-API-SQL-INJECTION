# Flask API for SQL Injection Check

## Objective

Build a Flask API that receives a JSON payload via a POST request, checks for SQL injection characters, and returns a JSON response indicating whether the input is sanitized or not.

## Endpoint

- **Endpoint:** `/v1/sanitized/input/`
- **Method:** POST
- **Request Payload Example:**
  ```json
  {
    "input": "some input"
  }
  ```
- **Response Examples:**
  - Sanitized Input:
    ```json
    {
      "result": "sanitized"
    }
    ```
  - Unsanitized Input:
    ```json
    {
      "result": "unsanitized"
    }
    ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app/app.py
   ```

5. Access the API at: (POST)
    ```bash
    http://127.0.0.1:5000/v1/sanitized/input/
    ``` 

## Testing

To run the tests using pytest, execute the following command:
```bash
pytest tests/test_app.py
```

