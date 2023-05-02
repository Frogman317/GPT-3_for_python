# GPT-3のライブラリ
import openai

# APIキー入力 osモジュールを使いwindows環境変数から入力
# APIキーはここから https://platform.openai.com/account/api-keys
import os
GPT_API_KEY = os.getenv('GPT-3_API_KEY')
openai.api_key = GPT_API_KEY

# これがメインプログラム
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo", # GPTのVersionみたいなもの
    messages = [ # GPTへの入力はList型の中に辞書型で行う
        { "role":"system" , "content":"You are a helpful assistant." }, # systemはどのような返答を希望するかをcontentに記述します。
        { "role":"user" , "content":"What is the company behind Genshin Impact?" }, # userはGPTに聞きたい内容を記述します。
        { "role":"assistant" , "content":"The company behind Genshin Impact is miHoYo." }, # assistantはGPTからの返答を書きます初めての質問はもちろんないので2回目から記述します。
        { "role":"user" , "content":"When was this game released?" } # GPTは前述された内容を考慮します。
    ]
)

print(response)

# 下記はこのプログラムの実行結果です
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Genshin Impact was released on September 28, 2020.", # ここが返答
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1683038111,
#   "id": "chatcmpl-7BlNvGCm3CfUbdaP53F19zSWpQVBs",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 15,
#     "prompt_tokens": 57,
#     "total_tokens": 72 # このプログラムの実行で使ったトークンの合計
#   }
# }