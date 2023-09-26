"""
-------------------------------------------------------


AVANT DE LANCER LE SCRIPT, POUR UN MEILLEUR CONFORT
MERCI DE METTRE EN PLEIN ECRAN LA PARTIE OUTPUT DE REPLIT


-------------------------------------------------------
"""
"""
Rappels :

'1' + '1' = '11'
3 * '0' = '000'
'1' + 3*'0' = '1000'
"""

#LIBS IMPORTS
import customtkinter


# Vérifier que la chaîne de caractères est un nombre binaire.
def is_binary(nb_binaire: str) -> bool:
  setNumber = set(nb_binaire)
  if {"0", "1"} != setNumber and setNumber != {'0'} and setNumber != {'1'}:
    return False
  else:
    return True


# 2. Renvoyer la valeur binaire d'un entier non signé
# Convertir un nombre binaire en entier
def calculer_binaire(nb_binaire: str) -> int:
  if is_binary(nb_binaire):
    final = 0
    for i in range(len(nb_binaire)):
      final += 2**i * int(nb_binaire[-1 - i])
    return final


# 3. Encoder un entier en binaire par soustraction
# Convertir un entier en binaire
def encodage_par_soustraction(nombre: int, nb_bits: int):
  if nombre == 0:
    return 0
  else:
    nb_base10 = nombre
    exp = 0
    while 2**exp <= nb_base10:
      exp += 1
    exp -= 1
    reste = nb_base10
    nb_binaire = ''

    for k in range(exp + 1):
      if 2**(exp - k) <= reste:
        nb_binaire = nb_binaire + '1'
        reste -= 2**(exp - k)
      else:
        nb_binaire = nb_binaire + '0'

    nb_binaire = (nb_bits - exp - 1) * "0" + nb_binaire

    return nb_binaire


# 4. Encoder un entier en binaire par division
# Convertir un entier en binaire
def encodage_par_division(number: int, N: int) -> str:
  nb_binaire = ""
  bits = N
  while number > 0:
    bits -= 1
    reste = number % 2
    number //= 2
    nb_binaire = str(reste) + nb_binaire
  nb_binaire = bits * "0" + nb_binaire
  return nb_binaire


# 5. Transformer un nombre binaire sur un nombre de bits précis.
# Mettre un nombre binaire sur n bits
def écriture_sur_Nbits(nb_binaire: str, N: int) -> str:
  if is_binary(nb_binaire):
    return (N - len(nb_binaire)) * "0" + nb_binaire


# 6. Additionner deux nombres binaires
# Additionner deux nombres binaires
def additionner_binaire(nb_binaire1: str, nb_binaire2: str, N: int) -> str:
  if is_binary(nb_binaire1) and is_binary(nb_binaire2):
    resultat = ""
    nb_binaire_list1 = list(écriture_sur_Nbits(nb_binaire1, N))
    nb_binaire_list2 = list(écriture_sur_Nbits(nb_binaire2, N))
    nb_binaire_list1.reverse()
    nb_binaire_list2.reverse()

    additionneur_bit_à_bit = {
      ('0', '0', '0'): ('0', '0'),
      ('0', '0', '1'): ('1', '0'),
      ('0', '1', '0'): ('1', '0'),
      ('0', '1', '1'): ('0', '1'),
      ('1', '0', '0'): ('1', '0'),
      ('1', '0', '1'): ('0', '1'),
      ('1', '1', '0'): ('0', '1'),
      ('1', '1', '1'): ('1', '1')
    }

    retenue = 0

    for bit in range(len(nb_binaire_list1)):
      result = additionneur_bit_à_bit[(nb_binaire_list1[bit],
                                       nb_binaire_list2[bit], str(retenue))]
      resultat = result[0] + resultat
      retenue = result[1]

    return (resultat, retenue)


# 7. Inverser un nombre binaire bits à bits
# Inverser les bits d'un nombre binaire
def inverser_bits(nb_binaire: str, N: int) -> str:
  if is_binary(nb_binaire):
    final = ""
    for bit in nb_binaire:
      if bit == "1":
        final += "0"
      else:
        final += "1"

    return écriture_sur_Nbits(final, N)


# Calculer l'opposé d'un nombre binaire
def opposé_binaire(number: int, N: int) -> str:
  nb_binaire = encodage_par_division(number, N)
  if check_bits_length(nb_binaire) == False:
    return
  else:
    return additionner_binaire(inverser_bits(nb_binaire, N), "1", N)


