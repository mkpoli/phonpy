"""
A tool for plotting vowels as a formant plot.

TODO: A library for phoneticians.
"""
from matplotlib import pyplot

# i,y 1,} M,u
# STANDARD_F1 = [300, 300, 300, 400, 400, 400]
# STANDARD_F2 = [2400, 2000, 1400, 2300, 1500, 640]


def draw_standard():
    """Draw standard grid."""
    pyplot.plot([3000, 1000], [300, 300], 'k--')
    pyplot.plot([2500, 1000], [500, 500], 'k--')
    pyplot.plot([2000, 1000], [700, 700], 'k--')
    pyplot.plot([1500, 1000], [900, 900], 'k--')

    pyplot.plot([3000, 1500], [300, 900], 'k--')
    pyplot.plot([2000, 1250], [300, 900], 'k--')
    pyplot.plot([1000, 1000], [300, 900], 'k--')

def plot_vowels(f1, f2, vowel=None, standard=False):
    """
    Plot vowels from data.

    All list of data arguments must have the same dimension.(length)

    Arguments:
    f1 - list of frequency of formant 1 by Hz as number.
    f2 - list of frequency of formant 2 by Hz as mumber.

    Optinal Arguments:
    vowel - list of vowel, mus
    """
    # for row in data:
    #     pyplot.plot(row["F1"], row["F2"])
    # for i in range(0, len(f1)):
    #     print(f1[i], f2[i])

    if len(f1) != len(f2):
        raise IndexError("Unequal dimensions for 'f1' and 'f2'.")
    elif vowel and len(vowel) != len(f1):
        raise IndexError("Unequal dimensions for 'f1' and 'vowel'.")

    if standard:
        draw_standard()
    pyplot.plot(f2, f1, "o")

    pyplot.ylabel("F1 (Hz)")
    pyplot.xlabel("F2 (Hz)")
    if vowel:
        for i in range(0, len(f1)):
            print(vowel[i])
            pyplot.text(float(f2[i]) - 10, float(f1[i]) - 10, vowel[i])
    pyplot.axis([3500, 500, 1000, 100]) # TODO: Changable axis limit.
    pyplot.show()
