import openai
from scraper import scrape_website

# Set up your OpenAI API key
openai.api_key = "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"

def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    # Step 1: Scrape the website
    url = input("Enter the website URL: ")
    website_content = scrape_website(url)
    if "Error" in website_content:
        print(website_content)
        return

    print("Website content scraped successfully.\n")

    # Step 2: Chatbot interaction
    print("You can now ask questions about the website content.\n")
    while True:
        user_input = input("Your question (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Combine user input with scraped content
        prompt = f"The following is content from a website:\n\n{website_content}\n\nUser's question: {user_input}"
        response = ask_chatgpt(prompt)
        print(f"ChatGPT: {response}\n")

if __name__ == "__main__":
    main()
