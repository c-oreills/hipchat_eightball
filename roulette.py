from random import choice

ROULETTE_LEN = 40
ANIMATION_LEN = 5 # seconds

EMOTE_CACHE = {}
WORD_CACHE = {}

def rand_seq(choices, n):
    return [choice(choices) for _ in xrange(n)]

def gif_roulette(tokens):
    return _generic_roulette(tokens, get_emote_image)

def word_roulette(tokens):
    return _generic_roulette(tokens, get_word_image)

def _generic_roulette(tokens, get_image_fn):
    roulette_seq = rand_seq(tokens, ROULETTE_LEN)
    images = [get_image_fn(s) for s in roulette_seq]
    roulette_image = roulettify_images(images)
    return roulette_image

def roulettify_images(images):
    pass

def get_emote_image(emote):
    pass

def get_word_image(word):
    pass
