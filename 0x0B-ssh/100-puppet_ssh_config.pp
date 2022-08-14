# Configure the SSH client to authenticates only through SSh keys
include stdlib
file_line { ' Deny pass auth':
  path    => '/etc/ssh/ssh_config',
  line    => ' PasswordAuthentication no',
  replace => true,
}
file_line { ' Add id private key file':
  path    => '/etc/ssh/ssh_config',
  line    => ' IdentityFile ~/.ssh/school',
  replace => true,
}
