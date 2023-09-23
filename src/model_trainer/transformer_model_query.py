import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def generate_query_from_text(text_input, max_length=50, temperature=1.0):
    # Load pre-trained GPT-3.5 model and tokenizer
    model_name = "EleutherAI/gpt-neo-2.7B"  # GPT-3.5 model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Tokenize the input text
    input_ids = tokenizer.encode(text_input, return_tensors="pt")

    # Generate query using the model
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=max_length,
            # You can adjust this parameter to control the diversity of the generated queries.
            num_beams=5,
            temperature=temperature,
            early_stopping=True
        )

    # Decode the generated query
    query = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return query


# Example usage
text_input = "In the 19th century, the telephone was invented by Alexander Graham Bell."
generated_query = generate_query_from_text(text_input)
print("Generated Query:", generated_query)
