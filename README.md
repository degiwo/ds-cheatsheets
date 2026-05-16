# Personal Knowledge Base

## Setup
1. Git Config, see https://git-scm.com/book/ms/v2/Getting-Started-First-Time-Git-Setup
```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vim
git config --global init.defaultBranch main
```

2. GitHub SSH Key, see https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
# set ssh key in GitHub
ssh -T git@github.com
```

3. Zsh, Oh My Zsh, see https://github.com/ohmyzsh/ohmyzsh
```bash
sudo apt install -y zsh
chsh -s $(which zsh)
# re-open terminal
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

4. Tmux, see https://github.com/tmux/tmux
```bash
sudo apt install tmux
```

5. Neovim, see https://github.com/neovim/neovim
```bash
sudo apt install neovim
```

6. fzf, see https://github.com/junegunn/fzf
```bash
sudo apt install fzf
echo 'source /usr/share/doc/fzf/examples/key-bindings.zsh' >> ~/.zshrc
echo 'source /usr/share/doc/fzf/examples/completion.zsh' >> ~/.zshrc
```

7. zk CLI, see https://github.com/zk-org/zk
```bash
curl -LO https://github.com/zk-org/zk/releases/download/v0.15.4/zk-v0.15.4-linux-amd64.tar.gz
tar -xzf zk-v0.15.4-linux-amd64.tar.gz
chmod -x zk /usr/local/bin/
```

