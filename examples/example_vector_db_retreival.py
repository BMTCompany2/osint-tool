from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from typing import List

load_dotenv()

llm = ChatOpenAI()
llm_deterministic = ChatOpenAI(temperature=0) # This is for tag assignment and we want a near deterministic model
embeddings = OpenAIEmbeddings()
csv_parser = CommaSeparatedListOutputParser()
str_parser = StrOutputParser()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=200)

def _create_summary(self, query):
        # Log function and inputs
        self._logger.spacing()
        self._logger.private_function(f"_create_summary()") 
        self._logger.input(f"title: {query}")

        summary_prompt = ChatPromptTemplate.from_template(
            """Write a 3 bullet point summary about the topic based only on the following context:
            {context}
            TOPIC: {topic}"""
        )
        summary_chain = (
            RunnablePassthrough.assign(context=(lambda x: self._format_docs(x["context"])))
            | summary_prompt
            | llm
            | str_parser
        )
        summary_chain_retreival = RunnableParallel(
            {"context": self._source_retreiver, "topic": RunnablePassthrough()}
        ).assign(answer=summary_chain)

        summary_w_sources = summary_chain_retreival.invoke(query)
        summary_unformatted = summary_w_sources['answer']
        source_chunks = summary_w_sources['context']

        summary_unformatted = summary_unformatted.split('\n')
        summary = [sentence.lstrip('-* ').rstrip().rstrip('.') for sentence in summary_unformatted if sentence.strip()]

        # Log function output
        self._logger.output(f"summary: {summary}")
        self._logger.output(f"source chunk count: {len(source_chunks)}")
        for source in source_chunks:
            self._logger.output(f" -source title: {source.metadata['title']}")

        return summary, source_chunks