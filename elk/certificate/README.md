https://kpitest.qa-mpad.azure.cloud.bmw:5601/app/home#/


COPY CERTIFICATE:
scp kpitest.qa-mpad.azure.cloud.bmw.cer qxz2gui@10.11.115.13:/home/qxz2gui

CONVERT CER TO CRT:
openssl x509 -inform PEM in kpitest.qa-mpad.azure.cloud.bmw.cer -out kpitest.qa-mpad.azure.cloud.bmw.crt





sudo vim /etc/nginx/sites-available/elk.conf


server {
     listen [::]:80;
     listen 80;

     server_name kpitest.qa-mpad.azure.cloud.bmw;
 
     return 301 https://kpitest.qa-mpad.azure.cloud.bmw;$request_uri;
}
 
server {
     listen [::]:443 ssl http2;
     listen 443 ssl http2;
 
     server_name kpitest.qa-mpad.azure.cloud.bmw;
    
     ssl_certificate /etc/nginx/certs/kpitest.qa-mpad.azure.cloud.bmw.crt;
     ssl_certificate_key /etc/nginx/certs/kpitest.qa-mpad.azure.cloud.bmw.key;
    location / {
         proxy_pass http://localhost:9200;
         proxy_redirect off;
         proxy_read_timeout    90;
         proxy_connect_timeout 90;
         proxy_set_header  X-Real-IP  $remote_addr;
         proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header  Host $http_host;
     }
} 

ln -s /etc/nginx/sites-available/elk.conf /etc/nginx/sites-enabled/elk.conf