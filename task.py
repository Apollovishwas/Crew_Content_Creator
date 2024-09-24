from crewai import Task
from agents import Trend_researcher, Hashtag_Specialist, Caption_Generator, Email_Content_Generator
from tools import research_tool


## Research Task
research_task = Task(
    description='Search for top fashion trends in 2024',
    expected_output='3 sentence list  of the top 3 fashion trends in 2024',
    agent=Trend_researcher,
    tools=[research_tool]
)



#generate Trends and hashtags
summarize_and_hashtag_task = Task(
    description="""
    Take the top fashion trends for 2024 provided by the Trend Researcher, 
    summarize them concisely, and generate potential hashtags for each trend.
    Use the OpenAI tool to process the input and generate creative hashtags.
    """,
    expected_output="""
    A concise summary of the top 2(not more than that) fashion trends for 2024 within 20 words at most, followed by 
    2-3 potential hashtags for each trend.
    """,
    agent=Hashtag_Specialist
)


#generate captions
caption_task = Task(
    description="""
    Generate Instagram (max 250 characters) and Twitter (max 200 characters) 
    captions for a fashion product.

    Use the trending topics and hashtags provided by the previous task as input.

    The product description : {description}.

    Guidelines:
    1. Craft engaging captions that highlight the product while incorporating 
       relevant trending topics and hashtags from the input.
    2. It's not necessary to include all trending topics, only use them if they fit naturally.
    3. Prioritize using trending hashtags when appropriate. 
    4. Ensure the Instagram caption is no more than 250 characters and the 
       Twitter caption is no more than 200 characters. use emojis.
    5. The captions should be distinct for each platform while maintaining 
       a consistent brand voice.
    6.Save the generated captions to a file named 'captions.md' in Markdown format.
    
    The Markdown file should have the following structure:
     Captions for Social Media

     Instagram Caption
    [Your Instagram caption here]

     Twitter Caption
    [Your Twitter caption here]

 After generating the captions and saving them to 'captions.txt', return a confirmation message. 
    """,
expected_output="""
      A confirmation message stating that the captions have been generated and saved to 'captions.txt'
    """,
output_file="markdown/captions.txt",

    agent=Caption_Generator
)



email_newsletter_task = Task(
    description="""
    Generate HTML content for an email newsletter using the fashion trend research and product details.
    Use the trending topics provided by the Trend Researcher as input and incorporate the product information.

    Guidelines:
    1. Create an engaging HTML email newsletter that highlights the top fashion trends for 2024.
    2. Include a brief introduction that ties the trends to the product being promoted.
    3. For each major trend, explain how the product aligns with or complements the trend.
    4. Use appropriate HTML tags for structure (headings, paragraphs, lists).
    5. Include product details such as key features, benefits, and how it fits with current fashion trends.
    6. Add a compelling call-to-action (CTA) encouraging readers to purchase the product.
    7. Include a special offer or discount code to incentivize immediate action.
    8. Keep the content concise yet informative, suitable for an email format (aim for 300-400 words).
    9. Use persuasive language that emphasizes the value and trendiness of the product.
    10. Save the generated HTML content to a file named 'email_content.txt'.

    Product Description: {description}

    After generating the email content and saving it to 'email_content.txt', return a confirmation message.
    """,
    expected_output="""
    A confirmation message stating that the email newsletter content has been generated and saved to 'email_content.txt'
    """,
    output_file="markdown/email_content.txt",
    agent=Email_Content_Generator
)