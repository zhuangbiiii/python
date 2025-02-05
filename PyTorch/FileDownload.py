# from huggingface_hub import hf_hub_download
# hf_hub_download(repo_id="distilbert-base-uncased-finetuned-sst-2-english", filename="config.json")

# hf_hub_download(repo_id="distilbert-base-uncased-finetuned-sst-2-english", filename="fleurs.py", repo_type="dataset")


# from huggingface_hub import snapshot_download
# snapshot_download(repo_id="distilbert-base-uncased-finetuned-sst-2-english")

# snapshot_download(repo_id="google/fleurs", repo_type="dataset")


# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
# model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B")

from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="bigscience/T0_3B", filename="config.json", cache_dir="./your/path/bigscience_t0")