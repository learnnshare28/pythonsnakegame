with open("highscore.txt","r") as f:
        data=f.read()
        print((data.split('""')))