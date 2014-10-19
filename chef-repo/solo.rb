# estas configs somente sao usadas para o chef na maquina

file_cache_path "/tmp/vagrant-chef-1"
cookbook_path ["/opt/app/curso-de-extensao/chef-repo/cookbooks"]
role_path nil
log_level :info

encrypted_data_bag_secret "/tmp/encrypted_data_bag_secret"

data_bag_path "/opt/app/curso-de-extensao/chef-repo/data_bags"

http_proxy nil
http_proxy_user nil
http_proxy_pass nil
https_proxy nil
https_proxy_user nil
https_proxy_pass nil
no_proxy nil
