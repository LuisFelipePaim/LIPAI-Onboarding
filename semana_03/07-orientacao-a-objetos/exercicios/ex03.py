# src/07-orientacao-a-objetos/exercicios/ex03.py

from ex01 import Aluno
from ex02 import Projeto

class Participacao:
    

    _contador_codigo = 0

    def __init__(self, data_inicio: str, data_fim: str, aluno: Aluno, projeto: Projeto):
        
        if not isinstance(aluno, Aluno):
            raise TypeError("O atributo 'aluno' deve ser uma instância da classe Aluno.")
        if not isinstance(projeto, Projeto):
            raise TypeError("O atributo 'projeto' deve ser uma instância da classe Projeto.")

        Participacao._contador_codigo += 1
        self.codigo = Participacao._contador_codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    def __repr__(self) -> str:
       
        return (f"Participacao(codigo={self.codigo}, "
                f"data_inicio='{self.data_inicio}', data_fim='{self.data_fim}', "
                f"aluno='{self.aluno.nome}', projeto='{self.projeto.titulo}')")


if __name__ == "__main__":
    aluno_ex = Aluno("SP1234", "Carlos Souza", "carlos@email.com")
    projeto_ex = Projeto(101, "Robótica Aplicada", "Prof. Eliana")

    participacao1 = Participacao("01/08/2024", "01/12/2024", aluno_ex, projeto_ex)
    print(f"Participação 1 criada: {participacao1}")

    aluno2_ex = Aluno("SP5678", "Beatriz Lima", "bia@email.com")
    participacao2 = Participacao("15/08/2024", "15/12/2024", aluno2_ex, projeto_ex)
    print(f"Participação 2 criada: {participacao2}")

    try:
        participacao_invalida = Participacao("01/01/2024", "31/12/2024", "Não é um aluno", projeto_ex)
    except TypeError as e:
        print(f"\nErro ao criar participação inválida: {e}")