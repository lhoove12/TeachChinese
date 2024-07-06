class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def check_answer(self, user_answer):
        return self.answer == user_answer

# 示例测验
def create_quizzes():
    quiz1 = Quiz("How to say 'Hello' in Chinese?", "你好")
    quiz2 = Quiz("How to say 'Thank you' in Chinese?", "谢谢")
    return [quiz1, quiz2]
