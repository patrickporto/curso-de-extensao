## Introdução ##
* Python 2.7
* MySQL 5.5 ou superior
#### Instalação de pacotes no sistema ####
```shell
$ sudo apt-get install $(cat packages.txt)
```
#### Instalação das dependências do projeto ####
> É altamente recomendável o uso de virtualenv na configuração e
> execução do projeto. Para mais informações, consulte a página oficial:
> http://virtualenv.readthedocs.org

```shell
$ pip2 install -r requirements.txt
```
### Configuração do banco de dados ###
```shell
$ mysqladmin -u root -p
mysql> CREATE DATABASE cursodeextensao;
mysql> CREATE USER 'escola'@'localhost' IDENTIFIED BY '#!Q@W#E$R';
mysql> GRANT ALL PRIVILEGES ON cursodeextensao.* TO 'escola'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit;
```
### Executar o projeto ###
```shell
$ python2 manage.py migrate    # Cria o banco de dados e todas as tabelas
$ python2 manage.py runserver  # Executa a aplicação no servidor de desenvolvimento
```
### Deploy para o ambiente de produção ###
Mude a permissão da chave de deploy:
```shell
$ chmod 644 fabfile/deploy
```
Para realizar deploy em um ambiente novo, execute o seguinte comando:
```shell
$ fab prod deploy:setup=True
```
> O arquivo fabfile/environments.py é o módulo responsável pela configuração
> de ambientes. Neste módulo é onde fica o host, user e endereço da key de
> deploy, havendo possibilidade de acrescentar a senha de acesso.
> Para mais informações:
> http://docs.fabfile.org/en/1.10/usage/env.html#environment-as-configuration

Caso o deploy seja em um ambiente já configurado, execute o seguinte comando:
```shell
$ fab prod deploy
```
