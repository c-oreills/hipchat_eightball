from roulette import gif_roulette, word_roulette

ALL_EMOTICONS = (':)', ':(')
YESNO = ('(thumbsup)', '(thumbsdown)')


def help(user, *tokens):
    pass

def yesno(user, *tokens):
    gif_roulette(YESNO)

def emote(user, *tokens):
    gif_roulette(ALL_EMOTICONS)

def choose(user, *tokens):
    if all(token in ALL_EMOTICONS for token in tokens):
        gif_roulette(tokens)
    else:
        word_roulette(tokens)

def users(user, *tokens):
    pass

default = emote

SWITCHES = {
        '--help': help,
        '': default,
        'yesno': yesno,
        'emote': emote,
        'choose': choose,
        }
