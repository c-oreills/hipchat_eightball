from random import choice, uniform
import PIL

from images2gif import writeGif

ROULETTE_ITEMS = 40
ANIMATION_DURATION = 10
DAMPING_FACTOR = 1.2

def _calculate_durations(items, damping_factor):
    durations = tuple(reversed([1/(float(DAMPING_FACTOR)**n) for n in xrange(items)]))
    return durations, sum(durations)

DURATIONS, TOTAL_DURATIONS = _calculate_durations(ROULETTE_ITEMS, DAMPING_FACTOR)

EMOTE_CACHE = {}
WORD_CACHE = {}


def rand_seq(choices, n):
    return [choice(choices) for _ in xrange(n)]

def test_roulette():
    from glob import glob
    image_filenames = glob('image_cache/*.gif')
    gif_roulette(image_filenames)

def gif_roulette(tokens):
    return _generic_roulette(tokens, get_emote_image)

def word_roulette(tokens):
    return _generic_roulette(tokens, get_word_image)

def _generic_roulette(tokens, get_image_fn):
    roulette_seq = rand_seq(tokens, ROULETTE_ITEMS)
    images = [get_image_fn(s) for s in roulette_seq]
    roulette_image = roulettify_images(images)
    return roulette_image

def random_scaled_durations():
    anim_duration = ANIMATION_DURATION * uniform(0.8, 1.2)
    scale = anim_duration/TOTAL_DURATIONS
    return tuple(d * scale for d in DURATIONS)

def roulettify_images(images):
    durations = random_scaled_durations()
    roulette_image = writeGif('out/out.gif', images, durations)
    return roulette_image

def get_emote_image(emote):
    return PIL.Image.open(emote)

def get_word_image(word):
    pass
