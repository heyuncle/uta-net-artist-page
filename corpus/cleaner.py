with open("raw_freq_20k.txt","r") as f:
    with open("freq_20k.txt","w+") as g:
        for line in f.readlines():
            g.write(line.split("	")[-2][:-1]+"\n")