# Manifest that sets up web servers for deployment of a static site
exec {'setup nginx':
  command  => 'sudo apt-get -y update && sudo apt-get -y upgrade',
'sudo apt-get -y install nginx',
'sudo mkdir -p /data/web_static/releases/test /data/web_static/shared',
  provider => shell,
}
