from typing import List, Dict
import openai


class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

    def image_generation(self, prompt: str) -> str:
        pass


class OpenAIModel(ModelInterface):

    # When using Azure OpenAI API, use following lines. Original OpenAI API are being commented below
    
    def __init__(self,
               api_key: str,
               model_engine: str,
               image_size: str = '512x512'):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.image_size = image_size
        openai.api_type = "azure"
        openai.api_base = AZURE_ENDPOINT
        openai.api_version = "2023-05-15"

  def chat_completion(self, messages) -> str:
    response = openai.ChatCompletion.create(deployment_id=AZURE_DEPLOY_NAME,
                                            model="gpt-3.5-turbo",
                                            messages=messages)
    return response

   # Following lines are original codes that use original OpenAI API
    
   # def __init__(self, api_key: str, model_engine: str, image_size: str = '512x512'):
   #     openai.api_key = api_key
   #     self.model_engine = model_engine
   #     self.image_size = image_size

   # def chat_completion(self, messages) -> str:
   #     response = openai.ChatCompletion.create(
   #         model=self.model_engine,
   #         messages=messages
   #     )
   #     return response

    def image_generation(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=self.image_size
        )
        image_url = response.data[0].url
        return image_url
