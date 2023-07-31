import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a AI experts that specializes in AI application development"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI Solution Pro")

demo.launch(share=True)