# discord.py-email-verification


```mermaid
flowchart TD
    setup("Le membre appelle une commande
    qui setup un message avec un modal qui
    demande à l'utilisateur son email")
    wait("On attends pendant x minute
    l'entrée utilisateur")
    code("On génère un code aléatoire")
    send("On envoie le code généré aléatoirement
    par email à l'utilisateur")
    code_send("Le membre a entré le code
    dans le salon")
    delete_code("On supprime le message du membre")
    unlock("On débloque le membre")

    setup-->wait
    setup-->code
    code-->send
    wait-->code_send
    send-->code_send
    code_send-->delete_code
    delete_code-->unlock
```