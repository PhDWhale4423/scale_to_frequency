import re


def scale_to_frequency(scale):
    pattern = r"[A-G]#?[0-9]"
    matchObj = re.match(pattern, scale)
    if not matchObj:
        print("Illegal scale (1)")
        exit()

    # B# and E# is not exist
    pattern = "[BE]#[0-9]"
    matchObj = re.match(pattern,    scale)
    if matchObj:
        print("Illegal scale (2)")
        exit()
    # A#0 -> 0
    if scale[0] == 'A' or scale[0] == 'B':
        f = 27.5*(2**int(scale[-1]))
    else:
        f = 27.5*(2**(int(scale[-1])-1))

    # A#0 -> A#
    pitch_name = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    n = pitch_name.index(scale[0:-1])
    f = f*((2**(1/12))**n)

    return f
    

if __name__ == "__main__":
    s = input("Input Scale (\"q\":exit) : ")
    while(s != "q"):
        f = scale_to_frequency(s)
        print("frequency: " + str(f) + "(Hz)")
        s = input("Input Scale (\"q\":exit) : ")