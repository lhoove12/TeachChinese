class Lesson:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __str__(self):
        return f"{self.title}: {self.content}"

# 示例课程
def create_lessons():
    lesson1 = Lesson("Lesson 1", "你好 (Hello), 再见 (Goodbye)")
    lesson2 = Lesson("Lesson 2", "谢谢 (Thank you), 不客气 (You're welcome)")
    return [lesson1, lesson2]
