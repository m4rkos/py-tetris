#!/usr/bin/env bash
set -e

# Garante que a execução ocorra no diretório do script
cd "$(dirname "$0")"

# Verifica se existe um ambiente virtual ou cria um novo
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Ambiente virtual não encontrado. Criando 'venv'..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Instalando dependências..."
    pip install -r requirements.txt
fi

# Executa o jogo
echo "Iniciando Py Tetris..."
python app.py
