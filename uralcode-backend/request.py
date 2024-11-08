import requests
import json
import ast


def generate_token(): # Создаем токен доступа для GigaChat
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': '29813b91-07ae-483a-ad6c-286bb7b21848',
        'Authorization': 'Basic OGQ3NjY5ZGMtZDU5Zi00YTQ5LWFhYjAtMGU0ZjczYWVmZWU2OjczZGYzZWQ4LTFhYmEtNDIyNS04ZWRlLWU2ZDBlNDU3OTM1Yw=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    token = ast.literal_eval(response.text)["access_token"]
    return token


def req_to_chat(prompt, text, token):  # Запрос к GigaChat, передаем запрос к тексту, текст и токен доступа
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    # Запрос происходит в трех собщениях: вступление, текст для анализа и заранее созданные промпт
    payload = json.dumps({
      "model": "GigaChat",
      "messages": [
          {
              "role": "user",
              "content": "Сейчас тебе будет дан текст, тебе нужно будет ответить на вопросы про данный текст"
          },
          {
          "role": "user",
          "content": text
          },
          {
              "role": "user",
              "content": prompt
          }
      ],
      "stream": False,
      "repetition_penalty": 1,
      "temperature": 0.1  # температура минимальна для максимальной предсказуемости
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f"Bearer {token}"}

    response = requests.post(url, headers=headers, data=payload, verify=False)
    print(response.text)
    return ast.literal_eval(response.text)["choices"][0]["message"]["content"]  # Преобразовываем выходное сообщение в строку



