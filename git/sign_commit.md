```bash

# Tell Git to use SSH format for signing
git config --global gpg.format ssh

# Point to your public key file
git config --global user.signingkey ~/.ssh/id_ed25519.pub

# (Optional) Sign all commits automatically
git config --global commit.gpgsign true