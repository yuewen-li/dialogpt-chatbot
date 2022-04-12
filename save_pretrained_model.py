from transformers import AutoModelForCausalLM, AutoTokenizer

def save_pretrained_model(model_name, model_path):
	
	tokenizer = AutoTokenizer.from_pretrained(model_name)
	model = AutoModelForCausalLM.from_pretrained(model_name)

	tokenizer.save_pretrained(model_path)
	model.save_pretrained(model_path)

if __name__ == "__main__":
	save_pretrained_model("microsoft/DialoGPT-medium", "/model/")