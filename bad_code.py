
def (filepath):
    cnt = 0
    # open data file
    with open(filepath) as f:
        for line in f:
            line = line.strip()  # strip whitespace
            if line.startswith('DATA'):
                cnt += 1  # increment counter



        #some code block -> make it a function


        # annother code block -> make it a function