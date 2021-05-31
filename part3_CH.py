s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
lala = s.split(" ")
for i in range(len(lala)):

    if (i % 2 == 0):
        print(i) # i must be even
        #lalaupp = [i.upper() for i in lala]
        # this does something for EACH element in lala but you just want the ith element.
        # Also, it uses i as loop variable for the "for loop" and I don't know if that
        # overwrites the i from the range loop (???)

        # grab element with index i, uppercase and print
        print(lala[i].upper())
    else:
        print(i) # not even
        print(lala[i]) # grab element with odd index i and just print
