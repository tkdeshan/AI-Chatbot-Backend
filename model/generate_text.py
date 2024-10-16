import onnxruntime_genai as og
import os

model_path = os.path.join(os.path.dirname(__file__), './cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4')  
model = og.Model(model_path)
tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

def generate_text(text, max_length=2048):
    chat_template = '<|user|>\n{input} <|end|>\n<|assistant|>'
    prompt = f'{chat_template.format(input=text)}'
    input_tokens = tokenizer.encode(prompt)

    search_options = {'max_length': max_length}
    params = og.GeneratorParams(model)
    params.set_search_options(**search_options)
    params.input_ids = input_tokens
    generator = og.Generator(model, params)

    while not generator.is_done():
        generator.compute_logits()
        generator.generate_next_token()
        new_token = generator.get_next_tokens()[0]
        decoded_token = tokenizer_stream.decode(new_token)
        yield decoded_token  # Yield tokens one by one

    del generator  # Clean up the generator
