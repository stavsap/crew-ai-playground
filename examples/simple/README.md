# Simple Crew Demo

2 tasks and 2 agents.

Install, recommended to use venv.

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Local LLMs

### [Text Gen](https://github.com/oobabooga/text-generation-webui)

Run text with api flag.

[Text gen API](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API) now supports [OpenAI API](https://openai.com/product#made-for-developers) so there is a need to set the 'OPENAI_API_BASE' env var to reach you text gen instance.

### [Ollama](https://github.com/jmorganca/ollama)

#### [Docker](https://hub.docker.com/r/ollama/ollama)

Run Ollama Locally

```shell
docker run -d --rm --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.1.27
```

Load a model

```shell
docker exec -it ollama ollama run gemma:7b
```