# Vérifier que le nombre de bits entré est valide
def set_bits_event():
  if input_nombre_bits.get().isnumeric():
    view_menu()


# Renvoyer le nombre de bits défini
def check_bits_length(nb_binaire: str) -> bool:
  if get_bits() < len(nb_binaire):
    result = customtkinter.CTkLabel(
      master=historique_liste,
      text="BitsError - Il y a eu un problème avec la longueur des bits")
    result.pack()
    return False
  else:
    return True


def get_bits():
  return int(input_nombre_bits.get())


# Convertir un nombre binaire en entier et l'afficher dans l'historique
def decoder_binaire_event():
  nb_binaire = choix_décoder_binaire_input_nb_binaire.get()
  if is_binary(nb_binaire):
    if check_bits_length(nb_binaire) == False:
      return
    else:
      choix_décoder_binaire_input_nb_binaire.delete(0, len(nb_binaire))
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=
        f"{nb_binaire} converti en entier -> {calculer_binaire(nb_binaire)}")
      result.pack()


# Convertir un entier en binaire à l'aide de la méthode par division et l'afficher dans l'historique
def encoder_binaire_division_event():
  nombre = choix_encoder_binaire_input_nb_binaire.get()
  if (nombre.isnumeric() == True):
    choix_encoder_binaire_input_nb_binaire.delete(0, len(nombre))
    calcul_result = encodage_par_division(int(nombre), get_bits())
    if check_bits_length(calcul_result) == False:
      return
    else:
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=f"{nombre} converti en binaire -> {calcul_result}")
    result.pack()


# Convertir un entier en binaire à l'aide de la méthode par soustraction et l'afficher dans l'historique
def encoder_binaire_soustraction_event():
  nombre = choix_encoder_binaire_input_nb_binaire.get()
  if (nombre.isnumeric() == True):
    choix_encoder_binaire_input_nb_binaire.delete(0, len(nombre))
    calcul_result = encodage_par_soustraction(int(nombre), get_bits())
    if check_bits_length(calcul_result) == False:
      return
    else:
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=f"{nombre} converti en binaire -> {calcul_result}")
    result.pack()


# Mettre un nombre binaire sur n bits et l'afficher dans l'historique
def additionner_binaire_event():
  nb_binaire1 = choix_choix_additionner_binaire_input_nb_binaire1.get()
  nb_binaire2 = choix_choix_additionner_binaire_input_nb_binaire2.get()
  choix_choix_additionner_binaire_input_nb_binaire1.delete(0, len(nb_binaire1))
  choix_choix_additionner_binaire_input_nb_binaire2.delete(0, len(nb_binaire2))
  if check_bits_length(nb_binaire1) == False or check_bits_length(
      nb_binaire2) == False:
    return
  else:
    operation = additionner_binaire(nb_binaire1, nb_binaire2, get_bits())
    if check_bits_length(operation[0]) == False:
      return
    else:
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=
        f"Le résultat de {nb_binaire1} + {nb_binaire2} est -> {operation[0]} avec pour retenue : {operation[1]}"
      )
      result.pack()


# Inverser les bits d'un nombre binaire et l'afficher dans l'historique
def inverser_bits_event():
  nb_binaire = choix_inverser_bits_input_nb_binaire.get()
  choix_inverser_bits_input_nb_binaire.delete(0, len(nb_binaire))
  if is_binary(nb_binaire):
    if check_bits_length(nb_binaire) == False:
      return
    else:
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=
        f"L'inverse bit a bit du nombre binaire {nb_binaire} est -> {inverser_bits(nb_binaire, get_bits())}"
      )
      result.pack()


# Calculer l’opposé d'un nombre binaire# et l'afficher dans l'historique
def opposé_binaire_event():
  number = choix_opposé_binaire_input_nb_binaire.get()
  choix_opposé_binaire_input_nb_binaire.delete(0, len(number))
  if number.isnumeric():
    calcul_result = opposé_binaire(int(number), get_bits())
    if check_bits_length(calcul_result) == False:
      return
    else:
      result = customtkinter.CTkLabel(
        master=historique_liste,
        text=f"L'opposé du nombre {number} est -> {calcul_result}")
      result.pack()


