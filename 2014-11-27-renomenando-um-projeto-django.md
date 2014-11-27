# Renomeando um projeto Django #
## Introdução ##
Neste artigo, irei explicar como renomear um projeto django. Isso se faz necessário quando um projeto repentinamente muda de nome por conveniência ou até mesmo por problemas judiciais.  

## Visão geral ##
Após ter criado um projeto Django, renomeá-lo não é tão simples quanto trocar apenas o nome do pacote em que estão os códigos, pois existe referências dentro dos códigos. Isso ocorre porque existe uma tendência de códigos pythons trabalharem apenas com importações absolutas ([PEP 328](https://www.python.org/dev/peps/pep-0328/)).  
Para resolver nosso problema, devemos seguir o [project_template](https://github.com/django/django/tree/master/django/conf/project_template) do django e substituir tudo em que nele está como *project_name*.  

## Renomeando o projeto ##
Vá até a raiz do projeto django. 
```
.
├── antigo_nome_do_projeto
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── manage.py
```
A primeira, e mais óbvia, tarefa à fazer é renomear o pacote principal do projeto, onde fica o settings.py. Lembre-se que o padrão para nomes de pacotes em python é minúsculo com undercores ([PEP 8](https://www.python.org/dev/peps/pep-0008#naming-conventions)):  
```
.
├── novo_nome_do_projeto
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── manage.py
```
Agora abra o manage.py em qualquer editor de textos:  
```python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "antigo_nome_do_projeto.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```
Onde está sendo definido o o valor padrão para a variável de ambiente DJANGO_SETTINGS_MODULE, troque o nome do pacote conforme foi definido anteriormente:  
```python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novo_nome_do_projeto.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```

Após isso, vá até o pacote principal do projeto e abra o wsgi.py:
```python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "antigo_nome_do_projeto.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
Repita o que foi feito na etapa anterior:  
```diff
import os
- os.environ.setdefault("DJANGO_SETTINGS_MODULE", "antigo_nome_do_projeto.settings")
+ os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novo_nome_do_projeto.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
Depois vá até o settings.py e mude as contantes ROOT_URLCONF e WSGI_APPLICATION:
```diff
[...]
- ROOT_URLCONF = 'antigo_nome_do_projeto.urls'
+ ROOT_URLCONF = 'novo_nome_do_projeto.urls'

- WSGI_APPLICATION = 'antigo_nome_do_projeto.wsgi.application'
+ WSGI_APPLICATION = 'novo_nome_do_projeto.wsgi.application'
[..]
```
Pronto. Agora seu projeto deverá funcionar, mas lembresse de verificar se você precisou fazer outras referências ao pacote principal para que não ocorra problemas durante a execução do projeto.
