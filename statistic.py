def check_statistic(list_of_answers):
    # Выводит статистику в нужном формате
    true_answers = []
    all_points = 0
    for element in list_of_answers:
        if element['answer_bool']:
            true_answers.append(element)
            all_points += element['check_points']
        else:
            pass
    print(f"Вот и всё!\nОтвечено {len(true_answers)} вопроса из {len(list_of_answers)}\nНабрано баллов: {all_points}")