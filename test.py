llm_model_dict = {
    # "llama-2-7b": "LinkSoul/Chinese-Llama-2-7b-4bit",
    "qwen7b": "Qwen/Qwen-7B-Chat",
    "qwen7b4": "Qwen/Qwen-7B-Chat-Int4",
    # "baichuan-13b-chat": "baichuan-inc/Baichuan-13B-Chat",
    # "chatglm-6b-int4-qe": "THUDM/chatglm-6b-int4-qe",
    # "chatglm-2-6b": "THUDM/chatglm2-6b",
    # "chatglm-2-6b-int4": "THUDM/chatglm2-6b-int4",
    # "chatglm-6b-int4": "THUDM/chatglm-6b-int4",
    # "chatglm-6b": "THUDM/chatglm-6b",
    # "llama-7b": "shibing624/chinese-alpaca-plus-7b-hf",
    # "llama-13b": "shibing624/chinese-alpaca-plus-13b-hf",
}
DEFAULT_GEN_TYPE = 'qwen7b4'
DEFAULT_GEN = 'Qwen/Qwen-7B-Chat-Int4'
import time

print(llm_model_dict.get('qwen7b4'))
time.sleep(191)
