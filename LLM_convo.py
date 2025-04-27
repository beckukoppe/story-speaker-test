class LLM:
    def __init__(self, server_url, start_prompt):
        self.server_url = server_url
        self._messages = []
        self._system(start_prompt)

    #"calls" LLM with message and returns response
    def call(self, message):
        self._user(message)
        response = self._send(self._messages)
        self._system(response)
        return response

    def getLastInteraction(self):
        if len(self._messages) >= 2:
            return self._messages[-2:]  # return last two elements
        else:
            print("Error: <getLastInteraction> no interactions yet")
            return []  # no messages yet

    def _system(self, content):
        self._messages.append({"role": "system", "content": content})

    def _user(self, content):
        self._messages.append({"role": "user", "content": content})

    #send request (with history) to LLM-server and return response
    def _send(self, messages):
        try:
            response = requests.post(self.server_url, json={
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