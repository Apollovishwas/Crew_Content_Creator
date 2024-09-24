from crewai import Task, Crew, Agent
import os
from crewai_tools import tool
from crewai_tools import tool
import requests
import json
from datetime import datetime



os.environ["OPENAI_API_KEY"] = ""


def append_to_new_file(text: str):
    """
    Creates a new text file with the name 'genImage.txt'
    and adds the given text to it.
    """
    file_name = "genImage.txt"
    file_path = os.path.join("markdown", file_name)

    # Ensure the 'markdown' directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the text to the new file
    with open(file_path, "w") as file:
        file.write(text)

    print(f"Created new file: {file_path}")


@tool("My Simple Tool")
def gen_image(image_url: str) -> str:
    """
         creates new image based off the given one
     """

    url = "https://api.developer.pixelcut.ai/v1/generate-background"

    payload = json.dumps({
        "image_url": image_url,
        "image_transform": {
            "scale": 1,
            "x_center": 0.5,
            "y_center": 0.5
        },
        "scene": "marble",
        "prompt": "Generate the image of the product, set in outdoors, untrarealistic, Cinematic, Ultra realistic",
        "negative_prompt": "string"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-API-KEY': 'sk_257de010b1594553bbd89d7ec3ee4685'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    append_to_new_file(response.text)
    return response.text

#agent to make an api call

agent = Agent(
    role="Tool User",
    goal="Use the simple tool",
    backstory="I am an agent that uses tools",
    tools=[gen_image]
)


#agent to make an api call
task = Task(
    description="Use the simple tool to process this input {image_url}. Guidelines: Do not add anything to the output from the tool. Do not, I repeat, Do not add anything before or after the output from the string",
    expected_output = "a string",
    agent=agent
)


#Exposing crew to pipeline
imageGen_crew = Crew(
    agents=[agent],
    tasks=[task]
)

# result = imageGen_crew.kickoff( inputs={'image_url': "https://cdn.shopify.com/s/files/1/0898/7305/6090/files/81b3u88f1KL._AC_SL1500_0593c974-a1b0-4a9c-ab69-79d0944d6c7c.jpg?v=1727098843"})
#print(result)