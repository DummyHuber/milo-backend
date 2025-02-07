from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence
from app.config import settings
from app.models import Message
from app.prompts import NEW_MESSAGE_PROMPT


class LLMService:
    def get_llm_model(self):
        """Returns an LLM instance."""
        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            temperature=settings.LLM_TEMPERATURE,
        )

    def get_llm_response(self, message_question: str, chat_history: list[Message] | None = None):
        """Creates a message, queries the AI, and streams the response."""
        try:
            prompt_template = PromptTemplate.from_template(NEW_MESSAGE_PROMPT)
            formatted_chat_history = "\n".join([f"{msg.question}: {msg.response}" for msg in chat_history])
            user_prompt = {
                'user_query': message_question,
                'chat_history': formatted_chat_history,
            }

            chain = prompt_template | self.get_llm_model()

            for chunk in chain.stream(user_prompt):  # Use regular for-loop
                yield chunk.content

        except Exception as e:
            yield str(e)
