# Usuarios

# para correr el docker 

- docker build -t usuarios .

- docker run -p 3000:3000 -e DB_HOST=link base de datos -e DB_PORT=3306 -e DB_USER=usuario -e DB_PASSWORD=contrasena -e DB_NAME=nombre generico -e URL=0.0.0.0:3000 usuarios
