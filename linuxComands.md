[]()

# SCP to remote server
scp -r -i Linux-Security-Server.pem GX010012.MP4 ubuntu@3.82.127.245:/tmp/video/

scp                             Initializes program
-r                              Set to reqursive if you want to upload a whole directory
-i Linux-Server.pem             Use private key to login to remote server
GX010012.MP4                    File to upload
uploads/*                       Upload all content from specified directory (-r required)
user@host:/path/uploads         Server credentials:path to where file chould be uploaded to

## --------- Compleate comand ----------------------------------------------------------------------------
scp -r -i /Applications/XAMPP/htdocs/keypairfile.pem uploads/* ec2-user@publicdns:/var/www/html/uploads
## -------------------------------------------------------------------------------------------------------