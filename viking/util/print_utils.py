from colorama import Fore

def create_yes_no_question(question):
    return question +" [Y]es, [N]o: "

def warning_format(message):
    return "{0}Warning: {1}{2}".format(Fore.YELLOW, message, Fore.RESET)

def error_format(message):
    return "{0}{1}{2}".format(Fore.RED, message, Fore.RESET)

def info_format(message):
    return "{0}{1}{2}".format(Fore.GREEN, message, Fore.RESET)

def print_data_table(headers, data):
    column_dimensions = [0] * len(headers)
    extra_space = 5

    for column_index in range(0, len(data[0])):
        max_len = 0 
        for row_index in range(0, len(data)):
            max_len = max(max_len, len(data[row_index][column_index]))
        column_dimensions[column_index] = max_len + extra_space
    
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