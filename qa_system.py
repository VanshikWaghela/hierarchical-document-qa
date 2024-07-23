from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def setup_qa_system(model, vector_index):
    prompt_template = '''Answer the question as precisely as possible using the provided context. If the answer is
     not contained in the context, say "answer not available in context"\n
     Context = \n{context}?\n
     Question: \n {question} \n
     Answer:
     '''
    prompt = PromptTemplate(
        template=prompt_template, input_variables=['context', 'question']
    )

    stuff_chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=vector_index,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return stuff_chain

def answer_question(qa_chain, question):
    answer = qa_chain({"query": question})
    return answer['result']