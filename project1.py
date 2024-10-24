# Zhiwei Zhang, ICS31, Project 1
from project1_quotes import *
import random


# ------------------------------------------------------------
# Movie Quotes Analysis Section
def is_question(input_string):
    if "?" in input_string[-1]:
        return True
    else:
        return False


def get_first_quotes(input_list_tuple):
    list = []
    for tuple in input_list_tuple:
        list.append(tuple[0])
    return list


def get_first_questions(input_list_tuple):
    list = get_first_quotes(input_list_tuple)
    list_of_question = []
    for x in list:
        if is_question(x):
            list_of_question.append(x)
    return list_of_question


def count_question_quotes(input_list_tuple):
    num_first_question = len(get_first_questions(input_list_tuple))
    return num_first_question


# By running the code count_question_quotes(get_quotes())
# it indicates that there are 7117 first quotes
# in the real data that are questions.


def get_average_question_length(input_list_tuple):
    list_of_questions = get_first_questions(input_list_tuple)
    count = count_question_quotes(input_list_tuple)
    length_sum = 0
    for item in list_of_questions[:]:
        length_sum += len(item)
    avg_length = length_sum / count
    return avg_length


# ------------------------------------------------------------
# Chatbot Section Version 0.0


def get_responses(input_list_tuples, question_string):
    responses = []

    for tuple in input_list_tuples:
        if tuple[0] == question_string:
            responses.append(tuple[1])

    return responses


# random module imported at the top of this documents
def get_random_from_list(input_list):
    x = random.randint(0, len(input_list) - 1)
    randomly_chosen = input_list[x]
    return randomly_chosen


def respond(input_list_tuples, question_string):
    response = get_responses(input_list_tuples, question_string)
    if "?" not in question_string:
        print("I only respond to questions!")
    elif len(response) == 0:
        return "I don't know."
    else:
        answer = get_random_from_list(response)
        return answer


# ------------------------------------------------------------
# Chatbot Version 1.0
THRESH = 0.6


def calculate_matching_percentage(user_question, stored_question):
    user_words = user_question.lower().split()
    stored_words = stored_question.lower().split()
    matching_words = 0

    for word in user_words:
        if word in stored_words:
            matching_words += 1
    return matching_words / len(stored_words)


def find_similar_questions(input_list_tuples, question_string):
    similar_questions = []
    for tuple in input_list_tuples:
        question = tuple[0]
        if calculate_matching_percentage(question_string, question) >= THRESH:
            similar_questions.append(question)
    return similar_questions


def response_v1(input_list_tuples, question_string):
    similar_questions = find_similar_questions(input_list_tuples, question_string)
    if "?" not in question_string:
        print("I only respond to questions!")
    elif len(similar_questions) == 0:
        print("I don't know.")
    else:
        selected_question = get_random_from_list(similar_questions)
        responses = get_responses(input_list_tuples, selected_question)
        answer = get_random_from_list(responses)
        print(answer)
        return answer


# ------------------------------------------------------------
# Chatbot Version 2.0
def find_similar_questions_v2(input_list_tuples, question_string):
    best_match_percentage = 0
    best_matches = []

    for tuple in input_list_tuples:
        question = tuple[0]
        match_percentage = calculate_matching_percentage(question_string, question)

        if match_percentage >= THRESH:
            if match_percentage > best_match_percentage:
                best_matches = [question]
                best_match_percentage = match_percentage
            elif match_percentage == best_match_percentage:
                best_matches.append(question)

    return best_matches


def response_v2(input_list_tuples, question_string):
    best_matching_questions = find_similar_questions_v2(
        input_list_tuples, question_string
    )
    if "?" not in question_string:
        print("I only respond to questions!")
    elif len(best_matching_questions) == 0:
        print("I don't know.")
    else:
        selected_question = get_random_from_list(best_matching_questions)
        responses = get_responses(input_list_tuples, selected_question)
        answer = get_random_from_list(responses)
        print(answer)
        return answer


# ------------------------------------------------------------
# Chatbot Launching Section
def chatbot(version):
    if version == 0:
        instruction = "Welcome!\nAsk me anything. When you're done, just type 'bye'"
        print(instruction)
        user_response = input(" - ")
        quotes = get_quotes()
        while user_response != "bye":
            answer = respond(quotes, user_response)
            if answer is not None:
                print(answer)
            user_response = input(" - ")

    elif version == 1:
        instruction = "Welcome to Chatbot version 1.0!\nAsk me anything. When you're done, just type 'bye'"
        print(instruction)
        user_response = input(" - ")
        while user_response != "bye":
            response_v1(get_quotes(), user_response)
            user_response = input(" - ")

    elif version == 2:
        instruction = "Welcome to Chatbot version 2.0!\nAsk me anything. When you're done, just type 'bye'"
        print(instruction)
        user_response = input(" - ")
        while user_response != "bye":
            response_v2(get_quotes(), user_response)
            user_response = input(" - ")


if __name__ == "__main__":
    chatbot(2)
