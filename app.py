import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"CodingRaja",
        "prompt":final_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=5,placeholder="Enter your Prompt"),
    outputs="text",
    title="CodingRaja Assistant 📝",
    examples=[
        ["Provide python code of Fibonacci Series."],
        ["Provide python code of Binary Search."],
    ]
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()



#theme="huggingface",