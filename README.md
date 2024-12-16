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
