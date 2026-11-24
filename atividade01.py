contatos = []

for i in range(3):
    print(f"\n--- Cadastro do {i + 1}º contato ---")
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)

print("\n=== CONTATOS CADASTRADOS ===")
for i, contato in enumerate(contatos, start=1):
    print(f"\nContato {i}:")
    print(f"Nome:     {contato['nome']}")
    print(f"Telefone: {contato['telefone']}")
    print(f"E-mail:   {contato['email']}")