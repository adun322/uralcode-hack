from fastapi import FastAPI, UploadFile
from request import req_to_chat, generate_token
from utils import json_to_dict_list
from starlette.middleware.cors import CORSMiddleware
import docx

# Код веб-приложения, способного принимать файл на вход и возвращать ответ нейросети


app = FastAPI()

prompts = json_to_dict_list("prompts.json")[0]  # Загружаем промпты

prompt_list = [
    "Титульный лист",
    "список исполонителей",
    "реферат",
    "содержание",
    "термины и определения",
    "введение",
    "заключение",
    "список использованных источников",
    "оценка современного состояния проблемы",
    "основание и исходные данные для разработки темы",
    "обоснование необходимости проведения работы",
    "актуальность и новизна темы присутствуют",
    "цель и задачи исследования присутствуют",
    "выводы по результатам работы или отдельных ее этапов",
    "оценка полноты решений поставленных задач",
    "разработка рекомендаций и исходных данных по конкретному использованию результатов НИР",
    "результаты оценки технико-экономической эффективности внедрения",
    "результаты оценки научно-технического уровня выполненной НИР в сравнении с лучшими достижениями в этой области",
    "наличие всех источников литературы в тексте работы",
    "следование индексации от наименьшего к наибольшем",

]

@app.post("/file/upload-file")  # Запрос POST для получения файла
def upload_file(file: UploadFile):
    token = generate_token()
    text = "\n".join([s.text for s in docx.Document(file.file).paragraphs])  # Преобразуем docx файл в строку
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

    ans = {}

    for i in range(20):
        if check_list[i]:
            ans[prompt_list[i]] = "+"
        else:
            ans[prompt_list[i]] = "-"
    return ans

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)