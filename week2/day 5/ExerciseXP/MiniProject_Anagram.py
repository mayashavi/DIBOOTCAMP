
class AnagramChecker:
    def __init__(self, word_list_file="sowpods.txt"):
        # Load all words into a set in lowercase
        with open(word_list_file, "r") as f:
            self.words = set(line.strip().lower() for line in f if line.strip())

    def is_valid_word(self, word):
        """
        Check if the word exists in the dictionary.
        """
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        """
        Return True if word1 and word2 have the same letters (not same word).
        """
        w1 = word1.lower()
        w2 = word2.lower()

        if w1 == w2:  # same exact word is NOT an anagram
            return False

        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word):
        """
        Return a list of anagrams for the given word.
        """
        word = word.lower()
        anagrams = []

        for w in self.words:
            if self.is_anagram(word, w):
                anagrams.append(w)

        return anagrams
