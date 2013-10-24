# Generate public/private key on your machine

    $ ssh-keygen -t rsa             # hit "enter" for all the defaults
    $ cd ~/.ssh                     # two new files were created here
    $ ls -l                             # look at the permissions
    $ cat id*                      # look at the two files

`id_rsa.pub` is your PUBLIC key. You can share this with anyone. Don't ever share your `id_rsa` file.

# Copy your public key to smpanthers.com

    $ scp id_rsa.pub scott@smpanthers.com:id_rsa.pub

# Log in and secure the file

    $ ssh scott@smpanthers.com
    $ mkdir .ssh
    $ mv id_rsa.pub .ssh/authorized_keys
    $ chmod 600 .ssh/authorized_keys
    $ exit
        
# Log out then log back in. ** no password! **

    $ ssh scott@smpanthers.com
    


