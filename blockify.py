import argparse
import json
import random
import sys
import urllib.parse

e = 'e'
b = 'b'

characters = {}

_a = [
    b + e + b,
    e + b + e,
    e + e + e,
    e + b + e,
    e + b + e,
]

_b = [
    e + e + b,
    e + b + e,
    e + e + b,
    e + b + e,
    e + e + b,
]

_c = [
    e + e + e,
    e + b + b,
    e + b + b,
    e + b + b,
    e + e + e,
]

_d = [
    e + e + b,
    e + b + e,
    e + b + e,
    e + b + e,
    e + e + b,
]

_e = [
    e + e + e,
    e + b + b,
    e + e + e,
    e + b + b,
    e + e + e,
]

_f = [
    e + e + e,
    e + b + b,
    e + e + e,
    e + b + b,
    e + b + b,
]

_g = [
    b + e + e,
    e + b + b,
    e + b + e,
    e + b + e,
    b + e + e,
]

_h = [
    e + b + e,
    e + b + e,
    e + e + e,
    e + b + e,
    e + b + e,
]

_i = [
    e + e + e,
    b + e + b,
    b + e + b,
    b + e + b,
    e + e + e,
]

_j = [
    b + b + e,
    b + b + e,
    b + b + e,
    e + b + e,
    e + e + e,
]

_k = [
    e + b + e,
    e + b + e,
    e + e + b,
    e + b + e,
    e + b + e,
]

_l = [
    e + b + b,
    e + b + b,
    e + b + b,
    e + b + b,
    e + e + e
]

_m = [
    e + b + b + b + e,
    e + e + b + e + e,
    e + b + e + b + e,
    e + b + b + b + e,
    e + b + b + b + e,
]

_n = [
    e + e + e,
    e + b + e,
    e + b + e,
    e + b + e,
    e + b + e,
]

_o = [
    e + e + e,
    e + b + e,
    e + b + e,
    e + b + e,
    e + e + e,
]

_p = [
    e + e + e,
    e + b + e,
    e + e + e,
    e + b + b,
    e + b + b,
]

_q = [
    e + e + e + b,
    e + b + e + b,
    e + b + e + b,
    e + b + e + b,
    e + e + e + e,
]

_r = [
    e + e + b,
    e + b + e,
    e + e + b,
    e + b + e,
    e + b + e,
]

_s = [
    b + e + e,
    e + b + b,
    b + e + b,
    b + b + e,
    e + e + b,
]

_t = [
    e + e + e,
    b + e + b,
    b + e + b,
    b + e + b,
    b + e + b,
]

_u = [
    e + b + e,
    e + b + e,
    e + b + e,
    e + b + e,
    e + e + e,
]

_v = [
    e + b + e,
    e + b + e,
    e + b + e,
    e + b + e,
    b + e + b,
]

_w = [
    e + b + b + b + e,
    e + b + b + b + e,
    e + b + e + b + e,
    e + e + b + e + e,
    e + b + b + b + e,
]

_x = [
    e + b + e,
    e + b + e,
    b + e + b,
    e + b + e,
    e + b + e,
]

_y = [
    e + b + e,
    e + b + e,
    e + e + e,
    b + e + b,
    b + e + b,
]

_z = [
    e + e + e,
    b + b + e,
    b + e + b,
    e + b + b,
    e + e + e,
]

characters['a'] = _a
characters['b'] = _b
characters['c'] = _c
characters['d'] = _d
characters['e'] = _e
characters['f'] = _f
characters['g'] = _g
characters['h'] = _h
characters['i'] = _i
characters['j'] = _j
characters['k'] = _k
characters['l'] = _l
characters['m'] = _m
characters['n'] = _n
characters['o'] = _o
characters['p'] = _p
characters['q'] = _q
characters['r'] = _r
characters['s'] = _s
characters['t'] = _t
characters['u'] = _u
characters['v'] = _v
characters['w'] = _w
characters['x'] = _x
characters['y'] = _y
characters['z'] = _z

_0 = [
    b + e + b,
    e + b + e,
    e + b + e,
    e + b + e,
    b + e + b,
]

_1 = [
    b + e + b,
    e + e + b,
    b + e + b,
    b + e + b,
    e + e + e,
]

_2 = [
    e + e + b,
    b + b + e,
    b + e + b,
    e + b + b,
    e + e + e,
]

_3 = [
    e + e + e,
    b + b + e,
    b + e + e,
    b + b + e,
    e + e + e,
]

_4 = [
    e + b + e,
    e + b + e,
    e + e + e,
    b + b + e,
    b + b + e,
]

_5 = [
    e + e + e,
    e + b + b,
    e + e + e,
    b + b + e,
    e + e + b,
]

_6 = [
    b + e + e,
    e + b + b,
    e + e + e,
    e + b + e,
    e + e + e,
]

_7 = [
    e + e + e,
    b + b + e,
    b + e + b,
    e + b + b,
    e + b + b,
]

_8 = [
    e + e + e,
    e + b + e,
    e + e + e,
    e + b + e,
    e + e + e,
]

