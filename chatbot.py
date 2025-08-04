def load_faqs(filename):
    faqs = {}
    with open(filename, "r") as file:
        for line in file:
            if ":" in line:
                question, answer = line.strip().split(":", 1)
                faqs[question.lower()] = answer
    return faqs

def chatbot():
    faqs = load_faqs("faqs.txt")
    print("🤖 Hi! I'm your FAQ chatbot. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Bot: Goodbye! 👋")
            break
        found = False
        for question in faqs:
            if question in user_input:
                print("Bot:", faqs[question])
                found = True
                break
        if not found:
            print("Bot: Sorry, I don't know the answer to that.")

if __name__ == "__main__":
    chatbot()
