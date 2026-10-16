from flask import Flask, jsonify, request

# ==========================================================
# INITIALIZE FLASK APPLICATION
# ==========================================================

# Create an instance of the Flask application.
app = Flask(__name__)


# ==========================================================
# SIMULATED DATA
# ==========================================================

# The Event class represents an event with an ID and title.
# Each event created will be an object of this class.

class Event:

    def __init__(self, id, title):

        # Store the unique event ID.
        self.id = id

        # Store the event title.
        self.title = title

    # Convert an Event object into a Python dictionary.
    # This allows Flask to return the event as JSON.
    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title
        }


# ==========================================================
# IN-MEMORY DATABASE
# ==========================================================

# This list simulates a database.
# It stores Event objects while the Flask application runs.
#
# Note:
# Data stored here is temporary and will be lost when
# the application restarts.

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# ==========================================================
# HELPER FUNCTION: FIND EVENT BY ID
# ==========================================================

# This function searches for an event using its unique ID.
#
# Instead of repeatedly writing the same search logic
# in different endpoints, we can reuse this function.
#
# This follows the DRY principle:
# Don't Repeat Yourself.

def find_event(event_id):

    # Loop through all events stored in memory.
    for event in events:

        # Compare the current event ID with the requested ID.
        if event.id == event_id:

            # Return the matching Event object.
            return event

    # If no matching event exists, return None.
    return None


# ==========================================================
# TASK 1: CREATE A NEW EVENT (POST)
# ==========================================================

# Define the Problem:
#
# Accept JSON data containing an event title.
# Validate the incoming data.
# Generate a unique event ID.
# Create a new Event object.
# Add the event to our in-memory database.
# Return the newly created event with HTTP status 201.

@app.route("/events", methods=["POST"])
def create_event():

    # ------------------------------------------------------
    # TASK 2: DESIGN AND DEVELOP THE CODE
    # ------------------------------------------------------

    # Extract JSON data from the incoming HTTP request.
    #
    # silent=True prevents Flask from raising an exception
    # when the JSON is missing or incorrectly formatted.
    data = request.get_json(silent=True)

    # Check whether the request contains a JSON object
    # with the required "title" field.
    if not isinstance(data, dict) or "title" not in data:

        return jsonify({
            "error": "Title is required"
        }), 400

    # Extract the event title from the JSON data.
    title = data["title"]

    # Validate the title.
    #
    # The title must:
    # 1. Be a string.
    # 2. Not be empty.
    # 3. Not contain only whitespace.
    if not isinstance(title, str) or not title.strip():

        return jsonify({
            "error": "Valid title is required"
        }), 400

    # ------------------------------------------------------
    # TASK 3: IMPLEMENT THE LOOP AND PROCESS EACH ELEMENT
    # ------------------------------------------------------

    # Find the highest existing event ID.
    #
    # The generator expression checks the IDs of all
    # events currently stored in our list.
    #
    # max() finds the highest ID.
    # default=0 handles cases where the list is empty.
    #
    # Adding 1 generates the next available ID.
    new_id = max(
        (event.id for event in events),
        default=0
    ) + 1

    # Create a new Event object.
    #
    # strip() removes unnecessary whitespace from
    # the beginning and end of the event title.
    new_event = Event(new_id, title.strip())

    # Add the new Event object to our in-memory database.
    events.append(new_event)

    # ------------------------------------------------------
    # TASK 4: RETURN AND HANDLE RESULTS
    # ------------------------------------------------------

    # Convert the newly created event into a dictionary.
    #
    # jsonify() converts the dictionary into JSON.
    #
    # HTTP 201 means the resource was successfully created.
    return jsonify(new_event.to_dict()), 201


# ==========================================================
# TASK 2: UPDATE AN EXISTING EVENT (PATCH)
# ==========================================================

