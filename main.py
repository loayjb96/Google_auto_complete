from command_line_view import print_suggestions, print_start_system, print_enter_text
from auto_complete import get_best_k_completions


def replace_index(string, index):
    before_index = string[:index]
    after_index = string[index + 1:]
    letter = string[index]
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) != letter:
            new_string = before_index + chr(i) + after_index
            yield new_string


def calc_defect_index(val):
    counter = 0
    pre = prefix(val)
    val = next(pre)
    while get_best_k_completions(val):
        prev = val
        counter += 1
        try:
            val = next(pre)
        except StopIteration:
            break
    return counter


def prefix(string):
    for j in range(1, len(string) + 1):
        prefix = string[:j]
        yield prefix


print_start_system()

print_enter_text()
val = input()
while val != '#':
    val = val.strip("\n")
    new_val = val[:]

    prev = None
    counter = 0
    to_return = get_best_k_completions(val)
    if not to_return:
        counter = calc_defect_index(val)
    else:
        for item in to_return:
            item.score *= 2
        print_suggestions(to_return)

    if counter < len(new_val) and len(to_return) < 5:
        i = len(to_return)
        list_count = [5, 4, 3, 2, 1]
        for correction in replace_index(new_val, counter):
            if i >= 5:
                break
            l = get_best_k_completions(correction)
            for item in l:
                i += len(l)
                if i >= 5:
                    break
                item.score -= 1
                item.score *= 2
                if counter >= 4:
                    item.score -= list_count[4]
                else:
                    item.score -= list_count[counter]
            if l:
                print_suggestions(l)
                break

    val = input()