# Afficher la page appropriée en fonction du choix de l'utilisateur
def menu_choix_event(value):
  if value == "Décoder Binaire":
    view_choix_décoder_binaire()
  elif value == "Encoder Binaire":
    view_choix_encoder_binaire()
  elif value == "Additionner Binaire":
    view_choix_additionner_binaire()
  elif value == "Inverser Bits":
    view_choix_inverser_bits()
  elif value == "Opposé Binaire":
    view_choix_opposé_binaire()


# Cacher toutes les pages
def hide_all_frames():
  accueil.pack_forget()
  historique.pack_forget()
  menu.pack_forget()
  choix_décoder_binaire.pack_forget()
  choix_encoder_binaire.pack_forget()
  choix_additionner_binaire.pack_forget()
  choix_inverser_bits.pack_forget()
  choix_opposé_binaire.pack_forget()


# Afficher la page d'accueil
def view_accueil():
  hide_all_frames()
  accueil.pack(pady=10, padx=30, fill="both", expand=True, side="left")


# Afficher la page de menu
def view_menu():
  hide_all_frames()
  menu.pack(pady=10, padx=30, fill="both", expand=True, side="left")
  view_historique()


# Afficher la partie historique
def view_historique():
  historique.pack(pady=10, padx=30, fill="both", expand=True)


# Afficher la page de décodage binaire
def view_choix_décoder_binaire():
  hide_all_frames()
  view_menu()
  choix_décoder_binaire.pack(padx=10, pady=5, fill="both", expand=True)


# Afficher la page d'encodage binaire
def view_choix_encoder_binaire():
  hide_all_frames()
  view_menu()
  choix_encoder_binaire.pack(padx=10, pady=5, fill="both", expand=True)


# Afficher la page d'addition binaire
def view_choix_additionner_binaire():
  hide_all_frames()
  view_menu()
  choix_additionner_binaire.pack(padx=10, pady=5, fill="both", expand=True)


# Afficher la page d'inversement bits a bits
def view_choix_inverser_bits():
  hide_all_frames()
  view_menu()
  choix_inverser_bits.pack(padx=10, pady=5, fill="both", expand=True)


# Afficher la page d’opposition binaire
def view_choix_opposé_binaire():
  hide_all_frames()
  view_menu()
  choix_opposé_binaire.pack(padx=10, pady=5, fill="both", expand=True)


# PROGRAMME PRINCIPAL

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Calculatrice Binaire")
root.attributes("-fullscreen", True)

# Préparer la page d'accueil
accueil = customtkinter.CTkFrame(master=root)
description_accueil = customtkinter.CTkLabel(
  master=accueil, text="Sur combien de bits voulez-vous travailler ?")
description_accueil.pack(pady=5, padx=10)
input_nombre_bits = customtkinter.CTkEntry(master=accueil)
input_nombre_bits.pack(pady=5, padx=10)
continuer_accueil = customtkinter.CTkButton(master=accueil,
                                            text="Valider",
                                            command=set_bits_event)
continuer_accueil.pack(pady=5, padx=10)

# Préparer la partie historique
historique = customtkinter.CTkFrame(master=root)
historique_titre = customtkinter.CTkLabel(master=historique,
                                          text="\t\t\tHistorique\t\t\t")
historique_titre.pack(pady=5, padx=10, side="top")
historique_liste = customtkinter.CTkScrollableFrame(master=historique)
historique_liste.pack(pady=5, padx=5, fill="both", expand=True)

# Préparer la partie menu
menu = customtkinter.CTkFrame(master=root)
menu_choix = customtkinter.CTkSegmentedButton(master=menu,
                                              values=[
                                                "Décoder Binaire",
                                                "Encoder Binaire",
                                                "Additionner Binaire",
                                                "Inverser Bits",
                                                "Opposé Binaire"
                                              ],
                                              command=menu_choix_event)
menu_choix.pack(padx=20, pady=10)

# Préparer la partie décodage binaire
choix_décoder_binaire = menu_choix = customtkinter.CTkFrame(master=menu)
choix_decoder_binaire_input_description = customtkinter.CTkLabel(
  master=choix_décoder_binaire, text="Entrez un nombre binaire :")
choix_decoder_binaire_input_description.pack(pady=5, padx=10)
choix_décoder_binaire_input_nb_binaire = customtkinter.CTkEntry(
  master=choix_décoder_binaire)
