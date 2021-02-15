### Difficulty selector | Hangman Project
### 13.03.2020

# Sets the word pool for the selected difficulty

import re
import numpy as np
from numpy.random import default_rng


class Difficulty:

    @staticmethod
    def word_bank():

        wordBank_untrimmed = []
        wordBank_trimmed = []

        # opens txt file with words for game selection
        with open('words.txt', 'r') as selectionFile:
            for line in selectionFile:
                line = line.rstrip()
                line = line.upper()
                if 4 <= len(line) <= 10:

                    pattern = r"(^\w+['].*)"
                    match = re.match(pattern, line)

                    if not match:
                        wordBank_untrimmed.append(line)

                else:
                    continue

        wordBank_subset = np.random.randint(0, len(wordBank_untrimmed), size=10000)
        for num in wordBank_subset:
            wordBank_trimmed.append(wordBank_untrimmed[num])

        return wordBank_trimmed

    @staticmethod
    def easy_modify():
        # No words with letter X, Z, Q, J
        wordBank_trimmed = Difficulty.word_bank()
        easy_bank = []

        for word in wordBank_trimmed:
            pattern = r'(\w*(X|Z|J|Q)\w*)'
            removed = re.match(pattern, word)

            if removed:
                continue
            elif not removed:
                easy_bank.append(word)

        return easy_bank

    @staticmethod
    def hard_modify():
        # No words with letter R, S, T, L, N, E
        wordBank_trimmed = Difficulty.word_bank()
        hard_bank = []

        for word in wordBank_trimmed:
            pattern = r'(\w*(R|S|T|L|N|E)\w*)'
            removed = re.match(pattern, word)

            if removed:
                continue
            elif not removed:
                hard_bank.append(word)

        return hard_bank
