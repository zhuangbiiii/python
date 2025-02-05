from transformers import pipeline

# 使用情绪分析流水线
#classifier = pipeline('sentiment-analysis')
#classifier('We are very happy to introduce pipeline to the transformers repository.')

# 使用问答流水线
#question_answerer = pipeline('question-answering')
#question_answerer({
#    'question': 'What is the name of the repository ?',
#    'context': 'Pipeline has been included in the huggingface/transformers repository'
#})

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)