import inquirer
from colorama import Fore

def ask_yes_no_question(question):
    questions = [inquirer.Confirm("question", message=question)]
    answer = inquirer.prompt(questions)
    return answer["question"]

def error_format(message):
    return "{0}{1}{2}".format(Fore.RED, message, Fore.RESET)

def info_format(message):
    return "{0}{1}{2}".format(Fore.GREEN, message, Fore.RESET)

def print_data_table(headers, data):
    column_dimensions = [len(header) for header in headers]
    extra_space = 5

    for column_index in range(0, len(data[0])):
        for row_index in range(0, len(data)):
            column_dimensions[column_index] = max(column_dimensions[column_index], len(data[row_index][column_index]))
        column_dimensions[column_index] += extra_space

    table_width = sum(column_dimensions)
    separator = '-' * table_width

    print(separator)
    for i in range(0, len(headers)):
        string_format = "{:<"+str(column_dimensions[i])+"}"
        print(string_format.format(headers[i]), end="")
    print()
    print(separator)

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            string_format = "{:<"+str(column_dimensions[j])+"}"
            print(string_format.format(data[i][j]), end="")
        print()
    print()

def print_option_picker(message, options):
    answer_key = 'option_picker'
    questions = [
        inquirer.List(answer_key, message=message, choices=options)
    ]
    answers = inquirer.prompt(questions)
    return answers[answer_key]