# 💻 Starting development

Get Lost gives you a level template that you can (and should) use to start building levels quickly. It comes with a premade demo map, some sample level code, and public domain assets.

## Load your local Devcontainer

First go to the [level template repo](https://github.com/amoffat/getlost-level-template) and click `Use this template`, then `Create a new repository`:

![create codespace](./assets/create-codespace.png)

Name your new repo whatever you want:

![create repo](./assets/new-repo.png)

Once your new repo is created, clone it locally. We assume you know how to do this!

!!! note

    Using Github Codespaces are not recommended for the Get Lost development environment. Always clone the repo locally instead of opening it in a Codespace.

![clone repo](./assets/clone-repo.png)

After you've cloned the repo locally, open it in VSCode. You should get a popup in the bottom right as VSCode detects that the repo has a devcontainer. When you see it, click `Reopen in Container`:

!!! note

    If you're on WSL2 for Windows, you'll need to make sure that you've activated the WSL integration in Docker Desktop. See [this](https://docs.docker.com/go/wsl2/) for more info.

![open in container](./assets/open-in-container.png)

Now navigate to the `Ports` tab in VSCode and you should see two open ports. One is for playtesting your level (Level Preview) and the other is for using the map editor (Tiled):

![ports](./assets/ports.png)

### 🚨 Troubleshooting

#### My level preview won't open

If you click the `Open in browser` button on the `Level Preview` port and your browser hangs, check that it is opening as `https://` and not `http://`. We serve the level preview over https on localhost, which is a little non-standard, but required for how we load assets.

Your browser also might display an "unsafe site" warning. This is because it's hosted as https on localhost, using a self-signed certificate, so the browser has no way of verifying it. There should be an option to proceed anyways and ignore the warning.

![unsafe](./assets/unsafe-dev.png)
