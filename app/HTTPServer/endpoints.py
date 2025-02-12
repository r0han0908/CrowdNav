from flask import jsonify, request
import json 


def get_monitor():
    file_path = "./monitor_data.json"

    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    except FileNotFoundError:
        raise FileNotFoundError("Monitor data not found")

    except Exception as e:
        raise e
  

# Construct the path to the knobs.json file, assuming it's two directories back
json_file_path = 'knobs.json'

# Open the JSON file in read mode ('r')
with open(json_file_path, 'r') as json_file:
    # Use json.load() to read data from the file
    adaptation_options_data = json.load(json_file)

    # Now 'data' contains the contents of the JSON file as a Python dictionary
    print(adaptation_options_data)


def getexecute():
    try:
        # Get the JSON data from the request body
        request_data = request.get_json()

        # Check if the required adaptation fields are present in the request data
        required_fields = ["routeRandomSigma", "explorationPercentage", "maxSpeedAndLengthFactor", 
                            "averageEdgeDurationFactor", "freshnessUpdateFactor", "freshnessCutOffValue", 
                            "reRouteEveryTicks"]
        if not all(field in request_data for field in required_fields):
            return jsonify({"error": "Missing required fields in the adaptation request"}), 400

        # Implement your adaptation logic here based on the received data
        # For demonstration, we'll print the received data
        print('Received adaptation data: {request_data}')

        # Return a response indicating the success of the adaptation
        return jsonify({"message": "Adaptation executed successfully"})

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e)}), 500
    
def getAdaptationOptions():
    return adaptation_options_data


