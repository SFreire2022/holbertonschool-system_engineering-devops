# Puppet script to Install Nginx server, configure and creating a custom HTTP header response.

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'X-Served-By':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
