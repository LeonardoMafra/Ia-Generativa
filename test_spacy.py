import spacy

#CARREGAR MODELO EM PORTUGUES
nlp = spacy.load("pt_core_news_sm")


#texto de exemplo

texto =""" O Leonardo trabalha como Tecnico Eletromecanico em Vinhedo"""


doc = nlp(texto)

# xibe tokens, lemas, e classes gramaticais

for token in doc:
    print(f"Texto: {token.text}")
    print(f"Lema: {token.lemma_}")
    print(f"Classe Gramatical: {token.pos_}")
    print("-" * 30)

    #exibe as entidades nominais

print("\nEntidades Encontradas:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")