import openai

openai.api_key = "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"

engine = "text-davinci-003"


async def asc_to_gpt(prompt: str):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": 'user', "content": prompt}
        ])
    return response['choices'][0]['message']['content']
