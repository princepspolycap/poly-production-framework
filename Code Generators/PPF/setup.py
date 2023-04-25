import openai
import os
import concurrent.futures
from code_generation import generate_and_populate

# Define the OpenAI API key
OPENAI_API_KEY = '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'

# Define the root directory of the project
ROOT_DIR = 'C:\\Users\\eagle\\OneDrive\\Documents\\Dev\\Code Generators\\PPF'

# Define a list of files to populate and their corresponding prompts
FILES_TO_POPULATE = [
    {
        'path': os.path.join(ROOT_DIR, 'src', 'codeFactories', 'ImageRecognitionCodeFactory.js'),
        'prompt': 'Write JavaScript code for an image recognition code factory.'
    },
    {
        'path': os.path.join(ROOT_DIR, 'src', 'codeFactories', 'NaturalLanguageProcessingCodeFactory.js'),
        'prompt': 'Write JavaScript code for a natural language processing code factory.'
    }
    # Add more files and prompts as needed
]

def main():
    for file_to_populate in FILES_TO_POPULATE:
        success, message = generate_and_populate(
            api_key=OPENAI_API_KEY,
            file_path=file_to_populate['path'],
            prompt=file_to_populate['prompt']
        )
        if success:
            print(f"Successfully populated file {file_to_populate['path']}")
        else:
            print(f"Error: {message}")

if __name__ == "__main__":
    main()
