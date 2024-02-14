import json, time, os
from openai import OpenAI
from config.config import Prompts, Path_
from utils.utilities import ShowJson

class AI:

    def __init__(me, job_desc, hw_client):
        global client
        client = hw_client
        me.job_desc = job_desc
        # me.job_desc = job_desc[:20]         # temporary, delete soon
        print(f"job_desc--- {me.job_desc}")

    def ai(me):
        assistant_id = me.create_1_assistant()       
        print(f"ass id--- {assistant_id}")

        thread_id    = me.create_2_thread()
        print(f"thread id--- {thread_id}")

        thread_msg   = me.create_3_thread_msg(thread_id, me.job_desc)
        print(f"thread msg --- {thread_msg}")

        cover_letter = me.create_4_run(assistant_id, thread_id)

        print(f"cl --- {cover_letter}")
        return (cover_letter)

    def create_1_assistant(me):
        assistant_file_path = Path_.config_file('assistant.json')

        # If there is an assistant.json file already, then load that assistant
        if assistant_file_path.exists():
            with open(assistant_file_path, 'r') as file:
                assistant_data = json.load(file)
                assistant_id = assistant_data['assistant_id']
                print(f"Loaded existing assistant ID:  {assistant_id}")
        else:
            file = client.files.create(file=open("./src/aiCL/data/MyFile.pdf", "rb"),purpose='assistants')  # uploading

            assistant = client.beta.assistants.create(
                name="aiCL",
                instructions = Prompts.assistant_instructions(),
                model="gpt-3.5-turbo-1106",     
                tools=[{"type": "retrieval"},],
                file_ids=[file.id])

            # Create a new assistant.json file to load on future runs
            with open(assistant_file_path, 'w') as file:
                json.dump({'assistant_id': assistant.id}, file)
                print("Created a new assistant and saved the ID.")

            assistant_id = assistant.id
            ShowJson.show_json(assistant)
            #Assistant(id='asst_iiM1BFfVhkRzcNKJWIUnEwcV', created_at=1706244748, description=None, file_ids=['file-Rn5vX1ipMgOVjl18xdUg0B69'], 
            # instructions="The assistant will play the role of a job seeker. Based on the uploaded PDF resume and the job description, 
            #       write a polite and professional job application message or cover letter to HR. Use professional language, integrate experiences 
            #       and skills from the resume, and highlight strengths in relation to the job. Please start with the recruiter's name and end sincerely 
            #       with resume's name This is a complete job application letter; exclude any content beyond it for easy automation.", 
            # metadata={}, model='gpt-3.5-turbo-1106', name='aiCL', object='assistant', tools=[ToolRetrieval(type='retrieval')])
        return assistant_id

    def create_2_thread(me):
        # Function to create a new thread and return its ID
        try:
            thread    = client.beta.threads.create()  # No assistant_id needed
            thread_id = thread.id
            ShowJson.show_json(thread)
            return thread_id                #{'id': 'thread_6IbmulcAob6MmD63WDkWXaVh', 'created_at': 1706326405, 'metadata': {}, 'object': 'thread'}
        except Exception as e:
            print(f"Error creating thread: {e}")
            return None
        
    def create_3_thread_msg(me,thread_id, user_input):

        # Run the Assistant
        try:
            # Add the user's message to the thread
            thread_msg = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_input
            )
            ShowJson.show_json(thread_msg)                                              
            # {'id': 'msg_7GdH0LXJbB6MGAVV6fSfUJxU', 'assistant_id': None, 'content': [{'text': {'annotations': [], 
            # 'value': 'At Haiper, we are on a mission to redefine the landscape of Perceptual Foundation Models.'}, 'type': 'text'}], 
            # 'created_at': 1706326567, 'file_ids': [], 'metadata': {}, 'object': 'thread.message', 'role': 'user', 'run_id': None, 'thread_id': 'thread_pgwNLHHLrzHOPGJGVHhR5tB0'}
            return thread_msg

        except Exception as e:
            print(f"An error occurred: {e}")
            error_response = json.dumps({"error": str(e)})
            return error_response

    def create_4_run(me, assistant_id, thread_id):
        # Run the Assistant
        try:

            # Start the Assistant Run
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id)
            ShowJson.show_json(run)

            # Check if the Run requires action (function call)
            while True:
                run_status = client.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=run.id
                )

                if run_status.status == 'completed':
                    break
                elif run_status.status == 'requires_action':
                    # Here you can handle specific actions if your assistant requires them
                    time.sleep(1)  # Wait for a second before checking again

            # Retrieve and return the latest message from the assistant
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            assistant_message = messages.data[0].content[0].text.value

            # response_data = json.dumps({"response": assistant_message, "thread_id": thread_id})
            return assistant_message

        except Exception as e:
            print(f"An error occurred: {e}")
            error_response = json.dumps({"error": str(e)})
            return error_response
