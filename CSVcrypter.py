# encrypt.py

# Importando as bibliotecas necessárias
from Crypto.Cipher import AES             # Biblioteca para encriptação AES
from Crypto.Hash import SHA256            # Biblioteca para geração de hash SHA256
from Crypto.Util.Padding import pad       # Biblioteca para preencher dados antes da encriptação
import pandas as pd                       # Biblioteca para manipulação de arquivos CSV

# Senha utilizada para encriptar o CSV
KEY = SHA256.new(b"OceanSec-SenhaSegura").digest()
# Inicialização do vetor para AES (precisa ter o tamanho de um bloco AES)
IV = b"0123456789ABCDEF"
# Define o modo de operação do AES como CBC (Cipher Block Chaining)
MODE = AES.MODE_CBC
# Cria um objeto de cifra AES com a chave e modo especificados
CIPHER = AES.new(KEY, MODE, IV)

# Função para encriptar dados
def encrypt_data(data):
    # Preenche os dados para garantir que eles tenham um múltiplo do tamanho do bloco AES
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    # Encripta os dados
    encrypted = CIPHER.encrypt(padded_data)
    # Retorna os dados encriptados como uma string hexadecimal
    return encrypted.hex()

# Função para encriptar um arquivo CSV
def encrypt_csv(input_filename, output_filename):
    # Carrega o arquivo CSV
    df = pd.read_csv(input_filename, delimiter=';')
    # Para cada coluna do CSV
    for column in df.columns:
        # Encripta os dados da coluna
        df[column] = df[column].apply(lambda x: encrypt_data(str(x)))
    # Salva o CSV encriptado
    df.to_csv(output_filename, sep=';', index=False)

# Encripta o arquivo 'original.csv' e salva como 'encrypted.csv'
encrypt_csv('original.csv', 'encrypted.csv')