# Define the Problem:
#
# Accept an event ID from the URL.
# Search for the existing event.
# Validate the new title from the JSON request.
# Update the event title.
# Return the updated event with HTTP status 200.
#
# If the event does not exist, return HTTP 404.

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

    # ------------------------------------------------------
    # TASK 2: DESIGN AND DEVELOP THE CODE
    # ------------------------------------------------------

    # Extract JSON data from the incoming request.
    data = request.get_json(silent=True)

    # ------------------------------------------------------
    # TASK 3: IMPLEMENT THE LOOP AND PROCESS EACH ELEMENT
    # ------------------------------------------------------

    # Use our helper function to search for the event
    # using the ID provided in the URL.
    event = find_event(event_id)

    # Check whether the requested event exists.
    #
    # If no matching event was found, return HTTP 404.
    if event is None:

        return jsonify({
            "error": "Event not found"
        }), 404

    # Check whether the JSON request contains
    # the required title field.
    if not isinstance(data, dict) or "title" not in data:

        return jsonify({
            "error": "Title is required"
        }), 400

    # Retrieve the new event title.
    new_title = data["title"]

    # Validate the new title.
    #
    # Reject titles that are missing, empty,
    # or contain only whitespace.
    if not isinstance(new_title, str) or not new_title.strip():

        return jsonify({
            "error": "Valid title is required"
        }), 400

    # Update the existing event title.
    #
    # The event ID remains unchanged.
    event.title = new_title.strip()

    # ------------------------------------------------------
    # TASK 4: RETURN AND HANDLE RESULTS
    # ------------------------------------------------------

    # Return the updated event as JSON.
    #
    # HTTP 200 indicates the update was successful.
    return jsonify(event.to_dict()), 200


# ==========================================================
# TASK 3: DELETE AN EXISTING EVENT (DELETE)
# ==========================================================

# Define the Problem:
#
# Accept an event ID from the URL.
# Search for the event.
# Remove the event from our in-memory database.
# Return HTTP 204 when the deletion is successful.
#
# If the event does not exist, return HTTP 404.

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):

    # ------------------------------------------------------
    # TASK 2: DESIGN AND DEVELOP THE CODE
    # ------------------------------------------------------

    # Search for the event using our helper function.
    event = find_event(event_id)

    # ------------------------------------------------------
    # TASK 3: IMPLEMENT THE LOOP AND PROCESS EACH ELEMENT
    # ------------------------------------------------------

    # Check whether the event exists.
    if event is None:

        return jsonify({
            "error": "Event not found"
        }), 404

    # Remove the matching Event object from our list.
    #
    # This modifies the existing in-memory database.
    events.remove(event)

    # ------------------------------------------------------
    # TASK 4: RETURN AND HANDLE RESULTS
    # ------------------------------------------------------

    # Return HTTP 204 to indicate successful deletion.
    #
    # HTTP 204 means "No Content".
    # Therefore, the response body must be empty.
    return "", 204


# ==========================================================
# TASK 4: RETRIEVE ALL EVENTS (GET)
# ==========================================================

# Endpoint: GET /events
#
# Purpose:
#
# Retrieve every event stored in our database.
# Convert each event into a dictionary.
# Return the complete list as JSON.
#
# HTTP 200 means the request was successful.

@app.route("/events", methods=["GET"])
def get_events():

    # Create an empty list to store event dictionaries.
    event_list = []

    # Loop through every event in our database.
    for event in events:

        # Convert the current Event object into a dictionary.
        event_data = event.to_dict()

        # Add the dictionary to our response list.
        event_list.append(event_data)

    # Return all events as JSON.
    return jsonify(event_list), 200


# ==========================================================
# TASK 5: RETRIEVE A SINGLE EVENT (GET)
# ==========================================================

# Endpoint: GET /events/<event_id>
#
# Purpose:
#
# Retrieve an event using its unique ID.
# Return the matching event as JSON.
#
# If no matching event exists, return HTTP 404.

@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):

    # Search for the requested event using its ID.
    event = find_event(event_id)

    # Check whether a matching event was found.
    if event is None:

        # Return an error message with HTTP 404.
        return jsonify({
            "error": "Event not found"
        }), 404

    # Convert the matching Event object into a dictionary.
    #
    # Return the event as JSON with HTTP status 200.
    return jsonify(event.to_dict()), 200


# ==========================================================
# START THE FLASK APPLICATION
# ==========================================================

# This condition ensures the Flask development server
# starts only when this file is executed directly.
#
# debug=True enables:
# 1. Automatic restarting when code changes.
# 2. Detailed error messages during development.
#
# Debug mode should not be enabled in production.

if __name__ == "__main__":

    app.run(debug=True)