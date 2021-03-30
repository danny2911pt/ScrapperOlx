from typing import Literal
from bs4 import BeautifulSoup
import requests 
import requests 
import pandas as pd

#MainSiteUrl
baseurl = 'https://www.olx.pt/'
trueurl= ''
ranger=0
#Categorias
###########################################################################################################################
CatTeleTablets= 'telemoveis-e-tablets/'
CatTecEInf = 'tecnologia-e-informatica/'
###########################################################################################################################

#SubCategorias
###########################################################################################################################
SubCatTelemoveis = 'telemoveis/'
SubCatTablets= 'tablets/'
SubCatAcess = 'acessorios-telemoveis-tablets/'
###########################################################################################################################

#Searched
############################################################################################################################
SIphone4 = 'q-iphone-4/?'
SIphone4s = 'q-iphone-4s/?'
SIphone5 = 'q-iphone-5/?'
SIphone5s = 'q-iphone-5s/?'
SIphone6 = 'q-iphone-6/?'
SIphone6Plus = 'q-iphone-6-plus/?'
SIphone6S = 'q-iphone-6s/?'
SIphone6SPlus = 'q-iphone-6s-plus/?'
SIphone7 = 'q-iphone-7/?'
SIphone7Plus = 'q-iphone-7-plus/?'
SIphone8 = 'q-iphone-8/?'
SIphone8Plus = 'q-iphone-8-plus/?'
SIphoneX = 'q-iphone-x/?'
SIphoneXMax = 'q-iphone-x-max/?'
SIphoneXs = 'q-iphone-xs/?'
SIphoneXsMax = 'q-iphone-xs-max/?'
SIphone11 = 'q-iphone-11/?'
SIphone11Pro ='q-iphone-11-pro/?'
################################################################################################################################
#Filtros
###############################################################################################################################
#Procurar na Descriçao
PDescricao = 'search%5Bdescription%5D=1&'
#Apenas Anuncios com Imagens
PCImagens = 'search%5Bphotos%5D=1&'
#Preço de
PrecoDe = 'search%5Bfilter_float_price%3Afrom%5D='
#Preço de Ate
PrecoAte = 'search%5Bfilter_float_price%3Ato%5D='
###############################################################################################################################
iphonelinks = []
iphonelist = []
iphone = ''


def categorias (): 
    print('Escolha a categoria que quer acrescentar a sua busca:')
    print('1-Telemoveis e Tablets')
    print('2-Tecnologia e Informatica')
    print('3-Nenhuma')
    escolha = input ("Escolha a sua opçao:")
    if(escolha == '1'):
       return CatTeleTablets
    if(escolha == '2'):
       return CatTecEInf 
    if(escolha == '3'):
        return ''
    
def subcategorias():
    print('Escolha a subcategoria que quer acrescentar a sua busca:')
    print('1-Telemoveis')
    print('2-Tablets')
    print('3-Acessorios')
    print('4-Nenhuma')
    escolha = input ("Escolha a sua opçao:")
    if(escolha == '1'):
       return SubCatTelemoveis
    if(escolha == '2'):
       return SubCatTablets
    if(escolha == '3'):
        return SubCatAcess
    if(escolha == '4'):
        return ''

def modelo():
    global iphone
    print('Escolha o modelo do telemovel:')
    print('1-Iphone 4')
    print('2-Iphone 5')
    print('3-Iphone 6')
    print('4-Iphone 7')
    print('5-Iphone 8')
    print('6-Iphone X')
    print('7-Iphone 11')
    escolha = input ("Escolha a sua opçao:")
    
    
    if(escolha == '1'):
       print('1-Iphone 4')
       print('2-Iphone 4s')
       escolha2 = input('Escolha a sua opcao:')
       if(escolha2 == '1'):
           iphone += 'Iphone 4'
           return SIphone4
       if(escolha2 == '2'):
           iphone='Iphone 4s'
           return SIphone4s

    if(escolha == '2'):
        print('1-Iphone 5')
        print('2-Iphone 5s')
        escolha2 = input('Escolha a sua opcao:')
        if(escolha2 == '1'):
           iphone='Iphone 5'
           return SIphone5
        if(escolha2 == '2'):
           iphone='Iphone 5s'
           return SIphone5s


    if(escolha == '3'):
        print('1-Iphone 6')
        print('2-Iphone 6 Plus')
        print('3-Iphone 6s')
        print('4-Iphone 6s Plus')
        escolha2 = input('Escolha a sua opcao:')
        if(escolha2 == '1'):
           iphone='Iphone 6'
           return SIphone6
        if(escolha2 == '2'):
           iphone='Iphone 6 Plus'
           return SIphone6Plus
        if(escolha2 == '3'):
           iphone='Iphone 6s'
           return SIphone6S
        if(escolha2 == '4'):
           iphone='Iphone 6s Plus'
           return SIphone6SPlus

    if(escolha == '4'):
       print('1-Iphone 7')
       print('2-Iphone 7 Plus')
       escolha2 = input('Escolha a sua opcao:')
       if(escolha2 == '1'):
           iphone='Iphone 7'
           return SIphone7
       if(escolha2 == '2'):
           iphone='Iphone 7 Plus'
           return SIphone7Plus

    if(escolha == '5'):
       print('1-Iphone 8')
       print('2-Iphone 8 Plus')
       escolha2 = input('Escolha a sua opcao:')
       if(escolha2 == '1'):
           iphone='Iphone 8'
           return SIphone8
       if(escolha2 == '2'):
           iphone='Iphone 8 Plus'
           return SIphone8Plus


    if(escolha == '6'):
        print('1-Iphone X')
        print('2-Iphone X Max')
        print('3-Iphone XS ')
        print('4-Iphone XS Max')
        escolha2 = input('Escolha a sua opcao:')
        if(escolha2 == '1'):
           iphone='Iphone X'
           return SIphoneX
        if(escolha2 == '2'):
           iphone='Iphone X Max'
           return SIphoneXMax
        if(escolha2 == '3'):
           iphone='Iphone XS'
           return SIphoneXs
        if(escolha2 == '4'):
           iphone='Iphone XS Max'
           return SIphoneXsMax

    if(escolha == '7'):
       print('1-Iphone 11')
       print('2-Iphone 11 Pro')
       escolha2 = input('Escolha a sua opcao:')
       if(escolha2 == '1'):
           iphone='Iphone 11'
           return SIphone11
       if(escolha2 == '2'):
           iphone='Iphone 11 Pro'
           return SIphone11Pro

