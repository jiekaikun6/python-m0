# utils.py
# 作用：存可以复用的工具函数。
# 规矩：模块顶层只定义，不执行动作；测试代码放 __main__ 守卫里。
def build_messages(user_input:str,system:str="")->list:
    """把用户输入拼成 DeepSeek / OpenAI 格式的 messages 列表。

    参数：
        user_input: 用户这一轮说的话
        system:     系统提示词；为空字符串时不添加 system 消息

    返回：
        一个新的列表，例如：
        [{"role": "system", "content": "..."},
         {"role": "user",   "content": "..."}]
    """
    messages=[]
    if system:  #等于if system!=""
        messages.append({"role":"system","content":system})

    messages.append({"role":"user","content":user_input})
    return messages


if __name__=="__main__":
    print(build_messages("你好"))
    print(build_messages("你好",system="你是一个财务助手"))


