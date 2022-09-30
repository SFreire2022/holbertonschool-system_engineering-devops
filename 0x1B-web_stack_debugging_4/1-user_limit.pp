# Change hard file limit for Holberton user.
exec { 'change-HFL-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Change soft file limit for Holberton user.
exec { 'change-SFL-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/4990/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
