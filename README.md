### dialogpt-chatbot

This repository is a dockerised chatbot service based on dialogpt model.

To spin up the container for the first time, run

```bash
docker-compose down && docker-compose up --build
```

And access the chatbot UI at `http://127.0.0.1:5000`

Once the image is built, for the subsequent times, run

```bash
docker-compose down && docker-compose up
```

## Structure
<details>
	<summary> Show/Hide Details </summary>

- [static/](static/)
  - `style.css`: icons and images, this is copied from [the style.css by Arraxx](https://github.com/Arraxx/new-chatbot/blob/master/app/static/styles/style.css)
- [templates/](templates/)
  - `index.html`: html templates, this is adpted from [the index.html by Arraxx](https://github.com/Arraxx/new-chatbot/blob/master/app/templates/index.html)
- `app.py`: The app file
- `requirements.txt`: The python libraries to build the Docker image and support chatbot funxtions
- `Dockerfile`: For building the chatbot image
- `docker-compose.yml`: The recipe for running the app
- `dialogpt.py`: The python script supporting the chatbot functionality, it is rewritten from [hugginface model card](https://huggingface.co/microsoft/DialoGPT-medium)
- `save_pretrained_model.py`: The script to save dialogpt model and tokeniser at image build

</details>
