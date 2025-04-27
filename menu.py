from LLM_convo import LLM


def action_one():
    print("\nSpeak with hostage taker:\n")
    inp = input()

def action_two():
    print("\nYou selected Action 2!\n")

def action_three():
    print("\nYou selected Action 3!\n")

def show_menu():
    with open("story-llm_startprompt.txt", "r", encoding="utf-8") as f:
        story_startprompt = f.read().strip()

    story_llm = LLM("testurl", story_startprompt)

    while True:
        print("=== Main Menu ===")
        print("1. Speak with hostage taker")
        print("2. Speak with police partner")
        print("3. Perform Action 3")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            action_one()
        elif choice == "2":
            action_two()
        elif choice == "3":
            action_three()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    show_menu()