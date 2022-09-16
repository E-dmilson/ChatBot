from email import message
from posixpath import split
import re
from tabnanny import check
from urllib import response

from pygments import highlight
import long_responses as long


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    #Calculates de percentage of words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Response ====================================================
    response('Hello', ['hello', 'hi', 'sup', 'hey', 'heyo', 'yo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'your', 'manners'], required_words=['your', 'manners'])
    response('Glad to hear that', ['i\'m', 'doing', 'good', 'too'], required_words=['i\'m'])
    response('You\'re welcome', ['thank', 'you'], required_words=['thank', 'you',])
    response('I\'m Katherine', ['who', 'are', 'you'], required_words=['who', 'you'])
    response('Nice to meet you too', ['nice', 'to', 'meet', 'you'], required_words=['nice', 'meet', 'you'])

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.IN_PUSSY, ['show', 'me', 'pussy'], required_words=['pussy'])
    response(long.IN_FUCK, ['do', 'you', 'wanna', 'fuck'], required_words=['fuck'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)


    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
