### Introdução
Este projeto foi projetado usando as tecnologias mais recentes do
mercado. Segue os pré-requisitos:  
* Python 3.3 (recomendado Python 3.4)  
* MySQL 5.6 ou superior  
### Instalação de pacotes no sistema
```shell
$ sudo apt-get install $(cat packages.txt)
```
### Instalação das dependências do projeto
> É altamente recomendável o uso de virtualenv na configuração e
> execução do projeto. Para mais informações, consulte a página oficial:
> http://virtualenv.readthedocs.org

```shell
$ pip3 install -r requirements.txt
```
### Configuração do branco  
```shell
$ mysqladmin -u root -p 
mysql> CREATE DATABASE cursodeextensao;
mysql> CREATE USER 'escola'@'localhost' IDENTIFIED BY '#!Q@W#E$R';
mysql> GRANT ALL PRIVILEGES ON cursodeextensao.* TO 'escola'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit;
```
### Executar o projeto  
```shell
$ python3 manage.py migrate    # Cria o banco de dados e todas as tabelas
$ python3 manage.py runserver  # Executa a aplicação no servidor de desenvolvimento
```
