# Fix bad phpp extensions to php inside WordPress config file wp-settings.php.
# `require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );`

exec { 'fix-line':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
