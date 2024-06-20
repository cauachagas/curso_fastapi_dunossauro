# curso_fastapi_dunossauro
Repositório para o curso de FastAPI do canal https://www.youtube.com/@Dunossauro, utilizando PDM com gerenciador de projeto

# PDM

Veja a [documentação](https://pdm-project.org/latest/#recommended-installation-method) para instalação do PDM

Após o PDM instalado, é preciso instalar a versão mínima necessária (`3.12.*`) do projeto

- `pdm python install 3.12.3` (baixa a versão `3.12.3` do python)
- `pdm use @3.12.3` (configura o PDM para utilizar a versão baixada)
- `pdm install` (instala os pacotes do projeto)

Feito isso, é possível rodar os `pdm.scripts` encontradados no [pyproject.toml](./pyproject.toml#L38)

- `pdm server` (`server` é um dos scripts do projeto.)
