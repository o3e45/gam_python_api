from flask import Flask, jsonify, request
import subprocess
import os

app = Flask(__name__)

def run_gam_command(command):
    """Runs a GAM command using subprocess and returns the output."""
    try:
        # Full path to GAM executable
        gam_path = "/root/bin/gam7/gam"  # Ensure this is correct

        # Ensure proper argument handling
        result = subprocess.run([gam_path] + command.split(), capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/gam', methods=['GET'])
def gam():
    """Exposes the GAM command as an API endpoint."""
    # Get the GAM command from the query string
    gam_command = request.args.get('command')

    if not gam_command:
        return jsonify({"error": "No command provided"}), 400

    # Run the command and get the output
    output = run_gam_command(gam_command)
    
    # Return the output as a JSON response
    return jsonify({"command": gam_command, "output": output})

if __name__ == '__main__':
    # Ensure the server runs on all addresses (can be accessed externally) and port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
