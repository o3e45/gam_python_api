# GAM Command API

This Python script exposes a **REST API** using **Flask** to run **GAM (Google Apps Manager)** commands via HTTP requests. You can use this API to automate Google Workspace management tasks like listing users, modifying domains, or generating reports.

## Features
- **Run GAM commands via HTTP**: Allows interaction with Google Workspace data through API requests.
- **Command Execution**: Execute any GAM command by sending it as a query parameter to the API endpoint.
- **Customizable Port**: The Flask app runs on port **8000** by default, which can be changed.
- **Easy Integration**: Can be integrated into other systems or workflows to automate Google Workspace management.

## Prerequisites
1. Python 3.6+ installed on your system.
2. **GAM** installed and configured properly (with the necessary permissions).
3. **Flask** and **subprocess** for running commands and exposing the API.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://your-repository-url.git
    cd gam-command-api
    ```

2. **Install dependencies**:
    Ensure that **Flask** is installed:
    ```bash
    pip install flask
    ```

3. **Ensure GAM is installed**:
    Make sure you have GAM installed and configured on your system, as the script runs GAM commands through it.

## Usage

1. **Start the Flask server**:
    To run the server, use:
    ```bash
    python3 gam_api.py
    ```

    By default, the server will be available at `http://127.0.0.1:8000`.

2. **Run a GAM Command**:
    You can now interact with the API by sending **GET** requests with the GAM command as a query parameter.

    For example, to list all users:
    ```bash
    curl "http://127.0.0.1:8000/gam?command=gam+print+users"
    ```

    **Response**:
    ```json
    {
        "command": "gam print users",
        "output": "primaryEmail\ndonovan_vincent@owendobson.com\nowen@owendobson.com\n"
    }
    ```

3. **Customize Port**:
    If you want to run the API on a different port, you can modify the `app.run(debug=True, port=8000)` line in the Python script.

## Example Endpoints

- **GET /gam**: Executes a GAM command and returns the output.
  - Example request:
    ```
    curl "http://127.0.0.1:8000/gam?command=gam+print+users"
    ```
  - Example response:
    ```json
    {
        "command": "gam print users",
        "output": "primaryEmail\ndonovan_vincent@owendobson.com\nowen@owendobson.com\n"
    }
    ```

## Security Considerations

1. **Authentication**:
   - The current script does not include authentication. It's recommended to implement authentication (e.g., API keys or OAuth) in a production environment to prevent unauthorized access to the API.

2. **Input Validation**:
   - User input is directly passed to the shell via the `subprocess` module, so it's important to sanitize the input to avoid shell injection vulnerabilities. You should validate and escape commands properly before running them.

## Extending the API

You can extend the API with additional endpoints to manage specific Google Workspace resources, such as:
- **Create, update, or delete users**.
- **Manage groups, domains, and security settings**.

For example, you can create a new endpoint to create users using `POST` requests:
```python
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password = data.get('password')
    
    command = f"gam create user {email} firstname {firstname} lastname {lastname} password {password}"
    output = run_gam_command(command)
    return jsonify({"output": output})
