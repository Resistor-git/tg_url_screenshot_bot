## Workflow
Checkout the guide on the GitHub https://docs.github.com/en/actions/using-workflows/about-workflows
Basically, you will need to add "secrets" in your GitHub repository: Settings - Secrets and variables - Actions.
Add the following secrets:
* DOCKERHUB_USERNAME - see https://hub.docker.com/
* DOCKERHUB_PASSWORD - see https://hub.docker.com/
* HOST - your dedicated server IP address
* SSH_KEY - ssh key to connect to your server
* SSH_KEY_PASSPHRASE - passphrase for your ssh key
* USERNAME - which user you are going to use on your remote server