name 'default'
description 'Default, every server is it.'
recipes 'apt', 'build-essential', 'python', 'libpq-dev', 'ohai', 'yum', 'mysql::server', 'mysql::client', 'nginx' ,'gunicorn'
