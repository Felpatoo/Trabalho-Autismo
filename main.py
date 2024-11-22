def avaliar_resposta(resposta):
    return resposta.lower() in ['sim', 's']

def sistema_especialista_autismo():
    print("Bem-vindo ao Sistema Especialista: Avaliação Inicial de Traços Associados ao Autismo!")
    print("Por favor, responda as perguntas apenas com 'sim' ou 'não'.\n")

    dificuldades_comunicacao = avaliar_resposta(input("A criança ou adulto apresenta dificuldades frequentes em se comunicar verbalmente? "))
    interação_social = avaliar_resposta(input("Apresenta dificuldade em interagir socialmente, como manter contato visual ou entender expressões faciais? "))
    comportamentos_repetitivos = avaliar_resposta(input("Demonstra comportamentos repetitivos, como movimentos constantes de mãos ou organização excessiva de objetos? "))
    sensibilidade_sensorial = avaliar_resposta(input("Mostra sensibilidade extrema ou média a sons, luzes ou texturas? "))
    interesses_restritos = avaliar_resposta(input("Possui interesses mais  intensos e restritos em tópicos ou atividades específicas? "))

    if dificuldades_comunicacao and interação_social and (comportamentos_repetitivos or sensibilidade_sensorial or interesses_restritos):
        print("\nCom base nas respostas registradas, há indicativos de características associadas ao autismo.")
        print("Recomendamos buscar orientação de um profissional qualificado de saúde qualificado para uma avaliação mais precisa e detalhada.")
    else:
        print("\nCom base nas respostas, não foram identificados traços claros de autismo. Caso haja dúvidas, consulte um profissional de saúde para  informações mais precisas.")

    print("\nObrigado por utilizaro nosso sistema.")

if __name__ == "__main__":
    sistema_especialista_autismo()
