# Implementation
''' write code here '''
class WordWrapper:
    def __init__(self, text):
        self.text = text

    def __lt__(self, s):
        # (self < (is less than) s)
        if len(self.text) != len(s.text):
            return len(self.text) < len(s.text)
        return self.text < s.text

def sort_words(words):
    words = set(words)
    words = [WordWrapper(text=word) for word in words]

    words = sorted(words)
    return [word.text for word in words]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert sort_words(['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']) == ['i', 'im', 'it', 'no', 'but', 'more', 'wait', 'wont', 'yours', 'cannot', 'hesitate']

    print("TEST DONE")

# Submit
def submit():
    n = int(input())
    words = [None] * n

    for i in range(n):
        words[i] = input()

    result = sort_words(words)
    for word in result:
        print(word)

# Case-switch
if __name__ == '__main__':
    submit()