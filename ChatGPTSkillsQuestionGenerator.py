import openai
import json

openai.api_key = "open api key here"
def generate_questions(skill_area, difficulty_level="intermediate", num_questions=5):
    prompt = f"Generate {num_questions} {difficulty_level} level questions related to {skill_area}:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=150,
        stop=None
    )

    choices = response["choices"]
    questions = [choice["message"]["content"].strip() for choice in choices]
    return questions

def main():
    skill_area = input("Enter the skill or subject area: ")
    difficulty_level = input("Specify difficulty level (basic, intermediate, advanced): ").lower()

    questions = generate_questions(skill_area, difficulty_level)

    if questions:
        print("\nGenerated Questions:")
        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question}")

        with open("generated_questions.json", "w") as file:
            json.dump({"skill_area": skill_area, "questions": questions}, file)

if __name__ == "__main__":
    main()
