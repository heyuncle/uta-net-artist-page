from bs4 import BeautifulSoup
import requests
import lxml
from text_difficulty import difficulty_eval

def gen_artist_html(artist_id, tagger):
    r = requests.get(f"https://www.uta-net.com/artist/{artist_id}")
    page = BeautifulSoup(r.text, 'lxml')
    sl = page.find("div", class_="songlist-table-block")
    names = sl.find_all("span", class_="songlist-title")
    lyrics = sl.find_all("span", class_="utaidashi")
    artist = sl.find("h2").text[7:-30]
    songs = []
    for i in range(len((lyrics))):
        diff = difficulty_eval(lyrics[i].contents[0].text.replace('\u3000', ' '), tagger)
        if diff!=-1:
            songs.append((diff, '\n' + '## ' + names[i].text + '\n' + '### JLPT N' + str(diff) + '\n' + lyrics[i].contents[0].text.replace('\u3000\u3000', '  \n').replace('\u3000', ' ')))
    sort_songs = sorted(songs, key=lambda tup: tup[0], reverse=True)
    with open("./output/" + artist + ".html","w+") as f:
        f.write(r'''<body id="md" style="background-color:#1E1E1E;font-family:'Helvetica Neue',Helvetica,sans-serif;color:#D4D4D4;padding:20px">''')
        f.write('\n# ' + artist)
        for tup in sort_songs:
            f.write(tup[1])
        f.write('\n')
        f.write(r'''</div><script src="https://unpkg.com/showdown/dist/showdown.min.js"></script><script>var c = new showdown.Converter();document.getElementById('md').innerHTML = c.makeHtml(document.getElementById('md').innerHTML);</script>''')