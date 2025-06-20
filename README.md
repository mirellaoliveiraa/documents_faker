✨ Funcionalidades
✅ Geração de documentos médicos com:

Título aleatório (Atestado, Laudo, Receituário)

Nome, CPF, endereço e CRM fictícios

Corpo de texto simulado

Inserção automática de:

Logos (Unimed, Hapvida, Docway, etc.)

Selos de assinatura digital

QR Codes

Assinaturas

✅ Controle de posicionamento via CSV (dimensoes.csv)

✅ Anti-sobreposição de elementos (logos, selos, QR)

✅ Geração de variações visuais:

Rotação (leve ou 180°)

Alteração de brilho, opacidade e alinhamento

✅ Salva os arquivos automaticamente em PDF

🗂️ Estrutura de pastas


documents_faker/
├── assets/
│   ├── ass_elements/   # Assinaturas
│   ├── fonts/          # Fontes
│   ├── logo_sign/      # Logos
│   ├── qr/             # QRCodes
│   └── selos_rodape/   # Selos
├── output/             # Arquivos gerados (PDFs)
├── dimensoes.csv       # Arquivo com posicionamento dos elementos
├── main.py             # Script principal
└── README.md           # Este arquivo
⚙️ Como rodar
Clone o repositório:

git clone https://github.com/mirellaoliveiraa/documents_faker.git
cd documents_faker
Crie e ative um ambiente virtual (opcional, recomendado):



python -m venv venv
venv\Scripts\activate   # No Windows
Instale as dependências:


pip install -r requirements.txt
Execute o script:


python main.py
📄 Arquivo dimensoes.csv
Nele você define onde cada logo, selo ou QR aparece no documento:

nome	arquivo	W	H	X	Y
unimed	unimed.png	400	90	100	50
qr	qr.png	120	120	900	1500
assinatura	sign.png	400	80	60	1475
selo_icp	icp_brasil.png	300	90	60	1550

W e H são largura e altura.

X e Y são as coordenadas no canvas.

🔥 Exemplo de documento gerado
<img src="https://github.com/mirellaoliveiraa/documents_faker/assets/example.png" width="500"/>
💻 Tecnologias usadas
Python 🐍

Pillow (PIL)

Faker

Pandas

🤝 Contribuições
Sinta-se livre para abrir PRs, relatar issues ou sugerir melhorias. Bora construir juntos!

⚠️ Aviso legal
Este projeto gera dados e documentos completamente fictícios. É destinado exclusivamente para fins educacionais, acadêmicos e treinamento de modelos de IA.

⭐ Dá uma estrela se te ajudei! 😍
🚀 Mirella Oliveira • github.com/mirellaoliveiraa
