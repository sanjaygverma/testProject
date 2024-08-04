class WordSearch:
    """
        Class which searches words with different techniques
        first one uses built in method of python.
    """

    def find_word(self, stmt: str, letter: str) -> str | None:
        """
        :param stmt:
        :param letter:
        :return:
        """
        if len(stmt.strip()) == 0:
            raise Exception("no empty spaces string is allowed")

        prev_letter_count = -1
        prev_word = None
        result = None

        for word in stmt.split():
            curr_letter_count = word.count(letter)  # case - 0
            if curr_letter_count > prev_letter_count:
                result = word
                prev_letter_count = curr_letter_count
                prev_word = word
            elif curr_letter_count == prev_letter_count:
                if len(word) == len(prev_word):
                    result = prev_word
                elif len(word) > len(prev_word):
                    result = word
        return result


#if __name__ == "__main__":
#    ws = WordSearch()
