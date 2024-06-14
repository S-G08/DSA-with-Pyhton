def printsubs(s,o=""):
    if len(s)==0:
        print(o)
        return
    printsubs(s[1:],o)
    new_output=o+s[0]
    printsubs(s[1:],new_output)

printsubs("abc")