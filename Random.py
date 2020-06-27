import numpy as np

Choice1, Choice2 = input('The choice between option1 '), input('or option2 ')
try:
    E = int(input('What percentage you want your option1 to be true (Default 50%) '))

except:
    E=50
def choicemaker():
    N = np.random.randint(0, 100)

    if N <= E:
        return print(N,'Then', Choice1, 'seems better')
    if N > E:
        return print(N,'Then', Choice2, 'seems good')

print('ok')
choicemaker()


