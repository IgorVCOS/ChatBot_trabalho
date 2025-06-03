def obter_resposta(mensagem):
    mensagem = mensagem.lower()

    marcas_celulares = ["samsung", "apple", "xiaomi", "motorola", "asus", "lg"]
    marcas_notebooks = ["dell", "asus", "lenovo", "acer", "hp", "apple"]

    tipos_notebook = {
        "gamer": "notebooks com alta performance para jogos e aplicações pesadas.",
        "ultrafino": "notebooks leves, finos e com boa autonomia de bateria.",
        "escritório": "notebooks focados em produtividade e tarefas diárias."
    }

    catalogo = {
        "celular samsung": "Samsung Galaxy S23 - R$ 4.500,00",
        "celular apple": "iPhone 14 - R$ 6.000,00",
        "notebook dell gamer": "Dell G15 Gamer - R$ 7.200,00",
        "notebook asus ultrafino": "ASUS ZenBook Ultrafino - R$ 6.800,00",
        "notebook lenovo escritório": "Lenovo IdeaPad Escritório - R$ 3.500,00"
    }

    # Saudações
    if any(p in mensagem for p in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "e aí"]):
        return "Olá! Bem-vindo à nossa loja de tecnologia. Como posso ajudar você hoje?"

    # Pedido de recomendação geral
    elif any(p in mensagem for p in ["indique", "recomende", "sugira", "produto", "algo para comprar"]):
        return "Claro! Temos notebooks, celulares, acessórios e muito mais. Qual categoria você prefere?"

    # Resposta para tipos específicos de notebook
    elif any(tipo in mensagem for tipo in tipos_notebook.keys()):
        for tipo in tipos_notebook:
            if tipo in mensagem:
                return f"Temos {tipos_notebook[tipo]} Gostaria de ver modelos ou marcas específicas?"

    # Celulares com marcas específicas
    elif any(marca in mensagem for marca in marcas_celulares):
        for marca in marcas_celulares:
            if marca in mensagem:
                return f"Ótima escolha! Temos vários modelos de {marca.capitalize()} disponíveis. Quer saber sobre algum modelo específico?"

    # Notebooks com marcas específicas (resposta detalhada)
    elif any(marca in mensagem for marca in marcas_notebooks):
        for marca in marcas_notebooks:
            if marca in mensagem:
                return (f"Trabalhamos com diversos notebooks {marca.capitalize()}, incluindo modelos gamer, "
                        "ultrafinos e para escritório. Deseja saber mais detalhes sobre algum tipo específico?")

    # Celulares gerais
    elif any(p in mensagem for p in ["celular", "telefone", "smartphone"]):
        return "Temos vários modelos de celulares disponíveis. Qual marca você prefere?"

    # Notebooks gerais
    elif any(p in mensagem for p in ["notebook", "laptop", "computador"]):
        return "Trabalhamos com notebooks gamer, ultrafinos e para escritório. Qual tipo você quer?"

    # Preços
    elif any(p in mensagem for p in ["preço", "preços", "valor", "valores", "custo", "custos"]):
        lista_precos = "\n".join([f"- {produto}: {preco}" for produto, preco in catalogo.items()])
        return f"Aqui estão alguns dos nossos produtos e preços:\n{lista_precos}"

    # Horário de funcionamento
    elif any(p in mensagem for p in ["horário", "funciona", "aberto"]):
        return "Funcionamos de segunda a sábado, das 9h às 18h."

    # Agradecimentos
    elif any(p in mensagem for p in ["obrigado", "valeu", "brigado"]):
        return "De nada! Se precisar de mais alguma coisa, é só chamar."

    # Despedida
    elif any(p in mensagem for p in ["tchau", "adeus", "encerrar", "sair"]):
        return "Até logo! Foi um prazer ajudar você."

    # Caso padrão
    else:
        return "Desculpe, não entendi. Pode reformular sua pergunta?"
