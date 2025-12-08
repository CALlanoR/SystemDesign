# Simple Question Answering Application

Modern implementation of a Question & Answer application using LangChain with streaming capabilities.

## Features

- ✅ Modern LangChain implementation with LCEL (LangChain Expression Language)
- ✅ Real-time streaming responses
- ✅ Interactive command-line interface
- ✅ ChatOpenAI with latest models (gpt-4o-mini, gpt-4, gpt-3.5-turbo)
- ✅ Environment variable management with python-dotenv
- ✅ Error handling and user-friendly messages
- ✅ Spanish language support

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv

   # On Linux/Mac:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**:

   Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Usage

Run the application:

```bash
python app.py
```

### Commands

- Type any question to get an answer
- Type `help` to see available commands
- Type `salir`, `exit`, or `quit` to exit

### Example Session

```
============================================================
Bienvenido al Asistente de Preguntas y Respuestas
============================================================
Escribe 'salir', 'exit' o 'quit' para terminar
Escribe 'help' para ver los comandos disponibles

You: ¿Cuál es la capital del Valle del Cauca en Colombia?
AI: La capital del Valle del Cauca en Colombia es Cali.

You: exit
¡Hasta luego!
```

## Code Structure

### Main Functions

- **`load_answer(question)`**: Processes questions with streaming enabled
- **`load_answer_no_streaming(question)`**: Alternative without streaming
- **`main()`**: Interactive loop for continuous Q&A

### Modern LangChain Features

1. **LCEL (LangChain Expression Language)**:
   ```python
   chain = prompt | llm | output_parser
   ```

2. **Streaming**:
   ```python
   for chunk in chain.stream({"question": question}):
       print(chunk, end="", flush=True)
   ```

3. **ChatPromptTemplate**:
   ```python
   prompt = ChatPromptTemplate.from_messages([
       ("system", "System message here"),
       ("human", "{question}")
   ])
   ```

## Configuration

Edit these values in `app.py` if needed:

- **Model**: Change `model="gpt-4o-mini"` to:
  - `"gpt-3.5-turbo"` - Faster, cheaper
  - `"gpt-4"` - More capable, expensive
  - `"gpt-4-turbo"` - Balance of speed and capability

- **Temperature**: Change `temperature=0` (0-2):
  - `0` - Deterministic, consistent
  - `1` - Balanced creativity
  - `2` - Maximum creativity

## Dependencies

- `langchain==0.3.20` - Main LangChain library
- `langchain-openai==0.3.0` - OpenAI integration
- `langchain-core==0.3.28` - Core components
- `openai==1.59.8` - OpenAI client
- `python-dotenv==1.0.0` - Environment variables
- `streamlit==1.32.2` - Optional UI framework
- `colorama==0.4.6` - Optional colored output

## Troubleshooting

### Error: "OPENAI_API_KEY no está configurada"

Make sure you:
1. Created the `.env` file
2. Added your actual API key
3. The `.env` file is in the same directory as `app.py`

### Error: "can't adapt type 'dict'" or similar

Update your dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Error: "Model not found"

Change to a valid model name:
- `gpt-4o-mini` (recommended)
- `gpt-3.5-turbo`
- `gpt-4`

## Version History

- **v2.0** (2025): Modern implementation with LCEL and streaming
- **v1.0** (2024): Original implementation with deprecated features

## License

MIT License - Feel free to use and modify

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Expression Language Guide](https://python.langchain.com/docs/expression_language/)
