import google.generativeai as genai
from dotenv import load_dotenv
import os
import unittest

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')


'''Takes in a complete response object from gemini and removes leading and trailing 
excess strings.'''
def format_python_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()    
        lines.pop(0)  
        lines.pop() 

    # Write the cleaned content back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)


def generate_program_code(filename):
    prompt = 'Provide code for a tic-tac-toe game in python. Do not include any explanations, comments, or extra text. Only the code: '

    response = model.generate_content(prompt)

    program_code = response.text

    with open(f'./{filename}', 'w') as file:
        file.write(program_code)
    
    format_python_file(f'./{filename}')

    return program_code


def generate_test_suite(program_code, filename):
    prompt = f'{program_code} Provide code for a test suite that confirms the functionality of this program. Do not include any explanations, comments, or extra text. Only the code: '

    response = model.generate_content(prompt)

    test_suite = response.text

    with open(f'./{filename}', 'w') as file:
        file.write(test_suite)
    
    format_python_file(f'./{filename}')

def run_tests(test_file_name):
    loader = unittest.TestLoader()
    suite = loader.discover('./temp/', pattern=f'{test_file_name}')
    print(suite)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result

# generate_test_suite(generate_program_code('tic_tac_toe.py'), 'ttt_test.py')

print(run_tests('ttt_test.py'))
