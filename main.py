import content_load
import utils
import statistic

questions = []

for question in content_load.get_content():
    for_question = utils.Questions(question['q'], question['d'], question['a'])
    for_question.build_question()
    user_answer = input('Ответ:')
    if for_question.is_correct(user_answer):
        for_question.build_positive_feedback()
    else:
        for_question.build_negative_feedback()
    questions.append({"answer_bool": for_question.is_correct(user_answer), "check_points": for_question.points})

statistic.check_statistic(questions)