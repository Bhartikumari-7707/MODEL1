import json

# Path to the dataset
dataset_path = r"ENTER YOUR DATA PATH"

# Load the dataset
with open(dataset_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Define the function to extract reviews
def make_prompt(pair):
    r1 = pair[0]
    r2 = pair[1]
    return f"Review 1 : {r1}\nReview 2: {r2}\n."  # Return the prompt as a string

# Iterate through each paper and process its review pairs



from groq import Groq

Api_key = 'KEY'

client = Groq(api_key=Api_key)

for paper_id, paper_values in data.items():
    Review_pairs = paper_values.get("review_pairs", [])  
    print(f"Paper ID: {paper_id}")
    
    for each_pair in Review_pairs:
        prompt = make_prompt(each_pair)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {   
                    "role": "user",
                    "content": f"""you are a contradiction detector , your job is to detect contradiction between two reviews ,you have to follow the steps below: 
                    step 1: Read the review1 and list the aspects of the review . such as clarity , motivation, originality,soundness, meaningful-comparision , substances etc.
                    step 2: Read the review2 and list the aspects of the review . such as clarity , motivation, originality,soundness, meaningful-comparision ,  substances etc. 
                    step 3: Identify and write the review portion from both the review which are contradicting to each other along with their aspect catogory .
                    step 4: Finally output those review portion in tupule formate along with their aspect catogeries : {prompt}
""",
                }
            ],
            temperature=0.5,
            max_tokens=2000,
            top_p=1
        )
        
        
        
        print(completion.choices[0].message.content)