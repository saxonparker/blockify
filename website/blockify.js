var B = 0;
var E = 1;

var letters = {};

var a = [
    [B, E, B],
    [E, B, E],
    [E, E, E],
    [E, B, E],
    [E, B, E]
];

var b = [
    [E, E, E],
    [E, B, E],
    [E, E, E],
    [E, B, E],
    [E, E, E]
];

var c = [
    [E, E, E],
    [E, B, B],
    [E, B, B],
    [E, B, B],
    [E, E, E]
];

var d = [
    [E, E, E],
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, E, E]
];

var e = [
    [E, E, E],
    [E, B, B],
    [E, E, E],
    [E, B, B],
    [E, E, E]
];

var f = [
    [E, E, E],
    [E, B, B],
    [E, E, E],
    [E, B, B],
    [E, B, B]
];

var g = [
    [E, E, E],
    [E, B, B],
    [E, B, E],
    [E, B, E],
    [E, E, E]
];

var h = [
    [E, B, E],
    [E, B, E],
    [E, E, E],
    [E, B, E],
    [E, B, E]
];

var i = [
    [E, E, E],
    [B, E, B],
    [B, E, B],
    [B, E, B],
    [E, E, E]
];

var j = [
    [B, B, E],
    [B, B, E],
    [B, B, E],
    [E, B, E],
    [E, E, E]
];

var k = [
    [E, B, E],
    [E, B, E],
    [E, E, B],
    [E, B, E],
    [E, B, E]
];

var l = [
    [E, B, B],
    [E, B, B],
    [E, B, B],
    [E, B, B],
    [E, E, E]
];

var m = [
    [E, B, B, B, E],
    [E, E, B, E, E],
    [E, B, E, B, E],
    [E, B, B, B, E],
    [E, B, B, B, E]
];

var n = [
    [E, E, E],
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, B, E]
];

var o = [
    [E, E, E],
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, E, E]
];

var p = [
    [E, E, E],
    [E, B, E],
    [E, E, E],
    [E, B, B],
    [E, B, B]
];

var q = [
    [E, E, E, B],
    [E, B, E, B],
    [E, B, E, B],
    [E, B, E, B],
    [E, E, E, E]
];

var r = [
    [E, E, E],
    [E, B, E],
    [E, E, B],
    [E, B, E],
    [E, B, E]
];

var s = [
    [E, E, E],
    [E, B, B],
    [E, E, E],
    [B, B, E],
    [E, E, E]
];

var t = [
    [E, E, E],
    [B, E, B],
    [B, E, B],
    [B, E, B],
    [B, E, B]
];

var u = [
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, E, E]
];

var v = [
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [E, B, E],
    [B, E, B]
];

var w = [
    [E, B, B, B, E],
    [E, B, B, B, E],
    [E, B, E, B, E],
    [E, E, B, E, E],
    [E, B, B, B, E]
];

var x = [
    [E, B, E],
    [E, B, E],
    [B, E, B],
    [E, B, E],
    [E, B, E]
];

var y = [
    [E, B, E],
    [E, B, E],
    [E, E, E],
    [B, E, B],
    [B, E, B]
];

var z = [
    [E, E, E],
    [B, B, E],
    [B, E, B],
    [E, B, B],
    [E, E, E]
];


letters['a'] = a;
letters['b'] = b;
letters['c'] = c;
letters['d'] = d;
letters['e'] = e;
letters['f'] = f;
letters['g'] = g;
letters['h'] = h;
letters['i'] = i;
letters['j'] = j;
letters['k'] = k;
letters['l'] = l;
letters['m'] = m;
letters['n'] = n;
letters['o'] = o;
letters['p'] = p;
letters['q'] = q;
letters['r'] = r;
letters['s'] = s;
letters['t'] = t;
letters['u'] = u;
letters['v'] = v;
letters['w'] = w;
letters['x'] = x;
letters['y'] = y;
letters['z'] = z;

function blockify(emojis, text, per_letter, random)
{
    var words = text.split(" ");
    var height = 5;
    var cur_emoji = 0;

    var result = "";

    var code_emojis = [];
    var index = 0;
    while (emojis.codePointAt(index) != undefined)
    {
        var codepoint = emojis.codePointAt(index);
        code_emojis.push(codepoint);
        if (codepoint > 0x10000)
        {
            index++;
        }
        index++;
    }

    for (w = 0; w < words.length; ++w)
    {
        var word = words[w];
        for (row = 0; row < height; ++row)
        {
            for (i = 0; i < word.length; ++i)
            {
                var c = word.charAt(i);
                var letter = letters[c];
                for (j = 0; j < letter[row].length; ++j)
                {
                    var val = letter[row][j];
                    if (val == E)
                    {
                        var em = cur_emoji;
                        if (random)
                        {
                            em = Math.floor(Math.random() * code_emojis.length);
                        }
                        else if (per_letter)
                        {
                            em += i;
                        }
                        result += String.fromCodePoint(code_emojis[em % code_emojis.length]);
                    }
                    else
                    {
                        result += "\u2b1c";
                    }
                }

                if (i < word.length - 1)
                {
                    result += "\u2b1c";
                }
            }

            result += "<br>";
        }

        if (per_letter)
        {
            cur_emoji += word.length;
        }
        else if (!random)
        {
            cur_emoji++;
        }
        result += "<br>";
    }

    return result;
}

var output = blockify(String.fromCodePoint(0x1F697)+String.fromCodePoint(0x1F600), "herps derp", true, true);
//alert(output);
//console.log(output);
