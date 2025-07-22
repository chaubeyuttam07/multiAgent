from transformers import pipeline

class ResponseAgent:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.qa_pipeline = pipeline("question-answering", model=model_name)

    def generate_response(self, question, context):
        """Generate a response using the question and context."""
        response = self.qa_pipeline(question=question, context=context)
        return response['answer']