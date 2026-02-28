<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Studio Player Pro</title>
    <style>
        :root { --primary: #2ecc71; --dark: #2c3e50; --light: #ecf0f1; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: var(--light); display: flex; justify-content: center; padding: 20px; }
        .container { background: white; width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: var(--dark); color: white; padding: 20px; text-align: center; }
        .media-section { padding: 20px; border-bottom: 1px solid #eee; }
        
        /* Badge de Durée */
        .badge { background: var(--dark); color: white; padding: 5px 12px; border-radius: 50px; font-size: 0.85em; font-weight: bold; margin-bottom: 10px; display: inline-block; }
        
        audio, video { width: 100%; border-radius: 10px; margin: 10px 0; background: #000; }
        
        .actions { display: flex; flex-direction: column; gap: 10px; margin-top: 10px; }
        
        /* Boutons */
        .btn { border: none; border-radius: 8px; padding: 12px; font-weight: bold; cursor: pointer; text-decoration: none; text-align: center; transition: 0.3s; color: white; }
        .btn-download { background: var(--primary); }
        .btn-share { background: #3498db; }
        .btn:hover { opacity: 0.9; transform: translateY(-2px); }
        
        .status-msg { font-size: 0.8em; color: #7f8c8d; margin-top: 5px; }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Mon Studio</h1>
        <p>Écoutez avant de télécharger</p>
    </div>

    <div class="media-section">
        <span id="audio-time" class="badge">Durée : --:--</span>
        <h3>Musique / Ma Voix</h3>
        
        <audio id="audioPlayer" controls preload="auto">
            <source src="votre-audio.mp3" type="audio/mpeg">
        </audio>
        
        <div id="audio-status" class="status-msg">Prêt à l'écoute</div>

        <div class="actions">
            <a href="votre-audio.mp3" download class="btn btn-download">⬇️ Télécharger MP3</a>
            <button onclick="share('Ma Chanson', 'votre-audio.mp3')" class="btn btn-share">🚀 Partager la musique</button>
        </div>
    </div>

    <div class="media-section">
        <span id="video-time" class="badge">Durée : --:--</span>
        <h3>Clip Vidéo</h3>
        
        <video id="videoPlayer" controls preload="auto" poster="miniature.jpg">
            <source src="votre-video.mp4" type="video/mp4">
        </video>

        <div class="actions">
            <a href="votre-video.mp4" download class="btn btn-download">⬇️ Télécharger le Clip</a>
            <button onclick="share('Mon Clip', 'votre-video.mp4')" class="btn btn-share">📱 Partager la vidéo</button>
        </div>
    </div>
</div>

<script>
    // 1. Gestion de la durée et du chargement
    function setupPlayer(elementId, displayId) {
        const player = document.getElementById(elementId);
        const display = document.getElementById(displayId);

        player.addEventListener('loadedmetadata', function() {
            let min = Math.floor(player.duration / 60);
            let sec = Math.floor(player.duration % 60);
            display.innerText = "Durée : " + min + ":" + (sec < 10 ? '0' : '') + sec;
        });

        // Message si le fichier est en train de charger
        player.addEventListener('waiting', () => {
            if(elementId === 'audioPlayer') document.getElementById('audio-status').innerText = "Chargement du flux...";
        });
        
        player.addEventListener('playing', () => {
            if(elementId === 'audioPlayer') document.getElementById('audio-status').innerText = "Lecture en cours";
        });
    }

    setupPlayer('audioPlayer', 'audio-time');
    setupPlayer('videoPlayer', 'video-time');

    // 2. Fonction de partage intelligente
    function share(title, url) {
        if (navigator.share) {
            navigator.share({
                title: title,
                text: 'Regarde ce que j\'ai créé !',
                url: url
            }).catch(err => console.log('Erreur de partage:', err));
        } else {
            // Lien WhatsApp par défaut pour ordi
            window.open(`https://api.whatsapp.com/send?text=Écoute ça : ${url}`, '_blank');
        }
    }
</script>

</body>
</html>

