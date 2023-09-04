import json
from difflib import get_close_matches

def load_db(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_newData(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent= 2)

def find_Match(question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_Answer(question: str, database: dict) -> str | None:
    for q in database["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def main():
    database: dict = load_db('DB_Learned.json')
    while True:
        us_input: str = input('Tu: ')
        if us_input.lower() == 'exit':
            break

        best_match: str | None = find_Match(us_input, [q["question"] for q in database["questions"]])
        if best_match:
            answer: str = get_Answer(best_match, database)
            print(f'ChatBot: {answer}')
        else:
            print('ChatBot: No tengo la respuesta, cual seria la respuesta?')
            new_answer: str = input('Escribe una respuesta o escribe "skip" para omitirlo: ')
            if new_answer.lower() != 'skip':
                database["questions"].append({"question": us_input, "answer": new_answer})
                save_newData('DB_Learned.json',database)
                print('ChatBot: Aprendi una nueva respuesta')

if __name__ == '__main__':
    print('Encendido')
    main()
    