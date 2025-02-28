<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Vérification de Code</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #111;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            flex-direction: column;
        }

        h1, p {
            text-align: center;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 3rem;
            color: #e60000;
            text-shadow: 0 0 5px #e60000, 0 0 10px #e60000, 0 0 20px #e60000;
        }

        p {
            font-size: 1.2rem;
            color: #bbb;
            margin-bottom: 30px;
            text-shadow: 0 0 5px #e60000, 0 0 10px #e60000;
        }

        .container {
            background-color: #1a1a1a;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 600px;
            text-align: center;
            border: 2px solid #e60000;
        }

        .button {
            background-color: transparent;
            border: 2px solid #e60000;
            color: #e60000;
            padding: 12px 30px;
            border-radius: 30px;
            font-size: 1.1rem;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease-in-out;
            text-decoration: none;
            display: inline-block;
        }

        .button:hover {
            background-color: #e60000;
            color: #111;
            transform: scale(1.1);
        }

        .code {
            font-size: 2rem;
            font-weight: 600;
            margin: 20px 0;
            color: #e60000;
            text-shadow: 0 0 5px #e60000, 0 0 10px #e60000;
        }

        footer {
            position: absolute;
            bottom: 10px;
            color: #bbb;
            font-size: 14px;
            text-align: center;
        }

        footer a {
            color: #e60000;
            text-decoration: none;
        }
    </style>
</head>

<body>

    <header>
        <h1>Vérification de Code</h1>
    </header>

    <div class="container">
        <p>Bienvenue, voici ton code de vérification !</p>
        <div class="code" id="verification-code"></div>

        <!-- Bouton pour copier le code -->
        <button class="button" id="copy-btn">Copier le Code</button>
    </div>

    <footer>
        <p>&copy; 2025 Ton Nom.</p>
    </footer>

    <script>
        // Fonction pour générer un code de vérification aléatoire
        function generateCode() {
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
            let code = '';
            for (let i = 0; i < 8; i++) {
                code += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            return code;
        }

        // Affiche le code généré sur la page
        document.getElementById('verification-code').textContent = generateCode();

        // Fonction pour copier le code dans le presse-papier
        document.getElementById('copy-btn').addEventListener('click', function() {
            const codeText = document.getElementById('verification-code').textContent;
            const textArea = document.createElement('textarea');
            textArea.value = codeText;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);

            alert('Code copié dans le presse-papier : ' + codeText);
        });
    </script>

</body>

</html>
