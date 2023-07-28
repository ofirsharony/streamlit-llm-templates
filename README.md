
# Streamlit LLM templates

A small library of examples for getting started with streamlit, LLM and langchain.

Fork and get started.

# Example

![Alt text](./resources/llm_stories_generator.png?raw=true "single question template")

## Templates

* Single question template - with an example of an LLM story generator.
* Chat with vector DB template - coming soon.
## Run Locally

Clone the project

```bash
  git clone https://github.com/ofirsharony/streamlit-llm-templates.git
```

Go to the project directory, to the desired template, e.g

```bash
  cd streamlit-llm-templates/single-question-llm
```

Install dependencies, by either 'pip install -r requirements.txt' or directly via

```bash
  pip install openai langchain streamlit
```

Make sure your OpenAI key is defined as environment var 
```bash
  export OPENAI_API_KEY=sk-XXXX
```

Run it!

```bash
  streamlit run single-question-llm.py
```

## Contributing

Contributions are always welcome!

Feel free to add your own templates.

## License

You are free to do whatever you'd like, including copying, modifying and distributing, without any need for attribution.

