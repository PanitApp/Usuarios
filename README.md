# Usuarios

para correr el docker 
docker build -t usuarios .
docker run -p 3000:3000 -e DB_HOST=database-1.c5uoovvhbt0n.us-east-1.rds.amazonaws.com -e DB_PORT=3306 -e DB_USER=admin -e DB_PASSWORD=password123 -e DB_NAME=usuarios -e URL=0.0.0.0:3000 usuarios
