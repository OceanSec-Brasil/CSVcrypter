from cryptography.fernet import Fernet
import pandas as pd
import csv

# chave de encriptação
key = b'OceanSecKEYcsv'

cipher_suite = Fernet(key)

# Ler o arquivo CSV original
input_filename = 'original.csv'
df = pd.read_csv(input_filename)

# Encriptar as células do DataFrame
for column in df.columns:
    df[column] = df[column].apply(lambda x: cipher_suite.encrypt(str(x).encode()))

# Salvar o DataFrame encriptado como um novo arquivo CSV
output_filename = 'encrypted.csv'
df.to_csv(output_filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
