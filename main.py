from command_line_view import print_suggestions, print_start_system, print_enter_text
from auto_complete import get_best_k_completions


def start_system():
    print_start_system()
    print_enter_text()
    val = input()
    while True:
        best_suggestions = get_best_k_completions(val)
        print_suggestions(best_suggestions)
        prev_val = val
        val = input(f"{prev_val}")
        if val == "#":
            val = input("Enter new text\n")
        elif val == "#q":
            break
        else:
            val = prev_val + val


if __name__ == '__main__':
    start_system()
