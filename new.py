import wget

# Referencia para pasta local
url = "https://super.abril.com.br/wp-content/uploads/2020/09/04-09_gato_SITE.jpg"
wget.download(url, "./downloaded/cat1.jpg")
print("baixou")
