from openai import OpenAI
# API key for OpenAI
api_key = "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"

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_summary(article_content):
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Set the prompt for generating summary
    prompt = article_content
    
    # Generate completion using OpenAI's chat completion API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",  # Specify the GPT-3 engine
        max_tokens=50,
        temperature=0.7,
        response_format={"type":"json_object"},
        messages = [
            {"role": "system", "content": "You are good at summerizing in valid JSON, where the only shown text is the summary and there is no \ or / within the max_tokens, don't show the rol='assistant' and after"},
            #Read article_content and give a summary on what its about
            {"role": "user", "content": article_content},
        ]
    )
    
    # Extract and return the generated summary from completion
    return completion.choices[0].message
