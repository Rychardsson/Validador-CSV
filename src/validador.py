# src/validador.py

import pandas as pd
from email_validator import validate_email, EmailNotValidError

class ValidadorClientes:
    """
    Classe para validar um DataFrame de clientes importado de um CSV.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.erros = []
        self.colunas_obrigatorias = ['id', 'nome', 'email', 'data_nascimento']

    def validar(self) -> bool:
        """
        Executa todas as validações e retorna True se os dados são válidos.
        """
        self.erros = [] # Limpa erros de validações anteriores

        self._validar_colunas_obrigatorias()
        self._validar_tipos_de_dados()
        self._validar_unicidade_id()
        self._validar_formato_email()

        return len(self.erros) == 0

    def _validar_colunas_obrigatorias(self):
        """Verifica se todas as colunas obrigatórias estão presentes."""
        colunas_faltando = set(self.colunas_obrigatorias) - set(self.df.columns)
        if colunas_faltando:
            self.erros.append(f"Colunas obrigatórias ausentes: {list(colunas_faltando)}")

    def _validar_tipos_de_dados(self):
        """Valida o tipo de dados das colunas, especialmente datas."""
        if 'data_nascimento' in self.df.columns:
            # Tenta converter para datetime. Erros viram NaT (Not a Time).
            datas_convertidas = pd.to_datetime(self.df['data_nascimento'], errors='coerce')
            # Verifica quais linhas falharam na conversão (são NaT)
            linhas_com_erro = self.df[datas_convertidas.isna()]
            for index in linhas_com_erro.index:
                valor_original = self.df.loc[index, 'data_nascimento']
                self.erros.append(
                    f"Linha {index + 2}: Formato de data inválido para '{valor_original}' na coluna 'data_nascimento'."
                )

    def _validar_unicidade_id(self):
        """Garante que não há IDs de clientes duplicados."""
        if 'id' in self.df.columns:
            duplicados = self.df[self.df.duplicated(subset=['id'], keep=False)]
            if not duplicados.empty:
                ids_duplicados = duplicados['id'].unique().tolist()
                self.erros.append(f"IDs duplicados encontrados: {ids_duplicados}")

    def _validar_formato_email(self):
        """Verifica se os e-mails estão em um formato válido."""
        if 'email' in self.df.columns:
            for index, row in self.df.iterrows():
                email = row['email']
                try:
                    # A biblioteca valida o formato e a existência do domínio (se possível)
                    validate_email(email)
                except EmailNotValidError as e:
                    # Adiciona uma mensagem de erro clara
                    self.erros.append(f"Linha {index + 2}: E-mail inválido: '{email}'. Motivo: {e}")

# Função auxiliar para carregar o CSV e instanciar o validador
def validar_csv(caminho_arquivo: str) -> ValidadorClientes:
    """Carrega um arquivo CSV e retorna uma instância do validador."""
    try:
        df = pd.read_csv(caminho_arquivo)
        validador = ValidadorClientes(df)
        return validador
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'")
        return None