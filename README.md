# Optimisation



Maintenant que tout est **push** sur GitHub, voici les étapes que les autres membres de l'équipe doivent suivre pour récupérer le projet **Optimisation** et commencer à collaborer.

---

### **1. Cloner le projet depuis GitHub**
Chaque membre de l'équipe doit suivre ces étapes :

1. Ouvrez **Git Bash** ou un terminal.
2. Allez dans le dossier où vous voulez placer le projet.
3. Clonez le dépôt en utilisant la commande suivante :
   ```bash
   git clone https://github.com/nom-utilisateur/Optimisation.git
   ```
   - Remplacez `nom-utilisateur` par votre nom GitHub ou le nom de l'organisation.
   - L'URL du dépôt se trouve en cliquant sur **Code** dans GitHub (copiez l'URL HTTPS).

4. Accédez au dossier cloné :
   ```bash
   cd Optimisation
   ```

---

### **2. Configurer l'environnement virtuel**
Chaque membre doit créer et activer son propre environnement virtuel.

1. **Créer un environnement virtuel :**
   ```bash
   python -m venv env
   ```

2. **Activer l'environnement virtuel :**
   - Sous Windows :
     ```bash
     .\env\Scripts\activate
     ```
   - Sous macOS/Linux :
     ```bash
     source env/bin/activate
     ```

3. **Installer les dépendances :**
   Si un fichier `requirements.txt` existe, exécutez :
   ```bash
   pip install -r requirements.txt
   ```
   Cela installera toutes les bibliothèques nécessaires.

---

### **3. Vérifier que tout fonctionne**
Chaque membre peut lancer le script principal pour s'assurer que tout est en ordre :

```bash
python main.py
```

Vous devriez voir le message suivant :
```
Bienvenue dans le projet Optimisation !
```

---

### **4. Commencer à travailler**
Chaque membre peut commencer à développer des fonctionnalités en suivant ces bonnes pratiques :

1. **Créer une branche spécifique :**
   - Pour chaque nouvelle fonctionnalité, créez une branche dédiée :
     ```bash
     git checkout -b feature/nom-fonctionnalite
     ```
     Exemple :
     ```bash
     git checkout -b feature/ajout-module-calcul
     ```

2. **Faire des modifications :**
   - Modifiez les fichiers et testez vos changements.

3. **Pousser les modifications :**
   - Une fois les modifications terminées, ajoutez-les :
     ```bash
     git add .
     git commit -m "Description des modifications"
     ```
   - Poussez la branche sur GitHub :
     ```bash
     git push origin feature/nom-fonctionnalite
     ```

---

### **5. Créer une Pull Request**
Sur GitHub :
1. Allez dans l'onglet **Pull Requests**.
2. Cliquez sur **New Pull Request**.
3. Sélectionnez votre branche (`feature/nom-fonctionnalite`) et demandez une revue.

Une fois validée, la branche sera fusionnée dans `main`.

---

### **6. Synchroniser régulièrement**
Pour éviter les conflits, chaque membre doit régulièrement mettre à jour son code local avec les derniers changements sur `main` :

```bash
git pull origin main
```

Si vous travaillez sur une branche, vous pouvez intégrer les changements de `main` dans votre branche :

```bash
git merge main
```

---

### **Résumé pour vos collègues :**
1. Cloner le projet avec `git clone`.
2. Configurer l'environnement virtuel et installer les dépendances.
3. Créer une nouvelle branche pour chaque fonctionnalité.
4. Pousser les modifications sur GitHub et créer des Pull Requests.
5. Mettre à jour régulièrement le code avec `git pull origin main`.

Si vos collègues rencontrent un problème, n'hésitez pas à me le signaler pour que je les guide ! 😊













Pour ouvrir votre projet **Optimisation** avec **Visual Studio Code**, suivez ces étapes simples :

---

### **1. Ouvrir le dossier du projet dans Visual Studio Code**
1. **Lancez Visual Studio Code**.
2. Dans le menu principal, cliquez sur **File > Open Folder** (ou **Fichier > Ouvrir un dossier** si votre VS Code est en français).
3. Naviguez jusqu'au dossier **Optimisation** sur votre disque `D:\`.
4. Cliquez sur **Sélectionner un dossier**.

