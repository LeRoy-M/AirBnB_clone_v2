# Manifest that sets up web servers for deployment of a static site
exec {'setup web servers for deployment':
  command => 'sudo apt-get -y update;sudo apt-get -y upgrade;sudo apt-get -y install nginx;sudo mkdir -p /data/web_static/releases/test /data/web_static/shared;printf %s "<h1>ALX School</h1>" > /data/web_static/releases/test/index.html;sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;sudo chown -hR ubuntu:ubuntu /data/;sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\' /etc/nginx/sites-available/default;sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
}