_9 = [
    e + e + e,
    e + b + e,
    e + e + e,
    b + b + e,
    e + e + b,
]

characters['0'] = _0
characters['1'] = _1
characters['2'] = _2
characters['3'] = _3
characters['4'] = _4
characters['5'] = _5
characters['6'] = _6
characters['7'] = _7
characters['8'] = _8
characters['9'] = _9

_question = [
    e + e + e,
    e + b + e,
    b + b + e,
    b + e + b,
    b + e + b,
]

_exclamation = [
    b + e + b,
    b + e + b,
    b + e + b,
    b + b + b,
    b + e + b,
]

# Can't really form a good dollar sign interpretation with 3x5 resolution.
_dollarSign = [
    e + e + e,
    e + e + b,
    e + e + e,
    b + e + e,
    e + e + e,
]

_equal = [
    b + b + b,
    e + e + e,
    b + b + b,
    e + e + e,
    b + b + b,
]

_minus = [
    b + b + b,
    b + b + b,
    e + e + e,
    b + b + b,
    b + b + b,
]

_plus = [
    b + b + b,
    b + e + b,
    e + e + e,
    b + e + b,
    b + b + b,
]

_apostrophe = [
    e,
    e,
    b,
    b,
    b,
]

_hashtag = [
    b + e + b + e + b,
    e + e + e + e + e,
    b + e + b + e + b,
    e + e + e + e + e,
    b + e + b + e + b,
]

characters['?'] = _question
characters['!'] = _exclamation
characters['$'] = _dollarSign
characters['='] = _equal
characters['-'] = _minus
characters['+'] = _plus
characters['\''] = _apostrophe
characters['#'] = _hashtag


def construct_message(options):
    parser = argparse.ArgumentParser(
        description='Print block letters made of emojis')
    parser.add_argument('emojis',
                        help="""The emojis to use to make characters. This must be a single string.
          The code will split on \':\'""")
    parser.add_argument('text', nargs='+', help='The text to print')
    parser.add_argument('-l', action='store_true',
                        help='Use a different emoji per letter. If theres only one word to print this will be default')
    parser.add_argument('-b', action='store', dest='blank',
                        default=':blank:', help='Specify the emoji to use for blank space')
    parser.add_argument('-r', action='store_true',
                        help="Use a random emoji for every emoji in the block. This will take precedence over -l")

    args = parser.parse_args(options)

    text = args.text

    per_letter = args.l
    if len(text) == 1:
        per_letter = True

    use_random = args.r

    emojis = args.emojis.split(':')
    emojis = [e for e in emojis if e]

    # add any missing ':'
    for i in range(len(emojis)):
        if emojis[i][0] != ':':
            emojis[i] = ':' + emojis[i]
        if emojis[i][-1] != ':':
            emojis[i] += ':'

    # handle skin tones
    for i in range(len(emojis)):
        if 'skin-tone' in emojis[i]:
            if i > 0:
                emojis[i-1] = emojis[i-1] + emojis[i]
            del emojis[i]

    # If only skin-tone was provided, the emoji array could be empty now, which will
    # cause an error below
    if len(emojis) == 0:
        return 'Cannot provide only a skin-tone emoji'

    blank = args.blank
    if blank[0] != ':':
        blank = ':' + blank
    if blank[-1] != ':':
        blank += ':'

    message = ''
    blockheight = 5
    emoji_index = 0

    # for each word in the message
    for word in text:
        # store the current emoji index. This is needed to keep per_letter accurate in each row
        wordstart = emoji_index

        # for each row in the block letters
        for row in range(blockheight):
            line = ''
            if per_letter:
                emoji_index = wordstart

            # for each character in the word
            for char in word:
                # Prepend a blank character between characters
                if len(line) != 0:
                    line += blank
                block = characters[char]

                # for each column in the block
                for col in range(len(block[row])):
                    if block[row][col] == e:
                        em = emojis[emoji_index]
                        if (use_random):
                            em = random.choice(emojis)
                        line += em
                    else:
                        line += blank

                if per_letter:
                    emoji_index = (emoji_index + 1) % len(emojis)

            message += line + '\n'

        message += '\n\n'

        if not per_letter:
            emoji_index = (emoji_index + 1) % len(emojis)

    return message


def lambda_handler(event, context):
    print(event)

    params = urllib.parse.parse_qs(event['body'])
    message = ''
    if 'text' not in params or not params['text']:
        message = 'Bad Request'
        return {
            'statusCode': str(200),
            'body': json.dumps({'text': message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    command = params['text'][0]
    print(command)
    opts = command.split(' ')
    print(opts)
    if len(opts) < 2:
        message = 'Must provide emoji and text'
        return {
            'statusCode': str(200),
            'body': json.dumps({'text': message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    message = construct_message(opts)

    return {
        'statusCode': str(200),
        'body': json.dumps({"response_type": "in_channel", 'text': message}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }


def main():
    message = construct_message(sys.argv[1:])
    print(message)


if __name__ == "__main__":
    main()
