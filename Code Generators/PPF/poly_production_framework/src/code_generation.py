import openai

def generate_code(api_key, prompt):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            top_p=1
        )
    except Exception as e:
        return None, str(e)
    return response.choices[0].text.strip(), None

def populate_file(file_path, code):
    with open(file_path, 'w') as file:
        file.write(code)

def generate_and_populate(api_key, file_path, prompt):
    code, error = generate_code(api_key, prompt)
    if error:
        return False, f"Error generating code for file {file_path}: {error}"
    populate_file(file_path, code)
    return True, None
