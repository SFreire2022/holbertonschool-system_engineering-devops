# Increase ULIMIT value For default Nginex server config
exec { 'Increase-ULIMIT_':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx Service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
