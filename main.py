import MeCab
import sys
from artist_page import gen_artist_html

def main():
    t = MeCab.Tagger()
    try:
        id = int(sys.argv[1])
        gen_artist_html(sys.argv[1], t) # artist_id in url on uta-net.com
    except:
        print("Failed to get songs for artist")

if __name__ == '__main__':
    main()