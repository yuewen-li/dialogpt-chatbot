from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class chat_bot:

    tokenizer = AutoTokenizer.from_pretrained("/model/")
    model = AutoModelForCausalLM.from_pretrained("/model/")

    def __init__(self):
        self.chat_history_ids = None

    def get_response(self, user_input):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        if self.chat_history_ids is not None:
            # append the new user input tokens to the chat history
            self.bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1)
        else:
            self.bot_input_ids = new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        self.chat_history_ids = self.model.generate(self.bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)

        output = self.tokenizer.decode(self.chat_history_ids[:, self.bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        return output