def descricao():
    print("Pretende procurar na descricao?")
    print("1-Sim")
    print("2-Nao")
    escolha = input('Escolha a sua opcao:')
    if(escolha=='1'):
        return PDescricao
    if(escolha=='2'):
        return ''

def cimagem():
    print("Pretende procurar anuncios com imagens?")
    print("1-Sim")
    print("2-Nao")
    escolha = input('Escolha a sua opcao:')
    if(escolha=='1'):
        return PCImagens
    if(escolha=='2'):
        return ''

def precode():
    escolha = input('Preco de:')
    if(escolha!=''):
        return PrecoDe+escolha+'&'
    else:
        return '0'

def precoate():
    escolha = input('Preco ate:')
    if(escolha!=''):
        return PrecoAte+escolha+'&'
    else:
        return '0'


def urlmaker():
    return baseurl+categorias()+subcategorias()+modelo()+descricao()+cimagem()+precode()+precoate()


def nPages(trueurl):
    r = requests.get(trueurl)
    soup = BeautifulSoup(r.content,'lxml')
    merda = str(soup.find(attrs={"data-cy" : "page-link-last"}).text.strip())
    return merda

def search(trueurl,iphone,ranger):
    for x in range (1,ranger+1):
        
        r = requests.get(trueurl+'&page='+str(x))
        soup = BeautifulSoup(r.content,'lxml')
        iphones = soup.find_all('h3',class_='lheight22 margintop5')
        
        for item in iphones:
            for link in item.find_all('a',href=True):
                
                if(link=='https://www.google.com/aclk?sa=l&ai=DChcSEwiFvuS86evsAhXElNUKHfjOAqEYABABGgJ3cw&num=1&sig=AOD64_0g198xSGCPCyHteY2acuVNcNfHgA&adurl=&q=&nb=18&rurl=https%3A%2F%2Fwww.olx.pt%2F&nm=32'
                or link=='/aclk?sa=l&ai=DChcSEwiai6KO7OvsAhUEstUKHRNECL8YABAAGgJ3cw&num=1&sig=AOD64_0JWdg4eP95dPRwpzunhXzZ-P8lWw&adurl=&q='):
                        print('')
                else : 
                    iphonelinks.append(link['href'])
        
        

    for link in iphonelinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content,'lxml')
        

        if (str(iphone) in soup.find('h1').text.strip() and 'Capas' not in soup.find('h1').text.strip()
        and 'capa' not in soup.find('h1').text.strip() and 'Ecrã' not in soup.find('h1').text.strip()
        and 'Display' not in soup.find('h1').text.strip() and 'Auriculares' not in soup.find('h1').text.strip()
        and 'auriculares' not in soup.find('h1').text.strip()):
            #Separacao dos Negociaveis dos Nao Negociaveis pois as paginas sao montadas de maneiras diferentes
            if(soup.find('small', class_='pricelabel__label')!=None):
                nome = soup.find('h1').text.strip()  
                preco = soup.find('strong', class_='pricelabel__value arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                    'Link':link,
                    'Nome': nome,
                    'Negociavel?':'Negociavel',
                    'Preco':preco,
                    'Descricao':descricao
                    } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])
            
            else:
                nome = soup.find('h1').text.strip()
                preco = soup.find('strong', class_='pricelabel__value not-arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                        'Link':link,
                        'Nome':nome,
                        'Negociavel?':'Nao Negociavel',
                        'Preco':preco,
                        'Descricao':descricao
                        } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])




trueurl=urlmaker()
ranger+=int(nPages(trueurl))
search(trueurl,iphone,ranger)
da = pd.DataFrame(iphonelist)
da.to_csv(iphone+'.csv')
da.to_excel(iphone+'.xlsx')




 

