# 819. Most Common Word
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # convert paragraph to lower
        # get rid of punctuations
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())  # Replace non-word characters with spaces

        paragraph = paragraph.split()

        filtered_words = [word for word in paragraph if word not in banned]

        word_counts = Counter(filtered_words)
        most_common_word, _ = word_counts.most_common(1)[0]

        return most_common_word
                