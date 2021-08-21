import requests
from PIL import Image
from io import BytesIO
import os
os.sys.path
from fpdf import FPDF

nom_manga = input("Donnez le nom du manga : ")
first_url = "https://www.scan-vf.net/uploads/manga/" + input("Donnez l'id du manga choisi en lisant le dossier liste :") + "/chapters/"
chapitre = 1
page = 1
max_page = input("Ecrivez ici le nombre de page par chapitre : ")
max_chapitre = input("Ecrivez ici le nombre de chapitre que vous voulez telecharger : ")
first_des = nom_manga
do_telechargement = input("Voulez vous telecharger (y/n) : ")

def gen_directory():
    chapitre = 1
    while int(chapitre) <= int(max_chapitre):
        url = first_des + "\Chapitre-" + str(chapitre) 
        if not os.path.exists(url):
            os.makedirs(url)
        chapitre = chapitre + 1

def gen_scan():
    if not os.path.exists(nom_manga):
        os.makedirs(nom_manga)

def remplissage_de_pdf():
    chapitre = 1
    page = 1

    x,y,w,h = 0,0,210,297

    while int(chapitre) <= int(max_chapitre):
        page = 0
        imagelist = []
        while int(page) <= int(max_page):
            page = int(page)
            page = page + 1
            if page < 10:
                page = "0"+str(page)
            p = first_des + "\Chapitre-" + str(chapitre) + "\p"+ str(page) + ".png"
            pdf_path = nom_manga + "\pdf\Chapitre-" + str(chapitre) + ".pdf"
            imagelist.append(p)
            pdf = FPDF()
        # imagelist is the list with all image filenames
            if not os.path.exists(p):
                break
            for image in imagelist:
                pdf.add_page()
                pdf.image(image,x,y,w,h)
            pdf.output(pdf_path, "F")
        chapitre = chapitre + 1
        print("Toutes les images du chapitre", chapitre, "on été mise dans leurs pdf attribué.")

def gen_dos_pdf():
    url = nom_manga + "\pdf"
    if not os.path.exists(url):
        os.makedirs(url)

def gen_pdf_vierge():
    chapitre = 1
    while int(chapitre) <= int(max_chapitre):
        url = nom_manga + "\pdf\Chapitre-" +str(chapitre)+'.pdf'
        fichier = open(url, "w") 
        chapitre = chapitre + 1

def telechargement():
    chapitre = 1
    while int(chapitre) <= int(max_chapitre):
        page = 0
        while int(page) <= int(max_page):
            page = int(page)
            page = page + 1
            if page < 10:
                page = "0"+str(page)
            url = first_url + "chapitre-" + str(chapitre) + "/" + str(page) + ".png"
            req = requests.get(url)
            url_2 = first_url + "chapitre-" + str(chapitre) + "/" + str(page) + ".jpg"
            req_2 = requests.get(url_2)
            if req.ok:
                img = Image.open(BytesIO(req.content))
                dim=img.size
                img=img.resize((int(dim[0]/2.),int(dim[1]/2.)))
                p = first_des + "\Chapitre-" + str(chapitre) + "/" +"p"+ str(page)
                img.save(str(p)+".png")
                print("L'image ", str(page), "du chapire", str(chapitre), "a bien été téléchargé.")
            elif req_2.ok:
                img = Image.open(BytesIO(req_2.content))
                dim=img.size
                img=img.resize((int(dim[0]/2.),int(dim[1]/2.)))
                p = first_des + "\Chapitre-" + str(chapitre) + "/" +"p"+ str(page) 
                img.save(str(p)+".png")
                print("L'image ", str(page), "du chapire", str(chapitre), "a bien été téléchargé.")
            else:
                print(req.status_code, req.reason, "Le lien :", url, "n'est pas valide.")
        print("Le  chapitre", str(chapitre), "a bien été téléchargé.")
        chapitre = chapitre + 1

gen_scan()
gen_directory()
gen_dos_pdf()
gen_pdf_vierge()
if do_telechargement == "y":
    telechargement()
remplissage_de_pdf()