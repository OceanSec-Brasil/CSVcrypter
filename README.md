# CSVcrypter

## Descrição

CSVcrypter é uma ferramenta Python projetada para encriptar arquivos CSV utilizando uma chave de segurança específica. O objetivo é garantir que seus dados sensíveis armazenados em formatos CSV estejam seguros e protegidos.

## Requisitos

- Python 3.x
- Bibliotecas: csv, cryptography

## Como usar

1 - Clone este repositório para sua máquina local.
```
git clone https://github.com/seu_usuario/CSVcrypter.git
```
2 - Entre no diretório do projeto e instale as dependências necessárias.
```
cd CSVcrypter
pip install -r requirements.txt
```
3 - Execute o script.
```
python csvcrypter.py --input seu_arquivo.csv --output arquivo_criptografado.csv
```
## Parâmetros

--input ou -i: Define o arquivo CSV de entrada que você deseja encriptar.
--output ou -o: Define o nome do arquivo CSV de saída que será criado após a encriptação.

## Notas

Este script é apenas para fins educativos e deve ser usado em ambientes controlados. Certifique-se de ter as permissões adequadas ao manipular arquivos CSV contendo informações sensíveis.

## Licença

Licença MIT. Consulte o arquivo LICENSE para mais informações.
