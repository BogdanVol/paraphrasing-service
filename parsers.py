
class Parser:
    @staticmethod
    def remove_subtree(tree, subtree):
        """Remove a subtree from a given tree."""
        if subtree in tree:
            tree.remove(subtree)

    @staticmethod
    def get_noun_phrases(tree):
        """Get all noun phrases from a given tree."""
        noun_phrases = [subtree for subtree in tree.subtrees() if subtree.label() == 'NP']
        return noun_phrases
    