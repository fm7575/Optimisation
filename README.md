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








