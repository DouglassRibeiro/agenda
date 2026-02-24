npm list tailwindcss >

npm install -D tailwindcss postcss autoprefixer

tailwindcss@3.4.1

Para que o Tailwind CSS observe seus arquivos HTML/Django e recompile o CSS automaticamente a cada salvamento, você precisa do modo **Watch**.

O comando exato depende de como você instalou o Tailwind, mas aqui estão as situações mais comuns:

### 1. Se você instalou via NPM (Padrão)

Se você tem um arquivo `package.json` e instalou via `npm install tailwindcss`, o comando geral é:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch

```

* **`-i`**: O arquivo CSS de entrada (onde você colocou as diretivas `@tailwind base;`, etc).
* **`-o`**: O arquivo CSS de saída (o arquivo final que o Django vai ler).
* **`--watch`**: A flag mágica que mantém o terminal "preso", observando alterações.

---

### 2. A forma recomendada (Scripts do `package.json`)

Para não ter que digitar esse comando gigante toda vez, é recomendável adicionar um script ao seu arquivo `package.json`.

Abra o `package.json` e procure a seção `"scripts"`. Adicione uma linha chamada `"dev"`:

```json
{
  "scripts": {
    "dev": "tailwindcss -i ./caminho/do/seu/input.css -o ./caminho/do/seu/output.css --watch",
    "build": "tailwindcss -i ./caminho/do/seu/input.css -o ./caminho/do/seu/output.css --minify"
  }
}

```

*(Lembre-se de ajustar os caminhos `./caminho/...` para onde estão seus arquivos reais).*

**Como executar:**
Agora, no terminal, basta rodar:

```bash
npm run dev

```

---

### 3. Se estiver usando o pacote `django-tailwind`

Se você instalou a biblioteca Python específica para integração (`django-tailwind`), o comando é gerenciado pelo `manage.py`:

```bash
python manage.py tailwind start

```

*Isso inicia o processo Node.js em segundo plano automaticamente.*

### Dica Importante

Você precisará de **dois terminais** abertos enquanto desenvolve:

1. Um rodando o servidor do Django (`python manage.py runserver`).
2. Outro rodando o Tailwind (`npm run dev` ou o comando acima).

# Instalar maquina virtual:
python -m venv .venv

# Iniciar Projeto django (não esesquecer que você precisa dele antes):
django-admin.exe startproject config .

# Listar pacostes
pip list

# Listar necessarios e colar em um arquivo:
pip freeze > requirements.txt


# Instalar necessearios
pip install -r requirements.txt

---

### Importante !
**Revisar:** No caso de menores apenas o responsavel vão ter ter acesso a plataforma. *(Essa nova geração praticamente já tem acesso a qual quer rede online tendo seus próprios endereços, muitas vezes os pais não acompanham esse avanço).*

django-browser-reload==1.21.0 
---
***figma - icons:**
tailwind.config.js > const { addDynamicIconSelectors } = require('@iconify/tailwind')
tailwind.config.js > plugins > addDynamicIconSelectors()

install --save-dev @iconify/tailwind
install -D @iconify-json/icon-park-outline
install node_module
