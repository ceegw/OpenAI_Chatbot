from openai import OpenAI
client = OpenAI(api_key="******")


response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    # Write your prompt
    prompt=input(" "), 
    max_tokens=300,
    
)

print(response.choices[0].text)
