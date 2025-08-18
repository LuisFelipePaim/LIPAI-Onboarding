
class Projeto:
    

    def __init__(self, codigo: int, titulo: str, responsavel: str):
        
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, dados_projeto: str):
        
        if not dados_projeto or not isinstance(dados_projeto, str):
            raise ValueError("A string de dados não pode ser nula ou vazia.")

        try:
            codigo_str, titulo, responsavel = dados_projeto.split(',')
            codigo = int(codigo_str.strip())
            return cls(codigo, titulo.strip(), responsavel.strip())
        except ValueError:
            raise ValueError("Formato da string inválido ou código não é um número. Use 'codigo,titulo,responsavel'.")

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

    def __eq__(self, outro) -> bool:
        
        if not isinstance(outro, Projeto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __repr__(self) -> str:
       
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', responsavel='{self.responsavel}')"


if __name__ == "__main__":
    projeto1_str = "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
    projeto1 = Projeto.from_string(projeto1_str)
    print(f"Projeto 1 criado a partir da string: {projeto1}")

    projeto2 = Projeto(2, "Pesquisa em Inteligência Artificial", "Ana Clara")
    print(f"Projeto 2 criado com o construtor: {projeto2}")

    projeto3 = Projeto(1, "Lab de Dev de Software", "Pedro Gomes da Silva")
    print(f"Projeto 3 criado com o mesmo código do Projeto 1: {projeto3}")
    
    print(f"\nProjeto 1 é igual ao Projeto 2? {projeto1 == projeto2}")
    print(f"Projeto 1 é igual ao Projeto 3? {projeto1 == projeto3}")

    try:
        projeto_invalido = Projeto(3, "", "Responsável Válido")
    except ValueError as e:
        print(f"\nErro ao criar projeto inválido: {e}")