# python
自己写的一些偷懒脚本
python -m venv .env

# Activate the virtual environment
source .env/bin/activate
# Deactivate the virtual environment
source .env/bin/deactivate

# huggingface pak list
pip install transformers
pip install 'transformers[torch]'
pip install "transformers[sentencepiece]"
pip install xformers
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
