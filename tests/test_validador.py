# tests/test_validador.py

import pytest
import pandas as pd
from src.validador import ValidadorClientes

@pytest.fixture(scope="module")
def df_validos() -> pd.DataFrame:
    """Fixture que carrega os dados válidos uma vez por sessão de teste."""
    return pd.read_csv("data/clientes_validos.csv")

@pytest.fixture
def df_invalidos() -> pd.DataFrame:
    """Fixture que carrega os dados inválidos para cada teste."""
    return pd.read_csv("data/clientes_invalidos.csv")

def test_validacao_com_dados_validos(df_validos):
    """
    Testa o cenário feliz: o validador deve retornar True e a lista de erros deve estar vazia.
    """
    validador = ValidadorClientes(df_validos)
    assert validador.validar() is True
    assert len(validador.erros) == 0

def test_falha_por_coluna_obrigatoria_ausente(df_invalidos):
    """
    Testa se o validador identifica a ausência de colunas obrigatórias.
    No nosso arquivo inválido, a coluna 'cidade' não é obrigatória, mas podemos
    simular a falta de 'data_nascimento' para este teste.
    """
    df_sem_data = df_invalidos.drop(columns=['data_nascimento'])
    validador = ValidadorClientes(df_sem_data)
    
    assert validador.validar() is False
    # Verifica se a mensagem de erro específica está presente na lista de erros
    assert any("Colunas obrigatórias ausentes" in erro for erro in validador.erros)

def test_falha_por_id_duplicado(df_invalidos):
    """Testa se o validador detecta IDs duplicados."""
    validador = ValidadorClientes(df_invalidos)
    validador.validar() # Executa a validação para popular os erros
    assert any("IDs duplicados encontrados: [2]" in erro for erro in validador.erros)

def test_falha_por_email_invalido(df_invalidos):
    """Testa se o validador detecta e-mails com formato incorreto."""
    validador = ValidadorClientes(df_invalidos)
    validador.validar()
    assert any("E-mail inválido: 'diego.martins@'" in erro for erro in validador.erros)

def test_falha_por_data_nascimento_invalida(df_invalidos):
    """Testa se o validador detecta datas em formato inválido."""
    validador = ValidadorClientes(df_invalidos)
    validador.validar()
    assert any("Formato de data inválido para '25-03-1998'" in erro for erro in validador.erros)

def test_validacao_completa_arquivo_invalido(df_invalidos):
    """
    Testa se o validador acumula todos os erros corretamente do arquivo inválido.
    """
    validador = ValidadorClientes(df_invalidos)
    assert validador.validar() is False
    
    assert len(validador.erros) == 3