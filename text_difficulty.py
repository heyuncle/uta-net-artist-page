import math

def difficulty_eval(sample, tagger):
    parsed = tagger.parse(sample).split("\n")
    indices = []
    with open("corpus/freq_20k.txt", "r", encoding="utf8") as f:
        freq = f.read().split("\n")
        for col in [token.split() for token in parsed]:
            # keiyoushi, meishi (not proper), doushi, has columns, does not start with a non-kana or kanji (not English)
            if len(col)>4 and (col[4][:3]=='形容詞' or col[4][:7]=='名詞-普通名詞' or col[4][:2]=='動詞') and not (ord(col[0][0])<1000 or ord(col[3][0])<1000):
                try:
                    surface = freq.index(col[0])
                except ValueError:
                    surface = 20000
                if col[0]!=col[3]:
                    try:
                        lemma = freq.index(col[3])
                    except ValueError:
                        lemma = 20000
                    indices.append(min(surface, lemma))
                else:
                    indices.append(surface)
    if len(indices)==0:
        print("Non-japanese song found")
        return -1
    # average of mid 50%
    quartiles = sorted(indices)[len(indices)//4:3*len(indices)//4]
    mid_avg = sum(quartiles)//len(quartiles)
    # normalize to JLPT level
    return round(math.log(mid_avg/18787)*-1.695, 1)