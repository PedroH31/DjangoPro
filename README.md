# DjangoPro
website simples para implementar meus conhecimentos em django.
Código de desenvolvimento no módulo Django do Site [Dev Pro](https://pythonpro.com.br/)

### <strong>Instruções para instalação</strong>:

#### Criar e ativar ambiente virtual Python (venv):

```python -m venv .venv```

```source .venv/bin/activate```

#### <strong>Instalar dependências</strong>:

```pip install -r requirements.txt```

#### <strong>Instalar dependências, inclusive de desenvolvimento</strong>:

```pip install -r requirements-dev.txt```

#### Copiar variáveis de ambiente:

```cp contrib/env-sample .env```

#### Rodar Django:

```python manage.py runserver```

#### Localizar arquivo manage.py:

```alias mng="python $VIRTUAL_ENV/../manage.py"```

### <strong>Instalar o flyctl</strong>:

```curl -L https://fly.io/install.sh | sh```

#### Após instalar o flyctl:

copie os caminhos export para o seu arquivo: ```source ~/.zshrc```

#### Rodar o fly.io:
```fly launch```

#### cobertura de testes:
```pipenv install --dev 'pytest-cov' codecov```

#### python decouple:
```pipenv install 'python-decouple'```