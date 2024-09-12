
import requests
import streamlit as st
def send_prompt_to_mistral(prompt):
        hf_token = "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"  # Remplacez par votre clé API
        url = "https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407"
        headers = {"Authorization": f"Bearer {hf_token}"}
        data = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 500, "return_full_text": False}
        }

        response = requests.post(url, headers=headers, json=data)
        print("--------------A")
        if response.status_code == 200:
            print("--------------B")
            response_json = response.json()
            print("--------------C")
            # st.write(response_json)
            try:
                print("--------------D")
                advice = response_json[0]["generated_text"]  # Extraction du texte généré
                print("--------------E")
                # return st.write(advice)
                return advice
            except KeyError:
                return "Erreur : la réponse ne contient pas de texte généré."
        else:
            return f"Erreur lors de la requête : {response.status_code}"
        
# prompt = f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé."
# print(send_prompt_to_mistral(prompt))