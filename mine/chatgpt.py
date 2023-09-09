import openai


# Set the API key
openai.api_key = "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"

# Define the model and prompt
model_engine = "text-davinci-003"
prompt = "写一段c语言代码"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the response text
message = completion.choices[0].text

print(message)