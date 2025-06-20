import os
import random
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
from faker import Faker

# ================= CONFIGURAÇÕES =================
BASE_WIDTH = 1080
BASE_HEIGHT = 1920

OUTPUT_DIR = "./output"
ASSETS_DIR = "./assets"
ASS_DIR = os.path.join(ASSETS_DIR, "ass_elements")
QR_DIR = os.path.join(ASSETS_DIR, "qr")
LOGO_DIR = os.path.join(ASSETS_DIR, "logo_sign")
SELOS_DIR = os.path.join(ASSETS_DIR, "selos_rodape")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

faker = Faker("pt_BR")

# ================= CARREGAR CSV =================
df = pd.read_csv("dimensoes.csv")

dimensoes = {}
for _, row in df.iterrows():
    nome = row['nome']
    dimensoes[nome] = {
        'arquivo': row['arquivo'],
        'W': int(row['W']),
        'H': int(row['H']),
        'X': int(row['X']),
        'Y': int(row['Y'])
    }

# ================= FUNÇÃO DE ROTAÇÃO DO DOCUMENTO FINAL =================
def aplicar_rotacao_documento(img):
    angulo = random.choice([0, 2, -2, 180])  # 0: sem rotação, 2/-2 graus leve ou 180 (ponta cabeça)
    if angulo == 0:
        return img
    elif angulo == 180:
        return img.transpose(Image.ROTATE_180)
    else:
        return img.rotate(angulo, expand=True, resample=Image.BICUBIC, fillcolor=(255, 255, 255))

# ================= FUNÇÃO INSERIR IMAGEM (ANTI-SOBREPOSIÇÃO) =================
def inserir_imagem(base, pasta, item, ocupados):
    if item not in dimensoes:
        print(f"❌ {item} não encontrado no CSV.")
        return False

    info = dimensoes[item]
    img_path = os.path.join(pasta, info['arquivo'])

    if not os.path.exists(img_path):
        print(f"❌ Arquivo {img_path} não encontrado.")
        return False

    img = Image.open(img_path).convert("RGBA")

    w = info['W']
    h = info['H']
    x = info['X']
    y = info['Y']

    # Corrige para não ultrapassar bordas
    if x + w > BASE_WIDTH:
        x = BASE_WIDTH - w
    if y + h > BASE_HEIGHT:
        y = BASE_HEIGHT - h
    x = max(0, x)
    y = max(0, y)

    # Verifica se cabe
    if w <= 0 or h <= 0:
        print(f"⚠️ {item} não cabe na área.")
        return False

    novo_retangulo = (x, y, x + w, y + h)

    # Verificar sobreposição
    for rect in ocupados:
        if not (novo_retangulo[2] <= rect[0] or novo_retangulo[0] >= rect[2] or
                novo_retangulo[3] <= rect[1] or novo_retangulo[1] >= rect[3]):
            print(f"🔴 {item} sobrepõe outro elemento. Pulando...")
            return False

    ocupados.append(novo_retangulo)

    img = img.resize((w, h))
    base.paste(img, (x, y), img)
    return True


# ================= GERAR DOCUMENTOS =================
quantidade = 10

for idx in range(1, quantidade + 1):
    base_img = Image.new("RGB", (BASE_WIDTH, BASE_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(base_img)
    ocupados = []  # Lista para controlar áreas ocupadas

    # Dados sintéticos
    nome_paciente = faker.name()
    cpf = faker.cpf()
    endereco = faker.address().replace("\n", " ")
    crm = f"{random.randint(10000,99999)}/SP"

    # Título
    titulo = random.choice(["ATESTADO MÉDICO", "RECEITUÁRIO", "LAUDO MÉDICO"])
    titulo_font = ImageFont.truetype("arial.ttf", size=42)
    draw.text((300, 250), titulo, fill="black", font=titulo_font)

    # Cabeçalho
    cabecalho = f"Nome: {nome_paciente}   CPF: {cpf}\nEndereço: {endereco}\nCRM: {crm}\n\n"
    cabecalho_font = ImageFont.truetype("arial.ttf", size=26)
    draw.text((100, 320), cabecalho, fill="black", font=cabecalho_font)

    # Texto corpo
    texto = " ".join([faker.paragraph(nb_sentences=5) for _ in range(3)])
    linhas = textwrap.wrap(texto, width=70)
    font = ImageFont.truetype("arial.ttf", size=28)

    for i, linha in enumerate(linhas):
        y = 500 + i * 35
        draw.text((100, y), linha, fill="black", font=font)

    # Inserir logos
    if os.listdir(LOGO_DIR):
        for logo in random.sample(os.listdir(LOGO_DIR), k=min(2, len(os.listdir(LOGO_DIR)))):
            inserir_imagem(base_img, LOGO_DIR, logo.split('.')[0], ocupados)

    # Inserir QR codes (🔥 agora SEM duplicar!)
    if os.listdir(QR_DIR):
        qr_selecionado = random.choice(os.listdir(QR_DIR))
        inserir_imagem(base_img, QR_DIR, qr_selecionado.split('.')[0], ocupados)

    # Inserir assinatura
    if os.listdir(ASS_DIR):
        assinatura = random.choice(os.listdir(ASS_DIR))
        inserir_imagem(base_img, ASS_DIR, assinatura.split('.')[0], ocupados)

    # Inserir selos rodapé
    if os.listdir(SELOS_DIR):
        for selo in os.listdir(SELOS_DIR):
            inserir_imagem(base_img, SELOS_DIR, selo.split('.')[0], ocupados)

    # Texto fixo rodapé
    rodape_text = "Documento assinado digitalmente. Valide em www.site.com.br"
    rodape_font = ImageFont.truetype("arial.ttf", size=20)
    rodape_y = 1850
    text_width = draw.textlength(rodape_text, font=rodape_font)
    draw.text(((BASE_WIDTH - text_width) / 2, rodape_y), rodape_text, fill="black", font=rodape_font)

    # 🔥 APLICAR ROTAÇÃO NO DOCUMENTO FINAL INTEIRO
    base_img = aplicar_rotacao_documento(base_img)

    # Salvar PDF
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    output_file = os.path.join(OUTPUT_DIR, f"documento_{idx}.pdf")
    base_img.save(output_file, "PDF", resolution=100.0)
    print(f"✅ Documento {idx} gerado.")

print("🚀 Todos os documentos foram gerados com sucesso!")
