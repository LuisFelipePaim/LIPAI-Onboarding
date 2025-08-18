
from ex01 import Aluno
from ex03 import Participacao
from typing import List

class Projeto:
  

    def __init__(self, codigo: int, titulo: str, responsavel: str):
        
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self._participacoes: List[Participacao] = []

    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O código deve ser um número inteiro positivo.")
        self._codigo = valor

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O título не pode ser nulo ou vazio.")
        self._titulo = valor

    @property
    def responsavel(self) -> str:
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O responsável не pode ser nulo ou vazio.")
        self._responsavel = valor
        
    @property
    def participacoes(self) -> List[Participacao]:
       
        return self._participacoes[:]

    def add_participacao(self, participacao: Participacao):
        
        if not isinstance(participacao, Participacao):
            raise TypeError("O parâmetro deve ser um objeto da classe Participacao.")
        
        if participacao.projeto != self:
             raise ValueError("A participação não pertence a este projeto.")
        
        self._participacoes.append(participacao)
        print(f"Participação de '{participacao.aluno.nome}' adicionada ao projeto '{self.titulo}'.")


    def __eq__(self, outro) -> bool:
        
        if not isinstance(outro, Projeto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __repr__(self) -> str:
        
        return (f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', "
                f"responsavel='{self.responsavel}', participacoes={len(self._participacoes)})")

if __name__ == "__main__":
    aluno_a = Aluno("SP9876", "Fernanda Costa", "fe@email.com")
    aluno_b = Aluno("SP5432", "Lucas Martins", "lucas@email.com")

    projeto_ml = Projeto(202, "Machine Learning no Agronegócio", "Profa. Renata")
    print(f"\nProjeto criado: {projeto_ml}")

    part1 = Participacao("01/03/2024", "28/02/2025", aluno_a, projeto_ml)
    part2 = Participacao("15/03/2024", "14/03/2025", aluno_b, projeto_ml)
    
    projeto_ml.add_participacao(part1)
    projeto_ml.add_participacao(part2)

    print(f"\nLista de participações no projeto '{projeto_ml.titulo}':")
    for p in projeto_ml.participacoes:
        print(f"- {p}")
        
    try:
        projeto_ml.add_participacao("participacao invalida")
    except TypeError as e:
        print(f"\nErro ao adicionar participação inválida: {e}")

    outro_projeto = Projeto(999, "Outro Projeto", "Outro Prof")
    part_outro_proj = Participacao("01/01/2024", "31/12/2024", aluno_a, outro_projeto)
    try:
        projeto_ml.add_participacao(part_outro_proj)
    except ValueError as e:
        print(f"\nErro ao adicionar participação de outro projeto: {e}")