import docx
import requests
import config

# Eleven Labs API endpoint
api_base_url = 'https://api.elevenlabs.io/v1'
voice_id = '21m00Tcm4TlvDq8ikWAM'
optimize_streaming_latency = 0

# Path to the input doc file
doc_file_path = r'C:\Users\asus\Desktop\abc.docx'

# Read the doc file contents
doc = docx.Document(doc_file_path)
text_content = ' '.join([paragraph.text for paragraph in doc.paragraphs])

# Prepare the request payload
payload = {
    'text': text_content,
    'voice_settings': {
        'stability': 0,
        'similarity_boost': 0
    }
}

# Replace 'YOUR_API_KEY' with your actual API key
api_key = config.ELEVENLABS_API_KEY

# Prepare the request headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Construct the complete API URL
api_url = f'{api_base_url}/voices/{voice_id}?optimize_streaming_latency={optimize_streaming_latency}'

# Send the HTTP POST request to the API
response = requests.post(api_url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the response text
    print(response.text)
else:
    # Print the error message if the request failed
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)
