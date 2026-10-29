# Replica Codex: instalação no Windows, Linux e macOS

Pré-requisitos: Git, Python 3.10+ e o Codex CLI ou extensão Codex do VS Code.

## Windows (PowerShell)

```powershell
git clone https://github.com/jeanpedroni2/replica-codex.git
cd replica-codex
python .\scripts\prepare_codex.py check
python .\scripts\prepare_codex.py install
```

## Linux ou macOS

```bash
git clone https://github.com/jeanpedroni2/replica-codex.git
cd replica-codex
python3 scripts/prepare_codex.py check
python3 scripts/prepare_codex.py install
```

O instalador copia as 11 skills em `~/.agents/skills/`. Reinicie a sessão do Codex, se necessário, e use um prompt como: `Use $replica-recon para mapear os fluxos públicos permitidos deste aplicativo.`

Para atualizar depois de revisar as alterações: `python scripts/prepare_codex.py install --force`.

O repositório é independente do recurso Fork do GitHub. Não é possível impedir tecnicamente forks de repositórios públicos.
