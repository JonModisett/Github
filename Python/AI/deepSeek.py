#DeepSeek

#Packages
import csv
from openai import OpenAI

class deepseek_chat:
#Intro Message
    print("####################################\nDeepSeek CLI:\n\tCurrently only chat is support (type 'exit' to quit)\n####################################")
    
    def __init__(self, key_file='ak.csv'): #this is the file that contains the api keys
        self.api_key = self._load_api_key(key_file)
        OpenAI.api_key = self.api_key

    #Pulling api key from csv
    def _load_api_key(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'deepseek_key':
                    print(row[1][0:])
                    return row[1][0:]
        raise ValueError ("API key not found in the CSV file.")

    #Pushing the Users Question(s)
    def deepseek_ask(self, question):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a masterful philosopher"},
                {"role": "user", "content": question},
                ],
            stream=False
            )
        answer = response.choices[0].message.content
        return answer
    
# Example usage
if __name__ == "__main__":
    chat = deepseek_chat()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat.deepseek_ask(user_input)
        print("DeepSeek:", reply)


''' client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
'''
