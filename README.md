# GAM Command API

This Python script exposes a **REST API** using **Flask** to run **GAM (Google Apps Manager)** commands via HTTP requests. The API accepts **POST** requests, where you send **GAM command arguments** in the body of the request. The script then executes the GAM command and returns the result in JSON format.

## Features
- **Run GAM commands via HTTP**: Allows interaction with Google Workspace data through API requests.
- **Command Execution**: Execute any **GAM** command by sending it as a JSON payload in the body of a **POST** request.
- **Customizable Port**: The Flask app runs on port **8000** by default, which can be changed.
- **Error Handling**: The script provides meaningful error messages if the command fails or if no command is provided.

## Prerequisites
1. **Python 3.6+** installed on your system.
2. **GAM** installed and configured properly (with necessary permissions).
3. **Flask** and **subprocess** for running commands and exposing the API.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git gam_python_api
    cd gam_python_api
    ```

2. **Install dependencies**:
    Make sure **Flask** is installed:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure GAM is installed**:
    Follow the [GAM installation instructions](https://github.com/GAM-team/GAM/wiki) for installing GAM and make sure the **GAM** executable is located at `/root/bin/gam7/gam` (or update the path in the script accordingly).

## Usage

1. **Start the Flask server**:
    To run the server, use:
    ```bash
    python3 gam_api.py
    ```

    By default, the server will be available at `http://127.0.0.1:8000`.

2. **Run a GAM Command**:
    You can interact with the API by sending **POST** requests with the **GAM command** in the body as JSON.

    Example request:
    ```bash
    curl -X POST http://127.0.0.1:8000/gam \
         -H "Content-Type: application/json" \
         -d '{"command": "print users"}'
    ```

    Example response:
    ```json
    {
      "command": "print users",
      "output": "primaryEmail\ndonovan_vincent@owendobson.com\nowen@owendobson.com\n"
    }
    ```

3. **Change Port**:
    If you want to run the API on a different port, modify the `app.run(debug=True, port=8000)` line in the Python script.

## Example Endpoints

- **POST /gam**: Executes a GAM command and returns the output.
  - Example request:
    ```bash
    curl -X POST http://127.0.0.1:8000/gam \
         -H "Content-Type: application/json" \
         -d '{"command": "print users"}'
    ```
  - Example response:
    ```json
    {
      "command": "print users",
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



License
This project is licensed under the MIT License - see the LICENSE file for details.

### Key Updates:
- **POST Method**: The API now expects **POST** requests with the **GAM command** passed in the request body as JSON.
- **Error Handling**: Provides proper error handling for missing commands or invalid execution.
- **Security Considerations**: A reminder to implement authentication and input validation in a production environment.

Let me know if you need any more changes!
