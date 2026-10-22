import matplotlib.pyplot as plt
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

#Carregar base de dados
df = pd.read_csv("olist_customers_dataset.csv")

#Tratamentos básicos para exemplos
# Contagem do tamanho da tabela para saber o Total de clientes
total_clientes = len(df)
# Contagem única de quantos clientes temos na tabela (sem repetir o cliente)
clientes_unicos = df["customer_unique_id"].nunique()
# Value_counts para contar quantas vezes cada estado aparece, head para pegar apenas os 10 primeiros itens e sort_values para ordenar em ordem decrescente
top_estados = df["customer_state"].value_counts().head(10).sort_values()

#Criar gráfico
plt.figure(figsize=(10,6)) # Criar área do gráfico
top_estados.plot(kind="barh", color="#2b5c8f", edgecolor="none") #tipo de gráfico e especificações do mesmo
plt.title("Top 10 Estados com Maior Base de Clientes (Olist)", fontsize=14, fontweight="bold") # Título do Gráfico
plt.xlabel("Número de Clientes", fontsize=11) # Título eixo X
plt.ylabel("Estado (UF)", fontsize=11) # Título eixo Y
plt.grid(axis="x", linestyle="--", alpha=0.5) # Linhas de grade e opacidade
plt.tight_layout() # Margens

# Guardar em alta resolução
caminho_grafico = "clientes_por_estado.png" # Nome do arquivo que vai ficar salvo na pasta
plt.savefig(caminho_grafico, dpi=300) # Salvando na pasta com o nome e a resolução desejada
plt.close() # Fecha a criação do gráfico

# Preparando o E-Mail
remetente = "coloque o email de quem vai enviar"
destinatario = "coloque o email de quem vai receber"
senha = "coloque a senha de app do servidor de email"

# Preparando a mensagem
mensagem = MIMEMultipart() #Criando o campo de email, que será preenchido abaixo com o remetente, destinatário e assunto. É como o campo de mensagem
mensagem["Subject"] = "relatório Automático: Análise Geográfica de Clientes" # Assunto do email
mensagem["From"] = remetente # O remetente definido acima
mensagem["To"] = destinatario # O destinatário definido acima

# Corpo do E-Mail
corpo_texto = f"""
Olá! Segue o relatório automatizado de clientes extraído da base de dados do Olist.

Resumo executivo da base:
- Total de Registros de Clientes: {total_clientes}
- Total de Clientes Únicos: {clientes_unicos}
- Estado Líder em Volume: {top_estados.index[-1]} ({top_estados.iloc[-1]:,} clientes)

O gráfico detalhado com o Top 10 estados encontra-se em anexo neste email.
"""

# Attach para anexar a mensagem ao corpo do email. 
mensagem.attach(MIMEText(corpo_texto, "plain")) # MIMEText prepara o texto, tendo o texto a ser preparado o corpo_texto e a formatação simples em "plain"
#Caso quiséssemos utilizar marcações HTML trocaríamos o "plain" por "html"

# Anexar Gráfico

with open(caminho_grafico, "rb") as anexo: # Vai abrir a imagem com o Open e o rb serve para ler o código binário da imagem (rb = read binary)
    parte = MIMEBase("application", 'octet-stream') # Cria um recipiente próprio para anexos genéricos (PDF, Imagem, Excel, etc...)
    # Apllication e Octet são os códigos padrões da internet, vai avisar para o servidor de email para trata-los como possível e necessário
    parte.set_payload(anexo.read()) # Anexo.read() vai ler todo o binário da imagem carregada
    # Set_playload vai carregar o anexo no campo anexo do email

encoders.encode_base64(parte) # Codifica o binário da imagem para o formato Base64 (Basicamente converte binário para código de texto)
parte.add_header ("Content-Disposition", f"attachment; filename= {caminho_grafico}") #Vai avisar basicamente 2 coisas
# 1º- Attachment - é um arquivo descarregável, então não é um texto inserido no corpo da mensagem
# 2º- filename - O nome que aparecerá para quem receber o email.
mensagem.attach(parte) # Vai pegar a imagem tratada e anexar no corpo principal do email


# Enviar

# Porta 587 para TLS / 465 para SSL
try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls() # Criptografia de segurança
    servidor.login(remetente, senha)

    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit() # Desliga o servidor da maneira correta e limpa

except Exception as e:
    print(f"Erro ao enviar o email: {e}")

