
class Aluno:
    

    def __init__(self, prontuario: str, nome: str, email: str):
       
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados_aluno: str):
       
        if not dados_aluno or not isinstance(dados_aluno, str):
            raise ValueError("A string de dados não pode ser nula ou vazia.")
        
        try:
            prontuario, nome, email = dados_aluno.split(',')
            return cls(prontuario.strip(), nome.strip(), email.strip())
        except ValueError:
            raise ValueError("Formato da string inválido. Use 'prontuario,nome,email'.")

    @property
    def prontuario(self) -> str:
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O prontuário não pode ser nulo ou vazio.")
        self._prontuario = valor

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O nome не pode ser nulo ou vazio.")
        self._nome = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O e-mail не pode ser nulo ou vazio.")
        self._email = valor

    def __eq__(self, outro) -> bool:
       
        if not isinstance(outro, Aluno):
            return NotImplemented
        return self.prontuario == outro.prontuario

    def __repr__(self) -> str:
        
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"

if __name__ == "__main__":
    aluno1_str = "SP0101,João da Silva,joao@email.com"
    aluno1 = Aluno.from_string(aluno1_str)
    print(f"Aluno 1 criado a partir da string: {aluno1}")

    aluno2 = Aluno("SP0102", "Maria Oliveira", "maria@email.com")
    print(f"Aluno 2 criado com o construtor: {aluno2}")

    aluno3 = Aluno("SP0101", "João da Silva Sauro", "joao.sauro@email.com")
    print(f"Aluno 3 criado com o mesmo prontuário do Aluno 1: {aluno3}")
    
    print(f"\nAluno 1 é igual ao Aluno 2? {aluno1 == aluno2}")
    print(f"Aluno 1 é igual ao Aluno 3? {aluno1 == aluno3}")

    try:
        aluno_invalido = Aluno("", "Nome Válido", "email@valido.com")
    except ValueError as e:
        print(f"\nErro ao criar aluno inválido: {e}")