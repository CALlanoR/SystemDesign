"""
LangChain Question Answering Application with Streaming
Using LangChain Expression Language (LCEL) and ChatOpenAI
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def load_answer(question):
    """
    Function to get answer using modern LangChain with LCEL

    Args:
        question (str): User's question

    Returns:
        str: AI's response
    """
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # Modern model (can also use "gpt-3.5-turbo" or "gpt-4")
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        streaming=True  # Enable streaming for real-time responses
    )

    # Create a modern chat prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil que responde preguntas de manera clara y concisa en español."),
        ("human", "{question}")
    ])

    # Output parser to convert response to string
    output_parser = StrOutputParser()

    # Create the chain using LangChain Expression Language (LCEL)
    chain = prompt | llm | output_parser

    # Stream the response
    print("AI: ", end="", flush=True)
    full_response = ""

    for chunk in chain.stream({"question": question}):  # devuelve fragmentos (chunks) conforme se generan
        print(chunk, end="", flush=True) # Le dice a print() que NO agregue un salto de línea al final, Fuerza la salida inmediata del buffer
        full_response += chunk

    print()  # New line after streaming completes

    return full_response


# Visualización del flujo:
# Sin streaming (.invoke()):
# Usuario: "¿Cuál es la capital de Francia?"
# [Esperando... 2 segundos]
# AI: "La capital de Francia es París."  ← Todo aparece de golpe
# Con streaming (.stream()):
# Usuario: "¿Cuál es la capital de Francia?"
# AI: L                     ← Chunk 1 (instantáneo)
# AI: La                    ← Chunk 2 (0.1s después)
# AI: La cap                ← Chunk 3
# AI: La capital            ← Chunk 4
# AI: La capital de         ← Chunk 5
# AI: La capital de Fr      ← Chunk 6
# AI: La capital de Francia ← Chunk 7
# AI: La capital de Francia es
# AI: La capital de Francia es París.  ← Final


def load_answer_no_streaming(question):
    """
    Alternative function without streaming (for comparison)

    Args:
        question (str): User's question

    Returns:
        str: AI's response
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil que responde preguntas de manera clara y concisa en español."),
        ("human", "{question}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({"question": question})

    return response


def get_text():
    """Get user input"""
    input_text = input("You: ")
    return input_text


def main():
    print("=" * 60)
    print("Asistente de Preguntas y Respuestas")
    print("=" * 60)
    print("Escribe 'salir', 'exit' o 'quit' para terminar")
    print("Escribe 'help' para ver los comandos disponibles\n")

    while True:
        user_input = get_text()

        # Check for exit commands
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("\n¡Hasta luego!")
            break

        # Check for help command
        if user_input.lower() == 'help':
            print("\nComandos disponibles:")
            print("  - Escribe cualquier pregunta para obtener una respuesta")
            print("  - 'salir', 'exit', 'quit': Salir del programa")
            print("  - 'help': Mostrar esta ayuda\n")
            continue

        # Skip empty inputs
        if not user_input.strip():
            continue

        try:
            # Get and display answer with streaming
            response = load_answer(user_input)
            print()  # Extra line for readability

        except Exception as e:
            print(f"\nError: {e}")
            print("Por favor, verifica tu API key en el archivo .env\n")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY no está configurada en el archivo .env")
        print("Por favor, crea un archivo .env con tu API key de OpenAI")
        exit(1)

    # Run the main interactive loop
    main()
