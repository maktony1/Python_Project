from wordcloud import WordCloud
text = ""
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text+=line.replace('오전','').replace('오후','')\
            .replace('ㅋ','').replace('ㅎ','').replace('사진','').replace('이모티콘','')


font_path = 'C:/Windows/Fonts/malgun.ttf'
print(text)
wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result2.png")


