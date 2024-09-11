import os
from openai import OpenAI
from config import Config


class Create:
    def __init__(self) -> None:
        self.__assistants = {}
        self.__config = Config()
        self.__client = OpenAI(api_key=self.__config.api_key)

    def __get_assistant_by_name(self, assistants_list, assistant_name):
        for assistant in assistants_list:
            if assistant.name == assistant_name:
                return self.__client.beta.assistants.retrieve(assistant.id)

    def __read_instruction(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Function to create an assistant
    def __create_assistant(self, name, instruction):
        return self.__client.beta.assistants.create(
            name=name,
            instructions=instruction,
            tools=[{"type": "code_interpreter"}],
            model=self.__config.llm,
            )

    def run(self):
        my_assistants = self.__client.beta.assistants.list(
            order="desc",
        )

        names = [assistant.name for assistant in my_assistants.data]

        dirname = os.path.dirname(__file__)
        instructions_folder = os.path.join(dirname, "instructions")

        if "Socratic with Hints" in names:
            self.__assistants["Socratic with Hints"] = self.__get_assistant_by_name(my_assistants.data, "Socratic with Hints")
        else:
            socratic_with_hints_instruction = self.__read_instruction(f"{instructions_folder}/socratic_with_hints.txt")
            socratic_id = self.__create_assistant("Socratic with Hints", socratic_with_hints_instruction)
            self.__assistants["Socratic with Hints"] = socratic_id
        
        if "Debug Helper" in names:
            self.__assistants["Debug Helper"] = self.__get_assistant_by_name(my_assistants.data, "Debug Helper")
        else:
            debug_helper_instruction = self.__read_instruction(f"{instructions_folder}/debug_helper.txt")
            debug_helper_id = self.__create_assistant("Debug Helper", debug_helper_instruction)
            self.__assistants["Debug Helper"] = debug_helper_id 

        if "Feedbackbot" in names:
            self.__assistants["Feedbackbot"] = self.__get_assistant_by_name(my_assistants.data, "Feedbackbot")
        else:
            feedbackbot_instruction = self.__read_instruction(f"{instructions_folder}/feedbackbot.txt")
            feedbackbot_id = self.__create_assistant("Feedbackbot", feedbackbot_instruction)
            self.__assistants["Feedbackbot"] = feedbackbot_id

        return self.__assistants
        
