import random
import streamlit as st


class QuizVirtualisation:
    def __init__(self):
        self.questions = [
            {
                "question": "Qu'est-ce qui est virtualisé dans une machine virtuelle ?",
                "choices": [
                    "Uniquement le processeur",
                    "Uniquement la mémoire et le stockage",
                    "Le processeur, la mémoire, le stockage et les autres périphériques",
                    "Uniquement les périphériques externes"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Quels sont les hyperviseurs mentionnés dans le cours pour les datacenters ? (Plusieurs réponses possibles)",
                "choices": [
                    "VMWare",
                    "VirtualPC",
                    "Proxmox",
                    "KVM"
                ],
                "correct": [0, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Quelle est la principale différence entre la virtualisation et la conteneurisation ?",
                "choices": [
                    "La conteneurisation est plus rapide",
                    "La conteneurisation n'utilise pas de virtualisation mais exécute un processus dans un environnement fermé",
                    "La virtualisation utilise moins de ressources",
                    "Il n'y a aucune différence significative"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Pourquoi podman est-il préféré à docker dans certains cas ?",
                "choices": [
                    "Il est plus rapide",
                    "Il ne nécessite pas les droits root",
                    "Il utilise moins de mémoire",
                    "Il est plus simple à installer"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans un fichier Dockerfile, quels sont les mots-clés corrects et leurs fonctions ? (Plusieurs réponses possibles)",
                "choices": [
                    "FROM définit l'image de base",
                    "WORKDIR définit le répertoire de travail",
                    "CMD lance une commande à chaque fois que le conteneur démarre",
                    "RUN exécute une commande pendant la construction de l'image"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Pour un site web PHP avec base de données, quels packages sont nécessaires ?",
                "choices": [
                    "apache2, php, mysql-server",
                    "apache2, libapache2-mod-php, php, php-mysql, mariadb-server, mariadb-client",
                    "nginx, php, postgresql",
                    "apache2, php uniquement"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans podman-compose, quels éléments peuvent être définis ? (Plusieurs réponses possibles)",
                "choices": [
                    "Le mappage des ports avec 'ports'",
                    "Les variables d'environnement avec 'environment'",
                    "Les dépendances entre services avec 'depends_on'",
                    "Les volumes montés avec 'volumes'"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Pour un site web conteneurisé, quelle est la meilleure approche ?",
                "choices": [
                    "Mettre tous les services (apache, mariadb, php) dans un seul conteneur",
                    "Séparer les services en différents conteneurs (un pour mariadb, un pour apache/php)",
                    "Ne pas utiliser de conteneurs",
                    "Utiliser uniquement des machines virtuelles"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Que permet l'instruction EXPOSE dans un Dockerfile ?",
                "choices": [
                    "D'ouvrir un port accessible par l'hôte",
                    "D'exposer les fichiers du conteneur",
                    "De rendre le conteneur visible sur internet",
                    "De partager des variables d'environnement"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Quels sont les cas d'usage appropriés pour la conteneurisation ? (Plusieurs réponses possibles)",
                "choices": [
                    "Développement de web services",
                    "Microservices",
                    "Services avec API web",
                    "Jeux vidéo haute performance"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Qu'est-ce que Kubernetes ?",
                "choices": [
                    "Un système de virtualisation",
                    "Un système d'orchestration de conteneurs",
                    "Un système d'exploitation",
                    "Un langage de programmation"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quelles sont les fonctionnalités principales de Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "La découverte de services et la répartition de charge",
                    "L'orchestration du stockage",
                    "L'auto-réparation",
                    "La gestion des configurations et des secrets"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "De quoi est composé un cluster Kubernetes ?",
                "choices": [
                    "Uniquement des workers",
                    "Uniquement du control plane",
                    "Du control plane et des workers (nodes)",
                    "D'un seul conteneur central"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Quels sont les composants du Control Plane ? (Plusieurs réponses possibles)",
                "choices": [
                    "kube-apiserver",
                    "kube-scheduler",
                    "kube-controller-manager",
                    "etcd"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Qu'est-ce qu'un Pod dans Kubernetes ?",
                "choices": [
                    "Une machine virtuelle",
                    "La plus petite unité dans le modèle d'objets Kubernetes",
                    "Un serveur physique",
                    "Un réseau virtuel"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quels sont les container runtimes supportés par Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "docker (avec cri-dockerd)",
                    "CRI-O",
                    "Containerd",
                    "VirtualBox"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Quel est le rôle de kubelet ?",
                "choices": [
                    "Gérer le stockage",
                    "Communiquer avec le control plane et exécuter les instructions sur le node",
                    "Gérer uniquement le réseau",
                    "Créer des conteneurs"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Sur quels types d'infrastructure peut-on déployer Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "Bare metal (métal nu)",
                    "Machines virtuelles",
                    "Cloud public",
                    "Environnements cloud hybrides"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Quel composant gère les communications réseau dans un node Kubernetes ?",
                "choices": [
                    "kube-proxy",
                    "kubelet",
                    "etcd",
                    "kube-scheduler"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Quelles sont les étapes principales du déploiement de Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "Installer un container runtime",
                    "Installer kubeadm, kubelet, kubectl",
                    "Initialiser la configuration du control plane",
                    "Installer un plugin réseau"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Dans un manifest Kubernetes, quelle est la structure correcte de base ?",
                "choices": [
                    "kind, apiVersion, spec, metadata",
                    "apiVersion, kind, metadata, spec",
                    "metadata, apiVersion, kind, spec",
                    "spec, metadata, apiVersion, kind"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Analysez ce manifest YAML. Qu'est-ce qui est incorrect ?\n\napiVersion: v1\nkind: Pod\nmetadata:\n  name: my-pod\n  labels:\n    app nginx\nspec:\n  containers:\n  - name: nginx-container\n    image: nginx",
                "choices": [
                    "L'indentation est incorrecte",
                    "Il manque deux points après 'app' dans les labels",
                    "Le nom du conteneur est trop long",
                    "L'image nginx devrait être entre guillemets"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quelles sont les bonnes pratiques pour l'écriture de YAML ? (Plusieurs réponses possibles)",
                "choices": [
                    "Utiliser une indentation cohérente dans tout le fichier",
                    "Utiliser des espaces plutôt que des tabulations",
                    "Mettre entre guillemets les chaînes contenant des caractères spéciaux (:, -, [])",
                    "Valider le YAML avec des outils comme yamllint"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Pour déployer une application avec 3 replicas, quel manifest est correct ?",
                "choices": [
                    "apiVersion: apps/v1\nkind: Deployment\nspec:\n  replicas: 3",
                    "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: my-app\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: my-app\n  template:\n    metadata:\n      labels:\n        app: my-app\n    spec:\n      containers:\n      - name: my-container\n        image: my-image",
                    "apiVersion: v1\nkind: Pod\nmetadata:\n  replicas: 3",
                    "apiVersion: v1\nkind: ReplicaSet\nspec:\n  count: 3"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Comment sélectionner tous les pods avec le label 'env=prod' dans le namespace 'production' via kubectl ?",
                "choices": [
                    "kubectl get pods -n production --selector env=prod",
                    "kubectl get pods -n production -l env=prod",
                    "kubectl select pods -n production where env=prod",
                    "kubectl pods -n production --env prod"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quels éléments sont requis dans la définition d'un Service Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "Le type de service (ClusterIP, NodePort, ou LoadBalancer)",
                    "Un selector pour cibler les pods",
                    "La définition des ports",
                    "Un namespace"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Analysez ce code et identifiez le(s) problème(s) :\n\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: nginx-deployment\nspec:\n  replicas: 2\n  template:\n    metadata:\n      labels:\n        app: nginx\n    spec:\n      containers:\n      - image: nginx\n        name: nginx",
                "choices": [
                    "Il manque le selector dans la spec",
                    "Le nombre de replicas est trop faible",
                    "L'indentation est incorrecte",
                    "Il manque les labels dans metadata"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Que font ces commandes kubectl dans l'ordre ?\n1. kubectl apply -f deployment.yaml\n2. kubectl scale deployment my-app --replicas=5\n3. kubectl rollout undo deployment my-app",
                "choices": [
                    "Créent un déploiement, le suppriment, puis le recréent",
                    "Créent un déploiement, augmentent le nombre de replicas à 5, puis reviennent à la version précédente du déploiement",
                    "Créent un namespace, y déploient 5 pods, puis les suppriment",
                    "Déploient une application, la mettent à jour, puis redémarrent tous les pods"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans un manifest de Service, quels types sont valides ? (Plusieurs réponses possibles)",
                "choices": [
                    "ClusterIP",
                    "NodePort",
                    "LoadBalancer",
                    "ExternalName"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Si vous avez un Deployment avec 3 replicas et un Service de type NodePort qui le cible, que se passe-t-il ?",
                "choices": [
                    "Chaque replica aura son propre port sur le node",
                    "Le Service équilibrera automatiquement la charge entre les 3 replicas sur le même port",
                    "Seul le premier replica sera accessible via le NodePort",
                    "Il faut créer 3 Services différents pour accéder aux 3 replicas"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Pourquoi a-t-on besoin de stockage persistant dans Kubernetes ?",
                "choices": [
                    "Pour stocker les images Docker",
                    "Car les conteneurs perdent leurs données par défaut à leur arrêt",
                    "Pour économiser de la RAM",
                    "Pour accélérer les applications"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quels types de stockage persistant sont disponibles dans Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "Local (Volumes, HDD)",
                    "NFS",
                    "iSCSI",
                    "Ceph"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Analysez ce manifest de PersistentVolume. Qu'est-ce qui est incorrect ?\n\napiVersion: v1\nkind: PersistentVolume\nmetadata:\n  name: pv-volume\nspec:\n  capacity:\n    storage: 5Gi\n  accessModes:\n  - ReadWriteOnce\n  hostPath:\n    path: '/data'",
                "choices": [
                    "Il manque le label 'type: local'",
                    "Il manque le storageClassName",
                    "Le path devrait être en minuscules",
                    "ReadWriteOnce n'est pas un mode d'accès valide"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans quel ordre doit-on créer les ressources pour utiliser du stockage persistant local ?",
                "choices": [
                    "PersistentVolumeClaim → PersistentVolume → Pod → Directory",
                    "Directory → PersistentVolume → PersistentVolumeClaim → Pod",
                    "PersistentVolume → Directory → Pod → PersistentVolumeClaim",
                    "Pod → PersistentVolume → PersistentVolumeClaim → Directory"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans un manifest de PersistentVolumeClaim, que signifie l'attribut 'ReadWriteOnce' ?",
                "choices": [
                    "Le volume ne peut être monté qu'une seule fois en lecture/écriture",
                    "Le volume ne peut être écrit qu'une seule fois",
                    "Le volume ne peut être lu qu'une seule fois",
                    "Le volume doit être monté en lecture seule"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Identifiez les éléments corrects dans ce manifest de Pod avec NFS : (Plusieurs réponses possibles)\n\nkind: Pod\napiVersion: v1\nmetadata:\n  name: pod-with-nfs\nspec:\n  volumes:\n  - name: nfs-volume\n    nfs:\n      server: 10.0.0.5\n      path: /storage\n  containers:\n  - name: app\n    image: nginx\n    volumeMounts:\n    - name: nfs-volume\n      mountPath: /usr/share/nginx/html",
                "choices": [
                    "Le nom du volume dans volumes correspond au nom dans volumeMounts",
                    "Le chemin de montage dans le conteneur est correct pour nginx",
                    "La définition du serveur NFS inclut l'IP et le chemin",
                    "La structure du manifest respecte l'indentation YAML"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Quelle commande permet de vérifier qu'un PersistentVolume est bien lié à un PersistentVolumeClaim ?",
                "choices": [
                    "kubectl get pv",
                    "kubectl describe pvc",
                    "kubectl get storage",
                    "kubectl check volume"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Quelles sont les contraintes du stockage NFS dans Kubernetes ? (Plusieurs réponses possibles)",
                "choices": [
                    "Nécessite une configuration du serveur NFS en amont",
                    "Ne résout pas les problèmes d'accès concurrents",
                    "Doit être monté sur tous les nodes du cluster",
                    "Permet le partage de données entre plusieurs pods"
                ],
                "correct": [0, 1, 3],
                "type": "multiple"
            },
            {
                "question": "Si un PersistentVolume a une capacité de 5Gi, que se passe-t-il si on crée un PVC demandant 3Gi ?",
                "choices": [
                    "Le PVC est rejeté car il ne demande pas toute la capacité",
                    "Le PVC est accepté et peut utiliser jusqu'à 3Gi",
                    "Le PVC est automatiquement ajusté à 5Gi",
                    "Le PVC reste en statut Pending"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Dans un manifest de Pod utilisant un PVC, quel élément fait le lien entre le volume et le PVC ?",
                "choices": [
                    "Le nom du volume dans la section volumes",
                    "L'attribut claimName dans persistentVolumeClaim",
                    "Le mountPath dans volumeMounts",
                    "Le storageClassName"
                ],
                "correct": [1],
                "type": "unique"
            }
        ]
        self.total_questions = len(self.questions)


def initialiser_session():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'questions_melangees' not in st.session_state:
        questions = list(range(len(quiz.questions)))
        random.shuffle(questions)
        st.session_state.questions_melangees = questions  # On prend toutes les questions
    if 'reponses_donnees' not in st.session_state:
        st.session_state.reponses_donnees = False


def reset_quiz():
    for key in st.session_state.keys():
        del st.session_state[key]


quiz = QuizVirtualisation()

st.title('Quiz de Virtualisation')

# Initialisation
initialiser_session()

# Si on n'a pas encore répondu à toutes les questions
if st.session_state.current_question < quiz.total_questions:
    question_idx = st.session_state.questions_melangees[st.session_state.current_question]
    question = quiz.questions[question_idx]

    # Affichage de la question
    st.header(f"Question {st.session_state.current_question + 1}/{quiz.total_questions}")
    st.write(question["question"])

    # Barre de progression
    progress = st.session_state.current_question / quiz.total_questions
    st.progress(progress)

    # Type de question
    st.write(f"*Type: {'Choix multiple' if question['type'] == 'multiple' else 'Choix unique'}*")

    # Création des options de réponse
    if not st.session_state.reponses_donnees:
        if question["type"] == "unique":
            reponse = st.radio("Choisissez votre réponse:",
                               options=range(len(question["choices"])),
                               format_func=lambda x: question["choices"][x])
        else:
            reponses = []
            for i, choix in enumerate(question["choices"]):
                reponses.append(st.checkbox(choix))

        # Bouton de validation
        if st.button('Valider'):
            st.session_state.reponses_donnees = True
            if question["type"] == "unique":
                if reponse == question["correct"][0]:
                    st.success("✅ Correct !")
                    st.session_state.score += 1
                else:
                    st.error("❌ Incorrect")
                    st.write(f"La bonne réponse était : {question['choices'][question['correct'][0]]}")
            else:
                reponses_utilisateur = [i for i, rep in enumerate(reponses) if rep]
                if sorted(reponses_utilisateur) == sorted(question["correct"]):
                    st.success("✅ Parfait ! Toutes les réponses sont correctes !")
                    st.session_state.score += 1
                else:
                    st.error("❌ Incorrect")
                    bonnes_reponses = [question['choices'][i] for i in question["correct"]]
                    st.write("Les bonnes réponses étaient : " + ", ".join(bonnes_reponses))

    # Bouton suivant
    if st.session_state.reponses_donnees:
        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            if st.button('Suivant ➡️'):
                st.session_state.current_question += 1
                st.session_state.reponses_donnees = False
                st.rerun()

# Affichage des résultats finaux
else:
    st.header("Quiz terminé ! 🎉")
    score_percentage = (st.session_state.score / quiz.total_questions) * 100

    # Création de colonnes pour un affichage plus élégant
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Score final", f"{st.session_state.score}/{quiz.total_questions}")
    with col2:
        st.metric("Pourcentage", f"{score_percentage:.1f}%")

    # Message personnalisé basé sur le score
    if score_percentage >= 80:
        st.success("🌟 Bien vu, t'es prêt :)")
    elif score_percentage >= 60:
        st.warning("👍 Pas mal ! Continue tes révisions.")
    else:
        st.error("📚 Oof, force. Revois tes cours.")

    if st.button('Recommencer le quiz 🔄'):
        reset_quiz()
        st.rerun()