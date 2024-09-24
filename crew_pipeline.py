import sys

from crewai import Pipeline
import asyncio
import warnings
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


warnings.filterwarnings("ignore", message="Overriding of current TracerProvider is not allowed")

def send_email(file_path, sender_email, sender_password, receiver_email):
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Combined Markdown File Contents"

    msg.attach(MIMEText(content, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


def combine_markdown_files():
    captions_path = "markdown/captions.txt"
    gmage_path = "markdown/genImage.txt"
    email_path = "markdown/email_content.txt"
    combined_path = "markdown/post_result.txt"

    # Ensure the markdown directory exists
    os.makedirs("markdown", exist_ok=True)

    # Read contents of both files
    captions_content = ""
    if os.path.exists(captions_path):
        with open(captions_path, 'r', encoding='utf-8') as f:
            captions_content = f.read()

    genimage_content = ""
    if os.path.exists(gmage_path):
        with open(gmage_path, 'r' ,encoding='utf-8') as f:
            genimage_content = f.read()
    email_content = ""
    if os.path.exists(email_path):
        with open(email_path, 'r' ,encoding='utf-8') as f:
            email_content = f.read()

    # Combine contents
    combined_content = f"# Captions\n\n{captions_content}\n\n# Generated Images\n\n{genimage_content}\n\n# Email NewsLetter HTML\n\n{email_content}"

    # Write combined content to a new file
    with open(combined_path, 'w',encoding='utf-8') as f:
        f.write(combined_content)

    print(f"Combined file created at: {combined_path}")


def create_pipeline():

    from crew import Social_crew
    from imagenCrew import imageGen_crew
    return Pipeline(stages=[Social_crew, imageGen_crew])


async def start_crew(description: str, image_url: str):

    my_pipeline = create_pipeline()

    social_crew_inp = {
        'description': description,
    }

    imagegen_crew_inp = {
        'image_url': image_url,
        # Add any other inputs specific to crew2
    }

    # Pass inputs as a dictionary
    inputs = {
        'description': description,
        'image_url': image_url
    }
    result = await my_pipeline.kickoff(
        inputs=[inputs]
    )
    print(result)
    combine_markdown_files()
    combined_file_path = "markdown/post_result.txt"


    sender_email = "apollovishwas@gmail.com"
    sender_password = "xsdz femy iyks mjhx"
    receiver_email = "apollovishwas@yahoo.com"
    send_email(combined_file_path, sender_email, sender_password, receiver_email)
    return result

    pass


def run_start_crew(product_info: str, image_url: str):
    try:

        asyncio.run(start_crew(product_info, image_url))
        print("Success, the run is complete")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.exit("Finished Executing Crew")

if __name__ == '__main__':
   print("running the pipeline")