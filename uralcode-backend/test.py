from request import req_to_chat, generate_token
from utils import json_to_dict_list
import docx

text = "\n".join([s.text for s in docx.Document("file_1.docx").paragraphs])
prompt_list = [
    "Титульный лист",
    "Список исполонителей",
    "Реферат",
    "Содержание",
    "Термины и определения",
    "Введение",
    "Заключение",
    "Список использованных источников",
    "Оценка современного состояния проблемы",
    "Основание и исходные данные для разработки темы",
    "Обоснование необходимости проведения работы",
    "Актуальность и новизна темы присутствуют",
    "Цель и задачи исследования присутствуют",
    "Выводы по результатам работы или отдельных ее этапов",
    "Оценка полноты решений поставленных задач",
    "Разработка рекомендаций и исходных данных по конкретному использованию результатов НИР",
    "Результаты оценки технико-экономической эффективности внедрения",
    "Результаты оценки научно-технического уровня выполненной НИР в сравнении с лучшими достижениями в этой области",
    "Наличие всех источников литературы в тексте работы",
    "Следование индексации от наименьшего к наибольшем",

]
prompts = json_to_dict_list("prompts.json")[0]
ans = dict()
token = generate_token()
check_list = [0] * 20

s = req_to_chat(". ".join(prompts["Анализ структуры"]), text, token)
if ',' in s:
    s = list(map(int, s.split(', ')))
else:
    s = list(map(int, list(s)))
for i in s[0:8]:
    check_list[i - 1] = 1

s = req_to_chat(". ".join(prompts["Анализ введения"]), text, token)
if ',' in s:
    s = list(map(int, s.split(', ')))
else:
    s = list(map(int, list(s)))

for i in s[0:5]:
    check_list[i + 7] = 1

s = req_to_chat(". ".join(prompts["Анализ заключения"]), text, token)
if ',' in s:
    s = list(map(int, s.split(', ')))
else:
    s = list(map(int, list(s)))
for i in s[0:5]:
    check_list[i + 12] = 1

s = req_to_chat(". ".join(prompts["Анализ литературы"]), text, token)
if ',' in s:
    s = list(map(int, s.split(', ')))
else:
    s = list(map(int, list(s)))
for i in s[0:2]:
    check_list[i + 17] = 1

ans = ""
for i in range(20):
    if check_list[i]:
        ans += f'{prompt_list[i]}: +\n'
    else:
        ans += f'{prompt_list[i]}: -\n'
print(ans)
# ans["Анализ структуры"] = req_to_chat(prompts[0]["Анализ структуры"], s, token)
# ans["Анализ введения"] = req_to_chat(prompts[0]["Анализ введения"], s, token)
# ans["Анализ заключения"] = req_to_chat(prompts[0]["Анализ заключения"], s, token)
# ans["Анализ списка литературы"] = req_to_chat(prompts[0]["Анализ списка литературы"], s, token)
# for item in ans.items():
#     print(item[0], ":", item[1])