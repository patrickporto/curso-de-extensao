# -*- encoding: utf-8 -*-
from fabric.api import (
    env,
    run,
    local,
    prefix,
)
from fabric.contrib.project import rsync_project
from fabric.context_managers import (
    cd,
    shell_env,
)


rm = lambda path: run('rm -rf {0}'.format(path))
mkdir = lambda dirname: run('mkdir -p {0}'.format(dirname))
pkg_install = lambda name: run('apt-get install -y {0}'.format(name))


def deploy(setup='n'):
    """
    Realizar deploy de uma versão da aplicação para o ambiente
    >> fab prod deploy:tag=master,setup=True
    """
    if setup.lower() == 's':
        __update()
        __create_structure()
        __upload()
        __install_packages()
        __settings_gunicorn()
        __settings_nginx()
        __install_virtualenv()
    else:
        __upload()
    with prefix('source /opt/env/bin/activate'),shell_env(DJANGO_SETTINGS_MODULE=env.DJANGO_SETTINGS):
        __install_dependencies()
        __migrate()
        __collecstatic()
    __restart_services()


def __create_structure():
    """
    Cria estrutura de pastas no ambiente
    """
    # Criação da pasta da aplicação
    mkdir('/opt/app')
    # Criação da pasta dos statics
    mkdir('/opt/static')
    # Criação da pasta dos medias
    mkdir('/opt/media')


def __upload():
    """
    Sincroniza pasta do projeto com produção
    """
    rsync_project(
        local_dir='./',
        remote_dir='/opt/app',
        exclude=['.git', 'media', '*.pyc', '__pycache__',
                 '.gitignore', 'fabfile', 'README.md'],
        delete=True,
    )


def __install_packages():
    """
    Instalação dos pacotes para o sistema
    """
    with cd('/opt/app/'):
        pkg_install('$(cat packages.txt)')


def __install_dependencies():
    """
    Instalação das dependências do sistema
    """
    with cd('/opt/app/'):
        run('pip install -r requirements.txt')



def __update():
    """
    Atualiza lista de repositórios
    """
    run('apt-get update')


def __settings_nginx():
    """
    Instalação do nginx
    """
    with cd('/opt/app/'):
        rm('/etc/nginx/sites-enabled/*')
        run('ln -f ./curso_de_extensao/nginx.conf /etc/nginx/sites-enabled/django')


def __settings_gunicorn():
    """
    Instalação do gunicorn
    """
    with cd('/opt/app/'):
        rm('/etc/init/gunicorn.conf')
        run('ln -f ./curso_de_extensao/gunicorn.conf /etc/gunicorn.conf')
        run('ln -f ./curso_de_extensao/gunicorn.conf /etc/init/gunicorn.conf')


def __restart_services():
    """
    Reinicia os serviços
    """
    run('service nginx restart')
    run('service gunicorn restart')


def __migrate():
    """
    Migração do banco de dados
    """
    with cd('/opt/app/'):
        run('python ./manage.py migrate --noinput')


def __collecstatic():
    """
    Coleta de arquivos estáticos
    """
    with cd('/opt/app/'):
        run('python ./manage.py collectstatic --noinput')
        rm('./static')


def __install_virtualenv():
    """
    Instalação de virtualenv
    """
    run('pip install virtualenv')
    run('virtualenv /opt/env')

