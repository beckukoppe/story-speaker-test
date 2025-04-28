from LLM_convo import LLM

allowed_SPEAKER_commands=["SPEAK", "SUM", "FORCEEND", "PROPOSEEND"]
allowed_STORY_commands = ["NOTHING", "STARTPROPMPT"]

STORY_URL = "http://localhost:8081/v1/chat/completions"
SPEAKER_URL = "http://localhost:8081/v1/chat/completions"

def action_one(start_prompt):
    print("\nSpeak with hostage taker (end with 'exit'):\n")
    a,b = start_prompt
    if(a != True or b[0].get("command") != "STARTPROPMPT"):
        print("\nError: no startprompt provided\n")

    start_prompt_str = b[0].get("data")
    
    start_prompt_str += readFile("speaker-llm_startprompt.txt")

    #print(start_prompt_str)


    hostage_taker = LLM(SPEAKER_URL, start_prompt_str, allowed_SPEAKER_commands)

    while True:
        user_input = input("User: ")
        if(user_input == "exit"):
            break

        if(user_input.startswith("#")):
            response = hostage_taker.call(user_input)
        else:
            response = hostage_taker.call("#USERSAY{"+user_input+"}")
        
        boolean, cmds = response

        if(not boolean):
            print("\nAnswer Error\n")

        end = False
        for cmd in cmds:
            if(cmd.get("command") == "SPEAK"):
                print("Hostage taker says:\t")
                print(cmd.get("data"))

            if(cmd.get("command") == "FORCEEND"):
                print("Hostage taker ends the conversation.\n")
                end = True

            if(cmd.get("command") == "PROPOSEEND"):
                print("Hostage has no more to say.\n")

        #print(response)
        if end: break

    return hostage_taker.getSumUp()


def action_two():
    print("\nYou selected Action 2!\n")

def action_three():
    print("\nYou selected Action 3!\n")

def show_menu():
    story_startprompt = readFile("story-llm_startprompt.txt")

    story_llm = LLM(STORY_URL, story_startprompt, allowed_STORY_commands)

    while True:
        print("=== Main Menu ===")
        print("1. Speak with hostage taker")
        print("2. Speak with police partner")
        print("3. Perform Action 3")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sum = action_one(story_llm.call("#SPEAKWITH: HOSTAGE_TAKER"))
        elif choice == "2":
            action_two(story_llm.call("#SPEAKWITH: POLICE"))
        elif choice == "3":
            action_three()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

def readFile(str):
    o = ""
    with open(str, "r", encoding="utf-8") as f:
        o = f.read().strip()
    return o


if __name__ == "__main__":
    show_menu()