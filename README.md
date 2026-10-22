📊 Automação de Relatórios Geográficos & Envio de E-mails com Python

Este projeto consiste numa solução automatizada de inteligência de dados e engenharia de processos que lê a base de clientes do e-commerce Olist, consolida métricas geográficas estratégicas, gera um gráfico executivo em alta definição e dispara um relatório via e-mail (SMTP com criptografia TLS) de forma 100% automatizada.

🎯 Objetivos do Projeto

Processamento de Dados: Leitura da base olist_customers_dataset.csv, extração de volumetria e ordenação dos 10 estados com maior concentração de clientes.

Visualização de Dados: Geração de gráfico de barras horizontais nítido (300 DPI) formatado especificamente para relatórios executivos.

Automação de E-mail: Estruturação de mensagem em contêiner MIMEMultipart, suporte a anexos binários codificados em Base64 e envio seguro utilizando o protocolo SMTP.

🛠️ Tecnologias Utilizadas

Python 3.x

Pandas: Manipulação, agregação e limpeza dos dados.

Matplotlib: Construção e exportação de gráficos estatísticos.

smtplib & email (Nativos do Python): Protocolo de comunicação SMTP, segurança SSL/TLS e estruturação de mensagens MIME.

📁 Estrutura do Projeto

.
├── main.py                     # Script principal de execução
├── olist_customers_dataset.csv # Base de dados de clientes
├── clientes_por_estado.png     # Gráfico gerado automaticamente (exportação 300 DPI)
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do repositório


🚀 Como Executar o Projeto

1. Clonar o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


2. Instalar as dependências

pip install -r requirements.txt


3. Configurar Credenciais de E-mail

No ficheiro main.py, atualize as variáveis do remetente, destinatário e senha de aplicativo:

remetente = "seu_email@gmail.com"
destinatario = "destinatario@gmail.com"
senha = "sua_senha_de_aplicativo"  # Senha de 16 dígitos gerada na Conta Google


⚠️ Nota de Segurança: Para enviar e-mails via Gmail, certifique-se de ativar a Verificação em Duas Etapas e gerar uma Senha de Aplicativo. Nunca disponibilize a sua senha pessoal no código.

4. Executar o script

python main.py


📊 Exemplo do Relatório Gerado

O e-mail enviado contém um resumo em texto formatado com separadores de milhar e o gráfico em anexo:

Métricas Extraídas: Total de clientes, clientes únicos e identificação dinâmica do estado líder em volume.

Anexo: Gráfico de barras horizontais comparativo dos Top 10 estados.

📝 Licença

Este projeto foi desenvolvido para fins de estudo e portfólio profissional. Fique à vontade para sugerir melhorias!
