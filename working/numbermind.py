class Guess():
    def __init__(self, seq, correct):
        self.seq = seq
        self.correct = correct

guesses = []
for guess in open('numbermind.txt', 'r').read().split('\n'):
    guesses.append(Guess(guess.split(' ')[0], guess.split(';')[1][0]))


for guess in guesses:
    print(guess.seq + ' ' + guess.correct)

