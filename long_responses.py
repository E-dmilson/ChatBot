import random
from urllib import response

R_EATING = "I don't like eating anything because i'm a bot obviously"
IN_PUSSY = "Stop being creepy nigga🙄"
IN_FUCK = "And your parents thinks you're innocent🙄"

def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?",
                "Hmmm?",
                "Excume me?"][random.randrange(6)]
    return response