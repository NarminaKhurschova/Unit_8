class Questions:
    def __init__(self, question_text, difficulty_level, true_answer):
        self.question_text = question_text
        self.difficulty_level = difficulty_level
        self.true_answer = true_answer
        self.is_question = False
        self.is_answer = None
        self.points = int(difficulty_level) * 10

    def is_correct(self, user_answer):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False."""
        if self.true_answer == user_answer:
            return True
        else:
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        print(f"Вопрос {self.question_text}\nСложность: {self.difficulty_level}/5")

    def build_positive_feedback(self):
        """Возвращает:
         Ответ верный, получено __ баллов"""
        print(f"Ответ верный, получено {self.points} баллов")

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __"""
        print(f"Ответ неверный, верный ответ {self.true_answer}")




