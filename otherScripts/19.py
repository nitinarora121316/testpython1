import docx
import pyttsx3

def read_aloud_from_docx(docx_file):
    # Open the Word document
    doc = docx.Document(docx_file)

    # Extract the text from each paragraph
    extracted_text = []
    for paragraph in doc.paragraphs:
        extracted_text.append(paragraph.text)

    # Join the extracted text into a single string
    text = ' '.join(extracted_text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Read the text aloud
    engine.say(text)
    engine.runAndWait()

# Specify the path to your Word document
word_file = r'C:\Users\asus\Desktop\abc.docx'

# Call the function to read aloud the content of the Word document
read_aloud_from_docx(word_file)
