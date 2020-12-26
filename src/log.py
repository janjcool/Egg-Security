from miscellaneous import pretty_time, time

debuggingState = True

OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'

ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def warning(warning_message: str):
    print('\033[93m' + "(" + str(pretty_time()) + ") WARNING: " + str(warning_message) + '\033[0m')


def error(error_message: str):
    print('\033[91m' + "(" + str(pretty_time()) + ") ERROR: " + str(error_message) + '\033[0m')


def message(log_message: str):
    print('\033[92m' + "(" + str(pretty_time()) + ") LOG: " + str(log_message) + '\033[0m')


def debugging(debug_message: str):
    if debuggingState:
        print('\033[0m' + "(" + str(pretty_time()) + ") DEBUGGING: " + str(debug_message) + '\033[0m')


def repeat_message(log_message: str, repeat: int, message_id: str = ""):
    from miscellaneous import read_json, write_json
    """
    print a message ones every [repeat] seconds and only one every second if you give the parameter
    repeat_message_previous_time

    :param log_message: the message
    :param repeat: how many seconds it takes to print the message again
    :param message_id: a id to get the previous time a repeat_message printed 
                       (so multiple repeat messages do not print in 1 second)
    :return: whether or not the message printed (printed = True)
    """
    json_dict = read_json("data/dump")

    if time() % repeat == 0 and not json_dict["repeatMessage"][message_id] == time():  # check if there is a rest when
        # you divide repeat by time() and if you already send a message of a certain id this second
        print('\033[92m' + "(" + str(pretty_time()) + ") LOG: " + str(log_message) + '\033[0m')  # print the message
        json_dict["repeatMessage"][message_id] = time()  # save time of message to json dictionary for next message/run

        write_json("data/dump", json_dict)  # save dictionary to the json file dump
