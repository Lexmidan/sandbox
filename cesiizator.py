with open('C:/Users/aleks/1a/FUNGUJETO_O/example data/text.txt',encoding="utf-8") as f:
    lines = f.read()



#!!!vůbec nefunguje s velkými písmeny (ctrl+c posouvá hačky a čárky u velkých písmen
#   na konec řádku - není šance zjistit jakému písmenu patří)
#   PŘEKONTROLUJ!

result=''
char=''
skip=0
for i in range(len(lines)):
    char=lines[i]
    if skip==1:
        skip=0
        continue
    else:
        if lines[i]=='´':
            if lines[i+1]=='e':
                char='é'
                skip=1
            if lines[i+1]=='a':
                char='á'
                skip=1
            if lines[i+1]=='y':
                char='ý'
                skip=1
            if lines[i+1]=='ı':
                char='í'
                skip=1
            if lines[i+1]=='u':
                char='ú'
                skip=1
            if lines[i+1]=='o':
                char='ó'
                skip=1
        if lines[i]=='ˇ':
            if lines[i+1]=='e':
                char='ě'
                skip=1
            if lines[i+1]=='s':
                char='š'
                skip=1
            if lines[i+1]=='c':
                char='č'
                skip=1
            if lines[i+1]=='r':
                char='ř'
                skip=1
            if lines[i+1]=='z':
                char='ž'
                skip=1
            if lines[i+1]=='t':
                char='ť'
                skip=1
            if lines[i+1]=='d':
                char='ď'
                skip=1
            if lines[i+1]=='n':
                char='ň'
                skip=1
        if lines[i]=='˚':
            char='ů'
            skip=1
        result+=char
        


# with open('C:/Users/aleks/1a/FUNGUJETO_O/example data/text2.txt',encoding="utf-8", mode='w') as f:
#     f.write(result)

print(result)