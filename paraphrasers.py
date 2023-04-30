from abc import ABC, abstractmethod
from parsers import Parser
import itertools
from nltk import Tree


class Paraphraser(ABC):
    @abstractmethod
    def paraphrase_text(self, text, limit=20):
        """Abstract base class for paraphrasers"""
        pass


class Paraphrase:
    def __init__(self, paraphraser: Paraphraser):
        self.paraphraser = paraphraser

    def paraphrase_text(self, text, limit=20):
        """Paraphrase a given text using the selected paraphrasing method."""
        return self.paraphraser.paraphrase_text(text, limit)
    

class ParaphraserMethod1(Paraphraser):
    def paraphrase_text(self, text, limit=20):
        """Paraphrase a given text using Method 1."""
        tree = Tree.fromstring(text)
        noun_phrases = Parser.get_noun_phrases(tree)
        paraphrases = []

        for r in range(2, len(noun_phrases) + 1):
            combinations = itertools.combinations(noun_phrases, r)
            for combination in combinations:
                for permutation in itertools.permutations(combination):
                    paraphrase = tree.copy(deep=True)
                    for np in combination:
                        Parser.remove_subtree(paraphrase, np)
                    for i, np_perm in enumerate(permutation):
                        paraphrase.insert(i, np_perm)
                    paraphrase_str = paraphrase.pformat(margin=float('inf'))
                    paraphrases.append({'tree': paraphrase_str})

                    if len(paraphrases) == limit:
                        return paraphrases

        return paraphrases[:limit]
