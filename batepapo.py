    import random
    
    estado = ("em trânsito", "cancelado", "pedido não encontrado") 
    estado1 = random.choice(estado)
    
    def bot_de_conversa():
        while True:
            print("--------------------------------------------------------------")
            print("Bom dia, com o que posso te ajudar?")
            print("1. Problema com o produto")
            print("2. Alterar dados")
            print("3. Cancelar pedido")
            print("4. Atendimento ao cliente")
            print("Escolha uma opção (ou digite '5' para cancelar):")
            resposta = input("--------------------------------------------------------------")
    
            if resposta == '1':
                print("--------------------------------------------------------------")
                print("Qual seria o problema?") 
                print("1. Produto danificado") 
                print("2. Produto chegou errado") 
                print("3. Não recebi o produto")
                print("4. voltar")
                print("Escolha uma opção (ou digite '5' para cancelar):")
                resposta1 = input("--------------------------------------------------------------")
                
                if resposta1 == '3':
                    print("--------------------------------------------------------------")
                    print("Entendemos. Qual opção abaixo deseja?")
                    print("1. Reembolso")
                    respostadefeito = input("2. esperar e voltar\nEscolha uma opção: ")
                    if respostadefeito == '1':
                        print("--------------------------------------------------------------")
                        print("ok")
                        numeropedido = input("Qual o numero do seu pedido?")
                        print("tudo bem, solicitamos o reembolso do pedido numero", numeropedido)
                        print("para mais informações reinicie o atendimento")
                        print("--------------------------------------------------------------")
                    elif respostadefeito == '2':
                        bot_de_conversa()
                    else:
                        print("você escolheu um numero invalido, digite novamente.")
                    
                if resposta1 in ['1', '2']:
                    print("--------------------------------------------------------------")
                    print("Entendemos. Qual opção abaixo deseja?")
                    print("1. Reembolso")
                    respostadefeito = input("2. Troca\nEscolha uma opção: ")
    
                    if respostadefeito == '1':
                        print("OK")
                        pedido = input("Qual é o número do seu pedido? ")
                        print("--------------------------------------------------------------")
                        print("Tudo bem, solicitamos o reembolso do pedido número:", pedido)
                        print("--------------------------------------------------------------")
                        print("deseja voltar ao inicio ou encerrar o atendimento aqui?")
                        print("1. voltar ao inicio")
                        continuar = input("2. Encerrar aqui")
                        if continuar == '1':
                            bot_de_conversa()
                        elif continuar == '2':
                            exit()
                    elif respostadefeito == '2':
                        print("OK")
                        pedido = input("Qual é o número do seu pedido? ")
                        print("--------------------------------------------------------------")
                        print("Tudo bem, solicitamos a troca do pedido número:", pedido)
                        print("--------------------------------------------------------------")
                        print("deseja voltar ao inicio ou encerrar o atendimento aqui?")
                        print("1. voltar ao inicio")
                        continuar = input("2. Encerrar aqui")
                        if continuar == '1':
                            bot_de_conversa()
                        elif continuar == '2':
                            exit()
    
            elif resposta == '2': 
                print("--------------------------------------------------------------")
                print("Qual dos seguintes dados deseja alterar?") 
                print("1. Endereço") 
                print("2. Telefone") 
                print("3. Email") 
                print("Escolha uma opção (ou digite '5' para cancelar):")
                resposta2 = input("--------------------------------------------------------------")
    
                if resposta2 in ['1', '2', '3']:
                    if resposta2 == '1':
                        endereco = input("Insira o novo endereço: ")
                        print("Seu novo endereço é", endereco)
                    elif resposta2 == '2':
                        telefone = input("Insira o novo telefone: ")
                        print("Seu novo número de telefone é", telefone)
                    elif resposta2 == '3':
                        email = input("Insira o novo email: ")
                        print("Seu novo email é", email)
                elif resposta2 == '4':
                    print("Operação cancelada.")
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
    
            elif resposta == '3':
                resposta103 = input("Qual seria o número do seu pedido? ")
                print("--------------------------------------------------------------")
                print("Seu pedido de número", resposta103, "foi cancelado.")
                print("deseja voltar ao inicio ou encerrar o atendimento aqui?")
                print("1. voltar ao inicio")
                continuar1 = input("2. Encerrar aqui")
                if continuar1 == '1':
                    bot_de_conversa()
                elif continuar1 == '2':
                    exit()
    
            elif resposta == '4':
                print("--------------------------------------------------------------")
                print("Você escolheu atendimento ao cliente") 
                print("1. Email") 
                resposta104 = input("2. WhatsApp\nEscolha uma opção: ")
                
                if resposta104 in ['1', '2']:
                    if resposta104 == '1':
                        print("--------------------------------------------------------------")
                        respostaemail = input("Insira seu email: ")
                        print("Dentro de aproximadamente 24 horas, nosso time entrará em contato com você através do email", respostaemail)
                        print("Para outras opções, inicie o atendimento novamente.")
                        print("--------------------------------------------------------------")
                        exit()
                    elif resposta104 == '2':
                        respostanum = input("Insira seu número: ")
                        print("Dentro de aproximadamente 24 horas, nosso time entrará em contato com você através do número", respostanum)
                        print("Para outras opções, inicie o atendimento novamente.")
                        print("--------------------------------------------------------------")
                        exit()
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
    
            elif resposta == '5':
                print("Atendimento cancelado.")
                exit()
    
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    
    bot_de_conversa()
