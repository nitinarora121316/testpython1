import docx
import requests
import pygame
import io
import config

# Initialize Pygame
pygame.init()


# Eleven Labs API endpoint
api_base_url = 'https://api.elevenlabs.io'
voice_id = '21m00Tcm4TlvDq8ikWAM'
optimize_streaming_latency = 0

# Path to the input doc file
doc_file_path = r'C:\Users\asus\Desktop\abc.docx'

# Read the doc file contents
doc = docx.Document(doc_file_path)
text_content = ' '.join([paragraph.text for paragraph in doc.paragraphs])

# Prepare the request payload
payload = {
    # 'text': text_content,
    'text': "hello1",
    'model_id': 'eleven_monolingual_v1',
    'voice_settings': {
        'stability': 0,
        'similarity_boost': 0
    }
}

# Replace 'YOUR_API_KEY' with your actual API key
api_key = config.ELEVENLABS_API_KEY

# Prepare the request headers
headers = {
    'xi-api-key': f'{api_key}',
    'Content-Type': 'application/json'
}

# Construct the complete API URL
api_url = f'{api_base_url}/v1/text-to-speech/{voice_id}?optimize_streaming_latency={optimize_streaming_latency}'

# Send the HTTP POST request to the API
response = requests.post(api_url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the API response
    print(response.text)
    
    # Verify the content of the audio response
    audio_data = response.content
    with open('audio.mp3', 'wb') as f:
        f.write(audio_data)
    
    # Play the audio file using Pygame
    pygame.mixer.init()
    pygame.mixer.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()  # Wait until the audio finishes playing
else:
    # Print the error message if the request failed
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)