---

### **2. Configurer l'environnement Python**
Pour utiliser l'environnement virtuel créé précédemment (`env`), configurez Visual Studio Code pour qu'il utilise le bon interpréteur Python.

1. Ouvrez la **palette de commandes** :
   - Appuyez sur `Ctrl + Shift + P` (ou `Cmd + Shift + P` sur macOS).

2. Tapez et sélectionnez **Python: Select Interpreter**.

3. Dans la liste des interpréteurs disponibles, sélectionnez celui qui correspond à votre environnement virtuel :
   ```
   D:\Optimisation\env\Scripts\python.exe
   ```
   - Si vous ne le voyez pas, choisissez **Enter interpreter path** et naviguez manuellement jusqu'à :
     ```plaintext
     D:\Optimisation\env\Scripts\python.exe
     ```

---

### **3. Ouvrir un terminal intégré**
Pour exécuter vos scripts Python directement dans Visual Studio Code, utilisez le terminal intégré :

1. Ouvrez le terminal intégré :
   - Allez dans **Terminal > New Terminal** (ou appuyez sur `Ctrl + `).

2. Assurez-vous que l'environnement virtuel est activé dans ce terminal :
   - Sous Windows :
     ```bash
     .\env\Scripts\activate
     ```

3. Lancez votre script principal :
   ```bash
   python main.py
   ```

---

### **4. Bonus : Ajouter un raccourci pour exécuter le code**
Pour exécuter rapidement vos scripts :
1. Cliquez sur **Run > Add Configuration** dans le menu.
2. Ajoutez un fichier `launch.json` pour configurer l'exécution du fichier `main.py` directement.

---

### **Récapitulatif**
- Ouvrez le dossier **Optimisation** dans Visual Studio Code.
- Sélectionnez l'environnement virtuel via **Python: Select Interpreter**.
- Activez l'environnement virtuel dans le terminal intégré.
- Exécutez vos fichiers Python directement dans le terminal avec `python main.py`.

Si vous avez des difficultés à sélectionner l'interpréteur ou lancer le script, faites-le-moi savoir ! 😊



PS D:\Optimisation> .\env\Scripts\activate
.\env\Scripts\activate : Impossible de charger le fichier D:\Optimisation\env\Scripts\Activate.ps1, car l’exécution de scripts est désactivée sur ce système. Pour plus d’informations, consultez 
about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ .\env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS D:\Optimisation> 



Ce message d'erreur apparaît parce que **l'exécution de scripts PowerShell** est désactivée par la politique de sécurité de votre système. Voici comment résoudre ce problème en modifiant temporairement la politique d'exécution :

---

### **Solution : Modifier la politique d'exécution**

1. **Ouvrez PowerShell en mode administrateur** :
   - Cherchez **PowerShell** dans le menu Démarrer.
   - Faites un clic droit sur **Windows PowerShell** et sélectionnez **Exécuter en tant qu'administrateur**.

