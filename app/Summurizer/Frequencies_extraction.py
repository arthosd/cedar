import nltk
from nltk.corpus import stopwords
from app.log.log import lprint

"""
Based on word frequencies in a corpus of text
"""


class Summurizer:

    def __init__(self, text):
        self.__text = text.lower()           # Raw text
        self.__split_text = text.split(".")  # Splited text
        self.__tokens = None                 # Words withouts stop words
        self.__selected = []                 # Selected text for resume

    def _ext_sum_up_tokens(self, props):

        temp_text = self.__split_text
        sentences_weigth = []
        temp_weigth = 0.0

        # adding up all the words with their props
        for sentence in temp_text:
            tokens = nltk.word_tokenize(sentence)

            try:
                for word in tokens:
                    temp_weigth = temp_weigth + \
                        float(props[self.__tokens.index(word)])

                break
            except ValueError:
                lprint("Value Error",3)
                pass

            sentences_weigth.append(temp_weigth)
            temp_weigth = 0

        index = -1
        compteur = 0
        number = None

        for w in sentences_weigth:

            if number == None:
                number = w
                index = compteur
            else:
                if w > number:
                    number = w
                    index = compteur

            compteur = compteur + 1

        return index

    def _ext_preproccess(self):

        tokens = []
        occurences = []
        props = []

        # Divise text in sentences in regards of points
        sentences = self.__split_text

        # Tokenize sentences
        for sentence in sentences:

            temp = nltk.word_tokenize(sentence)

            for t in temp:
                tokens.append(t)

        # Removing stop words
        for token in tokens:
            for word in stopwords.words('english'):
                if token == word:
                    tokens.remove(token)
        self.__tokens = tokens

        # Calculate Occurences of each words
        for token in tokens:
            occurences.append(tokens.count(token))

        # Calculate occurences dividing by greatest occurences
        for occurence in occurences:
            props.append(occurence/max(occurences))

        return props

    def extractive_summurize(self):

        props = self._ext_preproccess()
        max_index = self._ext_sum_up_tokens(props)

        print (self.__tokens)
        return self.__split_text[max_index]


"""text = "je suis un text"
s = Summurizer(text)
print(s.extractive_summurize())"""
