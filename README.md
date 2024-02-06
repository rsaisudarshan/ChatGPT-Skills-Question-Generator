# Question Generator using OpenAI's GPT-3.5 Turbo

This Python script utilizes OpenAI's GPT-3.5 Turbo model to generate questions based on a specified skill or subject area and difficulty level. Users can interactively input the skill area and choose the difficulty level, and the script will generate a set of questions accordingly.

## Setup

1. **OpenAI API Key:**
   - Obtain your OpenAI API key and replace the placeholder in the script with your key.
     ```python
     openai.api_key = "your-api-key-here"
     ```

2. **Dependencies:**
   - Make sure to install the required dependencies using:
     ```bash
     pip install openai
     ```

## Usage

1. **Run the Script:**
   - Execute the script by running the command:
     ```bash
     python ChatGPTSkillsQuestionGenerator.py
     ```

2. **Input:**
   - Enter the skill or subject area when prompted.
   - Specify the difficulty level (basic, intermediate, advanced).

3. **Generated Questions:**
   - The script will generate a set of questions based on the provided input.

4. **Output:**
   - The generated questions will be displayed on the console.
   - Additionally, the questions will be saved in a JSON file named "generated_questions.json" for future reference.
   - The path to the generated_questions.json file is the same location as the main program.

## Customization

- **Number of Questions:**
  - You can modify the `num_questions` parameter in the `generate_questions` function to change the number of questions generated.

- **Model Configuration:**
  - Adjust the parameters like `temperature` and `max_tokens` in the `openai.ChatCompletion.create` method for fine-tuning the question generation process.
