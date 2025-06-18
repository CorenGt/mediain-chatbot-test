from flask import Flask, render_template, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM, AutoModelForCausalLM

app = Flask(__name__)

# 1. Chit-chat pipeline (DialoGPT)
chatbot_tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
chatbot_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
chatbot = pipeline("text-generation", model=chatbot_model, tokenizer=chatbot_tokenizer)

# 2. Fill-mask pipeline (Bio_ClinicalBERT)
model_name1 = "emilyalsentzer/Bio_ClinicalBERT"
tokenizer1 = AutoTokenizer.from_pretrained(model_name1)
model1 = AutoModelForMaskedLM.from_pretrained(model_name1)
fill_mask = pipeline("fill-mask", model=model1, tokenizer=tokenizer1)

# 3. NER pipeline (d4data/biomedical-ner-all)
model_name2 = "d4data/biomedical-ner-all"
ner = pipeline("ner", model=model_name2, aggregation_strategy="simple")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Selamlaşma veya genel sohbet kontrolü
    greetings = ["hello", "hi", "how are you", "good morning", "good evening", "whats up", "how are you doing"]
    if any(greet in user_message.lower() for greet in greetings):
        response = chatbot(user_message, max_length=50, pad_token_id=chatbot_tokenizer.eos_token_id)[0]['generated_text']
        response += "\nIf you have any health-related questions, feel free to ask!"
        return jsonify({"response": response})

    # Tıbbi analiz (fill-mask + NER)
    user_message_clean = user_message.replace('[MASK]', '').replace('<mask>', '')
    mask_token = tokenizer1.mask_token
    prompt = f"{user_message_clean} This could be a sign of {mask_token}."
    results = fill_mask(prompt)
    top_diseases = [res['token_str'] for res in results[:3]]

    entities = ner(user_message)
    found_entities = [ent['word'] for ent in entities]

    response = (
        f"Possible related conditions: {', '.join(top_diseases)}.\n"
        f"Detected medical terms: {', '.join(found_entities) if found_entities else 'None'}.\n"
        "This is not a medical diagnosis, please consult a doctor.\n"
        "Get well soon!"
    )
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
