# main.py (for a Google Cloud Function or Cloud Run service)
import functions_framework
from google.cloud import firestore
import json

# Initialize Firestore DB client
db = firestore.Client()

@functions_framework.http
def submit_feedback(request):
    """
    HTTP Cloud Function that receives feedback and stores it in Firestore.
    """
    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json(silent=True)
    if not request_json or 'feedback' not in request_json:
        return ('{"error": "Invalid request: \'feedback\' field is missing."}', 400, headers)

    feedback_text = request_json['feedback']
    user_id = request_json.get('userId', 'anonymous') # Optional: if you pass user ID from frontend
    job_desc = request_json.get('jobdes', '')
    resume = request_json.get('resume', '')
    email = request_json.get('email', 'anonymous')

    try:
        # Reference to the 'feedback' collection
        # For public data, use /artifacts/{appId}/public/data/feedback
        # For this example, we'll assume a simple 'feedback' collection
        doc_ref = db.collection('feedback').document()

        doc_ref.set({
            'email': email,
            'feedback': feedback_text,
            'jobdesc': job_desc,
            'resume': resume,
            'time': firestore.SERVER_TIMESTAMP
        })
        return ('{"message": "Feedback successfully recorded."}', 200, headers)
    except Exception as e:
        print(f"Error writing feedback to Firestore: {e}")
        return (f'{{"error": "Failed to record feedback: {str(e)}"}}', 500, headers)# main.py (for a Google Cloud Function or Cloud Run service)
import functions_framework
from google.cloud import firestore
import json

# Initialize Firestore DB client
db = firestore.Client()

@functions_framework.http
def submit_feedback(request):
    """
    HTTP Cloud Function that receives feedback and stores it in Firestore.
    """
    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json(silent=True)
    if not request_json or 'feedback' not in request_json:
        return ('{"error": "Invalid request: \'feedback\' field is missing."}', 400, headers)

    feedback_text = request_json['feedback']
    user_id = request_json.get('userId', 'anonymous') # Optional: if you pass user ID from frontend
    job_desc = request_json.get('jobdes', '')
    resume = request_json.get('resume', '')
    email = request_json.get('email', 'anonymous')

    try:
        # Reference to the 'feedback' collection
        # For public data, use /artifacts/{appId}/public/data/feedback
        # For this example, we'll assume a simple 'feedback' collection
        doc_ref = db.collection('feedback').document()

        doc_ref.set({
            'email': email,
            'feedback': feedback_text,
            'jobdesc': job_desc,
            'resume': resume,
            'time': firestore.SERVER_TIMESTAMP
        })
        return ('{"message": "Feedback successfully recorded."}', 200, headers)
    except Exception as e:
        print(f"Error writing feedback to Firestore: {e}")
        return (f'{{"error": "Failed to record feedback: {str(e)}"}}', 500, headers)
