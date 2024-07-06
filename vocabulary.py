class Vocabulary:
    def __init__(self):
        self.words = []
    
    def add_word(self, chinese, pinyin, english):
        self.words.append({"chinese": chinese, "pinyin": pinyin, "english": english})
    
    def __str__(self):
        return '\n'.join([f"{word['chinese']} ({word['pinyin']}): {word['english']}" for word in self.words])

# 示例词汇
def create_vocabulary():
    vocab = Vocabulary()
    vocab.add_word("你好", "nǐ hǎo", "Hello")
    vocab.add_word("谢谢", "xièxiè", "Thank you")
    return vocab
