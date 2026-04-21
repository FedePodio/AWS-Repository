"""liste"""

frutti = ['mele', 'pere', 'banane', 'mandarini']

# for frutto in frutti:
#     print(f"il frutto corrente è: {frutto} ed è di tipo {type(frutto)}")

# for i in range(len(frutti)):
#     print(f"il {i+1}° frutto è: {frutti[i]} ed è di tipo {type(frutti[i])}")

# for i, frutto in enumerate(frutti):
#     print(f"il {i+1}° frutto è: {frutto} ed è di tipo {type(frutto)}")

for x in enumerate(frutti):
    print(f"il valore di x è{x} ed è di tipo {type(x)}")
