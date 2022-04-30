#########################################################
import selenium
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import wget

#########################################################
#                  TODAS AS FUNÇOES
#########################################################
#              RODANDO VERSÃO BUILD TESTE
#########################################################

# Variavel principal
total_src = set()

# Finalizado
def ajuda():
    print("perfil: escolha perfil alvo")
    print("baixar: baixa todos arquivos para pasta local")
    print("mapear: WIP")
    print("OBS: mapear somente após colocar alvo'")
    if input("digite qualquer coisa para voltar") == "":
        lobby()


# Finalizado
def qtd():
    print(len(total_src), " Imagens encontradas")
    lobby()


# Finalizado
def atualizar():
    driver.find_element_by_tag_name("html").send_keys(Keys.END)
    time.sleep(2)
    images = driver.find_elements_by_class_name("FFVAD")
    pics_scr = [elem.get_attribute("src") for elem in images]
    for src in pics_scr:
        total_src.add(src)
    lobby()


# Em progresso
def scroll():
    quantidade_scroll = int(input("valor de 1 a 10: "))
    for i in range(quantidade_scroll):
        print("Scroll em 2 segundos")
        time.sleep(2)
        driver.find_element_by_tag_name("html").send_keys(Keys.END)
        time.sleep(3)
        driver.find_element_by_tag_name("html").send_keys(Keys.END)
        time.sleep(3)
        driver.find_element_by_tag_name("html").send_keys(Keys.END)
        images = driver.find_elements_by_class_name("FFVAD")
        pics_scr = [elem.get_attribute("src") for elem in images]
        for src in pics_scr:
            total_src.add(src)
    qtd()
    lobby()


# Finalizado porem pode ter mais functions
def lobby():
    print("/" * 12 + "Qual opçao deseja? " + "/" * 12)
    print("/" * 12 + "Se precisar de ajuda digita 'help'" + "/" * 12)
    resp = input(str())
    if resp == "perfil":
        goProfile()
    elif resp == "baixar":
        baixaImagens()
    elif resp == "sair":
        quit()
    elif resp == "help":
        ajuda()
    elif resp == "scroll":
        scroll()
    elif resp == "atualizar":
        atualizar()
    elif resp == "qtd":
        qtd()
    else:
        print("Houve algum erro, voltando ao lobby...")
        time.sleep(0.5)
        lobby()


# Finalizado
def goProfile():
    #Limpa lista de fotos capturadas caso ja tenha.
    total_src.clear()
    #Vai até o perfil
    perfil = input("nome do perfil: ")
    time.sleep(3)
    driver.get(f"https://www.instagram.com/{perfil}/")
    # Começa scroll
    time.sleep(3)
    driver.find_element_by_tag_name("html").send_keys(Keys.END)
    time.sleep(3)
    driver.find_element_by_tag_name("html").send_keys(Keys.END)
    time.sleep(3)
    driver.find_element_by_tag_name("html").send_keys(Keys.END)
    # Finish
    print("Indo para o lobby em 2 segundos...")
    time.sleep(2)
    lobby()


# Finalizado
def baixaImagens():
    #
    download_speed = float(input("Velocidade de download: de 0.1 a 0.9: "))
    quantidade_posts = int(input("Quantos posts deseja baixar? "))
    index = 0
    try:
        for s in total_src:
            print("Success!")
            time.sleep(download_speed)  # Velocidade que baixa os arquivos
            wget.download(
                s,
                f"./downloaded/loot{index}.jpg",  # path de download das fotos
            )
            index += 1
            if index >= quantidade_posts:
                break
    except:
        print("Houve algum erro")
        lobby()

    # Finish
    print("Indo para o lobby em 2 segundos...")
    time.sleep(2)
    lobby()


#########################################################
#                   AO INICIAR
#########################################################

# Loga no instagram
nome = str(input("Seu Usuario: "))
senha = str(input("Sua Senha: "))
############### Descomente a linha abaixo caso seu navegador esteja em outra pasta
#ptions = Options()
#options.binary_location = (r"S:\Programs\Browsers\Mozilla Firefox\firefox.exe")  # Coloque seu path
#driver = webdriver.Firefox(options=options)  # ROda com o Firefox em Outra pasta local

driver = webdriver.Firefox()  # firefox_options=
driver.get("https://www.instagram.com")
time.sleep(4)
print("Iniciando Login.")
campo_nome = driver.find_element_by_name("username")
campo_nome.send_keys(nome)
campo_senha = driver.find_element_by_name("password")
campo_senha.send_keys(senha)
time.sleep(3)
campo_nome.send_keys(Keys.RETURN)
lobby()