import re
import requests

class LLM:
    def __init__(self, server_url, start_prompt, allowed_commands):
        self._server_url = server_url
        self._messages = []
        self._system(start_prompt)
        self._allowed_commands = allowed_commands

    #"calls" LLM with message and returns response
    def call(self, message):
        self._user(message)
        response = self._send(self._messages)
        self._system(response)
        print(response)
        return parseCommand(response, self._allowed_commands)

    def getSumUp(self):
        return self.call("#SUMUP")

    def _system(self, content):
        self._messages.append({"role": "system", "content": content})

    def _user(self, content):
        self._messages.append({"role": "user", "content": content})

    #send request (with history) to LLM-server and return response
    def _send(self, messages):
        try:
            response = requests.post(self._server_url, json={
                #"model": MODEL_NAME,
                "messages": self._messages,
                "temperature": 0.7
            }, headers={"Content-Type": "application/json"})

            reply = response.json()["choices"][0]["message"]["content"].strip()

            clean_reply = reply.replace("\n", " ").replace("\r", "")
            return clean_reply
            
        except Exception as e:
            print(f"LLM-Server-Error: {e}")
            return None



def parseCommand(text, allowed_commands):
    """
    Parse commands of the form:
    - #COMMAND{data}
    - #COMMAND
    - #COMMAND(param)
    
    Args:
        text (str): The input text containing commands.
        allowed_commands (list of str): List of allowed command names.

    Returns:
        tuple: (success: bool, results: list of dict)
    """

    # Erlaubte Kommandos absichern
    command_pattern = '|'.join(re.escape(cmd) for cmd in allowed_commands)
    
    # Regex: fängt COMMAND, optional {data} oder (param)
    pattern = rf'#({command_pattern})(?:\{{([^}}]*)\}}|\(([^)]*)\))?'

    matches = list(re.finditer(pattern, text))

    if not matches:
        return False, []


    results = []
    for match in matches:
        command, data, param = match.groups()
        result = {'command': command}
        
        if data is not None:
            result['data'] = data
        elif param is not None:
            result['param'] = param
        
        results.append(result)
    
    return True, results