choix_décoder_binaire_input_nb_binaire.pack(pady=5, padx=10)
continuer_choix_encoder_binaire = customtkinter.CTkButton(
  master=choix_décoder_binaire, text="Valider", command=decoder_binaire_event)
continuer_choix_encoder_binaire.pack(pady=5, padx=10)

# Préparer la partie encodage binaire
choix_encoder_binaire = menu_choix = customtkinter.CTkFrame(master=menu)
choix_encoder_binaire_input_description = customtkinter.CTkLabel(
  master=choix_encoder_binaire, text="Entrez un nombre entier :")
choix_encoder_binaire_input_description.pack(pady=5, padx=10)
choix_encoder_binaire_input_nb_binaire = customtkinter.CTkEntry(
  master=choix_encoder_binaire)
choix_encoder_binaire_input_nb_binaire.pack(pady=5, padx=10)
continuer_choix_encoder_binaire_division = customtkinter.CTkButton(
  master=choix_encoder_binaire,
  text="Encoder par division",
  command=encoder_binaire_division_event)
continuer_choix_encoder_binaire_division.pack(pady=5, padx=10)
continuer_choix_encoder_binaire_soustraction = customtkinter.CTkButton(
  master=choix_encoder_binaire,
  text="Encoder par soustractions",
  command=encoder_binaire_soustraction_event)
continuer_choix_encoder_binaire_soustraction.pack(pady=5, padx=10)

# Préparer la partie addition binaire
choix_additionner_binaire = menu_choix = customtkinter.CTkFrame(master=menu)
choix_choix_additionner_binaire_input_description = customtkinter.CTkLabel(
  master=choix_additionner_binaire,
  text="Entrez les deux nombres binaires à aditionner :")
choix_choix_additionner_binaire_input_description.pack(pady=5, padx=10)
choix_choix_additionner_binaire_input_nb_binaire1 = customtkinter.CTkEntry(
  master=choix_additionner_binaire)
choix_choix_additionner_binaire_input_nb_binaire1.pack(pady=5, padx=10)
choix_choix_additionner_binaire_input_signe = customtkinter.CTkLabel(
  master=choix_additionner_binaire, text="+")
choix_choix_additionner_binaire_input_signe.pack(pady=0, padx=10)
choix_choix_additionner_binaire_input_nb_binaire2 = customtkinter.CTkEntry(
  master=choix_additionner_binaire)
choix_choix_additionner_binaire_input_nb_binaire2.pack(pady=5, padx=10)
continuer_choix_additionner_binaire = customtkinter.CTkButton(
  master=choix_additionner_binaire,
  text="Valider",
  command=additionner_binaire_event)
continuer_choix_additionner_binaire.pack(pady=5, padx=10)

# Préparer la partie inversement binaire
choix_inverser_bits = menu_choix = customtkinter.CTkFrame(master=menu)
choix_inverser_bits_input_description = customtkinter.CTkLabel(
  master=choix_inverser_bits,
  text="Entrez un nombre binaire à inverser bit à bit :")
choix_inverser_bits_input_description.pack(pady=5, padx=10)
choix_inverser_bits_input_nb_binaire = customtkinter.CTkEntry(
  master=choix_inverser_bits)
choix_inverser_bits_input_nb_binaire.pack(pady=5, padx=10)
continuer_choix_inverser_bits = customtkinter.CTkButton(
  master=choix_inverser_bits, text="Valider", command=inverser_bits_event)
continuer_choix_inverser_bits.pack(pady=5, padx=10)

# Préparer la partie opposition binaire
choix_opposé_binaire = menu_choix = customtkinter.CTkFrame(master=menu)
choix_opposé_binaire_input_description = customtkinter.CTkLabel(
  master=choix_opposé_binaire, text="Entrez un nombre binaire à opposer :")
choix_opposé_binaire_input_description.pack(pady=5, padx=10)
choix_opposé_binaire_input_nb_binaire = customtkinter.CTkEntry(
  master=choix_opposé_binaire)
choix_opposé_binaire_input_nb_binaire.pack(pady=5, padx=10)
continuer_choix_opposé_binaire = customtkinter.CTkButton(
  master=choix_opposé_binaire, text="Valider", command=opposé_binaire_event)
continuer_choix_opposé_binaire.pack(pady=5, padx=10)

view_accueil()
