from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

def run_gam_command(command):
    """Runs a GAM command using subprocess and returns the output."""
    try:
        # Run the GAM command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return str(e)

@app.route('/gam', methods=['GET'])
def gam():
    """Exposes the GAM command as an API endpoint."""
    # Get the GAM command from the query string
    gam_command = request.args.get('command')

    if not gam_command:
        return jsonify({"error": "No command provided"}), 400

    # Run the command and get the output
    output = run_gam_command(gam_command)
    
    # Return the output
    return jsonify({"command": gam_command, "output": output})

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(debug=True, port=8000)
