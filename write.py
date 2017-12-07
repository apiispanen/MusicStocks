### THESE FUNCTIONS TAKE THE POPULARITY SCORES AND SAVE THEM INTO THE TXT FILE "HISTORY.TXT" #####

from artist import search
def store(name, investment):
    l = open('history2.txt', 'w')
    def rewrite(info):
        r = open('history2.txt', 'a')
        r.write(info+'\n')
        r.close()
        
    import os
    entry = str(search(name))
    entry = entry.lower()
    name = name.lower()
    b = open('history.txt', 'r')
    a = open('history.txt', 'a')
    
       
    thefile = open('history.txt', 'r').read()
    i=0
    for line in thefile.splitlines():
        if line.lower()[0:3]==name[0:3]:
            artist_line = line
            artist_line = artist_line+','+entry 
            rewrite(artist_line)
        else:
            etc_line = line
            rewrite(etc_line)
        i+=1
    if name not in b.read():
        rewrite(name+ ' for $'+ str(investment)+': '+entry)
        artist_line = name+ ' for $'+ str(investment)+': '+entry
        # artist_line = entry
    status = artist_line
    return status
    print(status)
    
    
    
def detail(status):
    import os
    os.remove('history.txt')
    os.rename('history2.txt', 'history.txt')
    while True:
        try:
            change = int(status[-5]+status[-4])-int(status[status.find(':')+1:status.find(':')+4])
            return 'The current popularity of the artist has upgraded by {} since the initial view.'.format(change)
            break
        except ValueError:
            return 'No analysis available. This is the initial entry.'

# x=store('Jack Johnson', 3000)
# print(x)
# print(detail(x))