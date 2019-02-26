import json
import urlparse
import argparse
import sys

def create_letters(e):
    b = ':blank:'
    letters = []

    a = [
        b + e + b,
        e + b + e,
        e + e + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(a)
    
    B = [
        e + e + b,
        e + b + e,
        e + e + b,
        e + b + e,
        e + e + b,  
        ]
    letters.append(B)
    
    c = [
        e + e + e,
        e + b + b,
        e + b + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(c)
    
    d = [
        e + e + b,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + b,  
        ]
    letters.append(d)
    
    E = [
        e + e + e,
        e + b + b,
        e + e + e,
        e + b + b,
        e + e + e,  
        ]
    letters.append(E)
    
    f = [
        e + e + e,
        e + b + b,
        e + e + e,
        e + b + b,
        e + b + b,  
        ]
    letters.append(f)
    
    g = [
        b + e + e,
        e + b + b,
        e + b + e,
        e + b + e,
        b + e + e,  
        ]
    letters.append(g)
    
    h = [
        e + b + e,
        e + b + e,
        e + e + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(h)
    
    i = [
        e + e + e,
        b + e + b,
        b + e + b,
        b + e + b,
        e + e + e,  
        ]
    letters.append(i)
    
    j = [
        b + b + e,
        b + b + e,
        b + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(j)
    
    k = [
        e + b + e,
        e + b + e,
        e + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(k)
    
    l = [
        e + b + b,
        e + b + b,
        e + b + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(l)
    
    m = [
        e + b + b + b + e,
        e + e + b + e + e,
        e + b + e + b + e,
        e + b + b + b + e,
        e + b + b + b + e,  
        ]
    letters.append(m)
    
    n = [
        e + e + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(n)
    
    o = [
        e + e + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(o)
    
    p = [
        e + e + e,
        e + b + e,
        e + e + e,
        e + b + b,
        e + b + b,  
        ]
    letters.append(p)
    
    q = [
        e + e + e + b,
        e + b + e + b,
        e + b + e + b,
        e + b + e + b,
        e + e + e + e,  
        ]
    letters.append(q)
    
    r = [
        e + e + b,
        e + b + e,
        e + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(r)
    
    s = [
        b + e + e,
        e + b + b,
        b + e + b,
        b + b + e,
        e + e + b,  
        ]
    letters.append(s)
    
    t = [
        e + e + e,
        b + e + b,
        b + e + b,
        b + e + b,
        b + e + b,  
        ]
    letters.append(t)
    
    u = [
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(u)
    
    v = [
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,
        b + e + b,  
        ]
    letters.append(v)
    
    w = [
        e + b + b + b + e,
        e + b + b + b + e,
        e + b + e + b + e,
        e + e + b + e + e,
        e + b + b + b + e,    
        ]
    letters.append(w)
    
    x = [
        e + b + e,
        e + b + e,
        b + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(x)
    
    y = [
        e + b + e,
        e + b + e,
        e + e + e,
        b + e + b,
        b + e + b,  
        ]
    letters.append(y)
    
    z = [
        e + e + e,
        b + b + e,
        b + e + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(z)

    return letters

def create_numbers(e):
    b = ':blank:'
    numbers = []
    zero = [
        b + e + b,
        e + b + e,
        e + b + e,
        e + b + e,
        b + e + b,  
        ]
    numbers.append(zero)
    
    one = [
        b + e + b,
        e + e + b,
        b + e + b,
        b + e + b,
        e + e + e,  
        ]
    numbers.append(one)
    
    two = [
        e + e + b,
        b + b + e,
        b + e + b,
        e + b + b,
        e + e + e,  
        ]
    numbers.append(two)
    
    three = [
        e + e + e,
        b + b + e,
        b + e + e,
        b + b + e,
        e + e + e,  
        ]
    numbers.append(three)
    
    four = [
        e + b + e,
        e + b + e,
        e + e + e,
        b + b + e,
        b + b + e,  
        ]
    numbers.append(four)
    
    five = [
        e + e + e,
        e + b + b,
        e + e + e,
        b + b + e,
        e + e + b,  
        ]
    numbers.append(five)
    
    six = [
        b + e + e,
        e + b + b,
        e + e + e,
        e + b + e,
        e + e + e,  
        ]
    numbers.append(six)
    
    seven = [
        e + e + e,
        b + b + e,
        b + e + b,
        e + b + b,
        e + b + b,  
        ]
    numbers.append(seven)
    
    eight = [
        e + e + e,
        e + b + e,
        e + e + e,
        e + b + e,
        e + e + e,  
        ]
    numbers.append(eight)
    
    nine = [
        e + e + e,
        e + b + e,
        e + e + e,
        b + b + e,
        e + e + b,  
        ]
    numbers.append(nine)

    return numbers

def create_symbols(e):
    b = ':blank:'
    symbols = {}
    question = [
        e + e + e,
        e + b + e,
        b + b + e,
        b + e + b,
        b + e + b,
        ]
    symbols['?'] = question

    exclamation = [
        b + e + b,
        b + e + b,
        b + e + b,
        b + b + b,
        b + e + b,
        ]
    symbols['!'] = exclamation

    #Can't really form a good dollar sign interpretation with 3x5 resolution.
    dollarSign = [
        e + e + e,
        e + e + b,
        e + e + e,
        b + e + e,
        e + e + e,
        ]
    symbols['$'] = dollarSign

    equal = [
        b + b + b,
        e + e + e,
        b + b + b,
        e + e + e,
        b + b + b,
    ]
    symbols['='] = equal

    minus = [
        b + b + b,
        b + b + b,
        e + e + e,
        b + b + b,
        b + b + b,
    ]
    symbols['-'] = minus

    plus = [
        b + b + b,
        b + e + b,
        e + e + e,
        b + e + b,
        b + b + b,
    ]  
    symbols['+'] = plus
    return symbols

def construct_message(options):
    parser = argparse.ArgumentParser(description='Print block letters made of emojis')
    parser.add_argument('emojis', 
    help="""The emojis to use to make characters. This must be a single string.
          The code will split on \':\'""")
    parser.add_argument('text', nargs='+', help='The text to print')
    parser.add_argument('-l', action='store_true', help='Use multiple emojis per letter. If theres only one word to print this will be default')

    args = parser.parse_args(options)
    
    text = args.text

    per_letter = args.l
    if len(text) == 1:
        per_letter = True
    
    emojis = args.emojis.split(':')
    emojis = [e for e in emojis if e]

    for i in range(len(emojis)):
        if emojis[i][0] != ':':
           emojis[i] = ':' + emojis[i]
        if emojis[i][-1] != ':':
            emojis[i] += ':'

    for i in range(len(emojis)):
        if 'skin-tone' in emojis[i]:
            if i > 0:
                emojis[i-1] = emojis[i-1] + emojis[i]
            del emojis[i]
    
    # If only skin-tone was provided, the emoji array could be empty now, which will
    # cause an error below
    if len(emojis) == 0:
        return 'Cannot provide only a skin-tone emoji'

    letters = []
    numbers = []
    symbols = []
    symbol_keys = create_symbols('a').keys()
    for e in emojis:
        letters.append(create_letters(e))
        numbers.append(create_numbers(e))
        symbols.append(create_symbols(e))

    b = ':blank:'
    message = ''
    blockheight = 5
    e = 0
    for word in text:
        wordstart = e
        for i in range(blockheight):
            line = ''
            if per_letter:
                e = wordstart
            for char in word:
                if len(line) != 0:
                    line += b
                if char.isalpha():
                    block = letters[e % len(letters)][ord(char.lower()) - ord('a')][i]
                    line += block
                elif char.isdigit():
                    block = numbers[e % len(numbers)][ord(char) - ord('0')][i]
                    line += block
                elif char in symbol_keys: #There does not appear to be a built-in check for symbols.
                    block = symbols[e% len(symbols)][char][i]
                    line += block
                if per_letter:
                    e = e + 1
            message += line + '\n'
        message += '\n\n'
        if not per_letter:
            e = e + 1
    return message

def lambda_handler(event, context):
    print event
     
    params = urlparse.parse_qs(event['body'])
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
    print command
    opts = command.split(' ')
    print opts
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
    print message

if __name__ == "__main__":
    main()
