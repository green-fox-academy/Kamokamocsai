class Anagram(object):

    def anagram(self, word1, word2):
        if len(word1) == len(word2):
            word_list = []
            for i in word2:
                word_list.append(i)
            for i in word1:
                if i in word_list:
                    word_list.remove(i)
                if len(word_list) == 0:
                    return True
        return False