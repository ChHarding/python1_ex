s = "A very long description" # a long string
filler = "..."

def abbr(s, h=5): # if no second arg is given set h to 5

    # In general Python doesn't bother to check if the type is correct
    # It would instead just let it bomb or use a try/except clause
    if isinstance(h, int) is True:
        starting = s[0:h]
        filler = "..."
        ending = s[-h:]
        print(starting, filler, ending, sep="") 
    else:
        print(h, "is not a valid integer.")


abbr(s)
abbr(s, 7)
abbr(s, 12)
abbr(s, 15) # what's happening here?
abbr(s, 20)
abbr(s, "not an int!")
