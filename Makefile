all :
	cd src && docker-compose up -d --build

clean : 
	cd src && docker-compose down

re : clean all

web : all
	xdg-open http://localhost:8080