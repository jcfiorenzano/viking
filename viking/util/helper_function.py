from colorama import Fore

def create_yes_no_question(question):
    return question +" [Y]es, [N]o: "

def create_warning_message(message):
    return "{0}Warning: {2}{1}".format(Fore.YELLOW, Fore.RESET, message)