2. **Autoriser temporairement les scripts locaux :**
   - Tapez la commande suivante pour autoriser l'exécution des scripts uniquement dans votre session actuelle :
     ```bash
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

   - Si demandé, tapez **Y** pour confirmer.

   > **Explication** :  
   `RemoteSigned` permet d'exécuter les scripts créés localement (comme votre `activate`) sans problème. Les scripts téléchargés depuis Internet nécessiteront une signature.

3. **Ressayez d'activer l'environnement virtuel :**
   - Retournez dans votre terminal PowerShell et activez votre environnement :
     ```bash
     .\env\Scripts\activate
     ```

---

### **Vérifier l'activation**
Si tout fonctionne, vous devriez voir `(env)` apparaître au début de votre invite de commande, comme ceci :

```
(env) PS D:\Optimisation>
```

---

### **Remarque**
La modification avec `Set-ExecutionPolicy` n'affecte que votre utilisateur local. Si vous voulez rétablir la sécurité par défaut après avoir terminé, exécutez :

```bash
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser
```

---

Si vous rencontrez encore des difficultés, je suis là pour vous aider ! 😊



Voici une section complète pour votre **README.md** qui servira de **guide Git** pour l'équipe. Ce guide couvre les commandes essentielles pour travailler en équipe sur le projet avec Git et GitHub.

---

## **Guide Git pour collaborer sur le projet**

Ce guide décrit les étapes essentielles pour utiliser **Git** et **GitHub** afin de collaborer efficacement sur le projet **Optimisation**.

---

### **1. Cloner le projet**
Pour récupérer le projet depuis GitHub pour la première fois :

```bash
git clone https://github.com/nom-utilisateur/Optimisation.git
cd Optimisation
```
- Remplacez `nom-utilisateur` par votre nom d'utilisateur GitHub ou le nom de l'organisation.

---

### **2. Mettre à jour votre projet local (pull)**
Avant de commencer à travailler, assurez-vous d'avoir la dernière version du projet en local :

```bash
git pull origin main
```

---

### **3. Créer une nouvelle branche**
Chaque nouvelle fonctionnalité ou correction doit être réalisée sur une **branche dédiée**. Pour créer une branche et basculer dessus :

```bash
git checkout -b nom-de-la-branche
```
Exemple :
```bash
git checkout -b feature/ajout-json-solution
```

---

### **4. Ajouter et valider vos modifications**
Après avoir modifié ou ajouté des fichiers, suivez ces étapes pour sauvegarder votre travail :

1. **Ajouter vos fichiers modifiés** :
   ```bash
   git add .
   ```

2. **Créer un commit avec un message descriptif** :
   ```bash
   git commit -m "Ajout de la fonctionnalité pour générer un fichier JSON de solution"
   ```

---

### **5. Pousser votre branche sur GitHub**
Une fois vos modifications prêtes, poussez votre branche sur GitHub :

```bash
git push origin nom-de-la-branche
```
Exemple :
```bash
git push origin feature/ajout-json-solution
```

---

### **6. Créer une Pull Request (PR)**
1. Allez sur votre dépôt GitHub : [Optimisation](https://github.com/nom-utilisateur/Optimisation).
2. Cliquez sur l'onglet **Pull Requests**.
3. Cliquez sur **New Pull Request**.
4. Sélectionnez votre branche (`feature/ajout-json-solution`) et créez la PR.
5. Ajoutez un commentaire pour expliquer vos modifications et demandez une revue.

---

### **7. Basculer entre les branches**
Si vous devez changer de branche pour travailler sur autre chose :

- **Voir les branches existantes** :
   ```bash
   git branch
   ```

- **Basculer sur une autre branche** :
   ```bash
   git checkout nom-de-la-branche
   ```

---

### **8. Mettre à jour votre branche avec `main`**
Pour récupérer les dernières modifications de la branche principale (`main`) dans votre branche de travail :

1. Basculez sur `main` et mettez à jour :
   ```bash
   git checkout main
   git pull origin main
   ```

2. Retournez sur votre branche et fusionnez `main` :
   ```bash
   git checkout nom-de-la-branche
   git merge main
   ```

---

### **9. Récupérer les changements d'une autre branche**
Si quelqu'un a poussé du code sur une autre branche et que vous voulez la tester :

```bash
git fetch origin
git checkout nom-de-la-branche
```

---

### **Résumé des commandes utiles**
| Action                                | Commande                                 |
|---------------------------------------|------------------------------------------|
| Cloner le projet                      | `git clone <url-du-repo>`                |
| Mettre à jour depuis `main`           | `git pull origin main`                   |
| Créer une nouvelle branche            | `git checkout -b nom-de-la-branche`      |
| Basculer sur une branche existante    | `git checkout nom-de-la-branche`         |
| Ajouter des modifications             | `git add .`                              |
| Créer un commit                       | `git commit -m "Message du commit"`      |
| Pousser sur GitHub                    | `git push origin nom-de-la-branche`      |
| Mettre à jour une branche avec `main` | `git merge main`                         |
| Voir les branches                     | `git branch`                             |

---

### **Bonnes pratiques**
1. **Travaillez toujours sur une branche dédiée** (jamais directement sur `main`).
2. **Faites des commits fréquents** avec des messages clairs.
3. **Synchronisez régulièrement votre branche** avec `main` pour éviter les conflits.
4. **Revoyez et testez les Pull Requests** avant de les fusionner.

---

Avec ce guide, votre équipe devrait pouvoir travailler efficacement sur le projet **Optimisation** ! 🚀






