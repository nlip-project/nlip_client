"""
This file provides a client-side module for easing development of nlip based
clients. The file hides the implementation of the nlip protocol over the underlying
base transfer protocol. 

"""

from nlip_sdk.nlip import NLIP_Message
from nlip_sdk import errors as err 
import httpx

class NLIP_Client: 
    def send(self, msg: NLIP_Message) -> NLIP_Message:
        raise err.UnImplementedError(f"synchronous send unimplemented", self.__class__.__name__)
    
    def async_send(self, msg:NLIP_Message)-> NLIP_Message:
        raise err.UnImplementedError(f"synchronous send unimplemented", self.__class__.__name__)



class NLIP_HTTPX_Client(NLIP_Client): 
    def __init__(self, base_url: str):
        self.base_url = base_url

    #define class factory methods to get instances in various ways 

    @classmethod
    def create_from_url(cls, base_url:str):
        return NLIP_HTTPX_Client(base_url)
    
    @classmethod
    def create_from_hostport(cls, host:str, port:int):
        base_url = f"http://{host}:{port}/nlip"
        return NLIP_HTTPX_Client(base_url)

    
    def base_process_response(self, response:httpx.Response) -> NLIP_Message:
        data = response.raise_for_status().json()
        nlip_msg = NLIP_Message(**data)
        correlator = nlip_msg.extract_conversation_token()
        if correlator is not None:
            self.conversation_id = correlator 
        return nlip_msg

    def check_for_conversation(self, msg:NLIP_Message) -> NLIP_Message:
        if hasattr(self, 'conversation_id'):
            if self.conversation_id is not None: 
                correlator = msg.extract_conversation_token()
                if correlator is None: 
                    msg.add_conversation_token(self.conversation_id)
        return msg
                
        

    
    def send(self, msg:NLIP_Message) -> NLIP_Message:
        msg = self.check_for_conversation(msg) 
        with httpx.Client() as client:
            response = client.post(self.base_url, json=msg.to_dict(), timeout=120.0, follow_redirects=True)
            return self.base_process_response(response)
            

    async def async_send(self, msg:NLIP_Message) -> NLIP_Message:
        async with httpx.AsyncClient() as client:
            msg = self.check_for_conversation(msg) 
            response = await client.post(self.base_url, json=msg.to_dict(),timeout=120.0, follow_redirects=True)
            return self.base_process_response(response)