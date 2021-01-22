def print_start_system():
    print("Loading the files and preparing the system...")


def print_enter_text():
    print("The system is ready. Enter your text:")


def print_suggestions(sentences):
    for i, val in enumerate(sentences):
        print(f"{i+1}. {val}")
