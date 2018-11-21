<!-- language: lang-none -->

    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMNKOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WXdc:::lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    WOc:::::oKMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMMWWWWMMMM
    WOc:::::oKWWNK0kkxddddxkk0KNWMMMMMMMMMMMMMMWNX0OkxxddddxxkO0XNWMMMMMNOxdxkXWMMMMMMMMMMMMMWN0xdxkKWMM
    WOc:::::lkOdlc::::::::::::cldOXWMMMMMMMMWN0kol::::::::::::::cox0XWMXx:::::lONMMMMMMMMMMMW0d:::::l0WM
    Wkc:::::::::::::::::::::::::::cd0NMMMMWXko::::::::::::::::::::::lkKKd::::::cdKWMMMMMMMWXkl::::::l0WM
    WOc::::::::::::::ccllcc:::::::::cd0WWXkl:::::::::ccclllc::::::::::lxkdc::::::lONMMMMMW0d:::::::lONMM
    WOc::::::::::ldk0KXXXXK0kdl:::::::cxOd:::::::coxOKKXXXXXKOxoc:::::::okkl::::::cdKWMWXkl::::::cdKWMMM
    WOc::::::::lkKWMMMMMMMMMMWXkl::::::::::::::cd0NWMMMMMMMMMMWN0dc::::::lO0dc::::::lOX0d:::::::lONMMMMM
    WOc::::::cdKWMMMMMMMMMMMMMMWXdc:::::::::::lONWMMMMMMMMMMMMMMMNOl::::::oKXkl::::::clc::::::cxKWMMMMMM
    WOc::::::dXWMMMMMMMMMMMMMMMMMXd::::::::::lOWMMMMMMMMMMMMMMMMMMW0l:::::ckNWKdc::::::::::::lONWMMMMMMM
    WOc:::::l0WMMMMMMMMMMMMMMMMMMW0l:::::::::dNMMMMMMMMMMMMMMMMMMMMNx::::::dXMWNkl:::::::::cdKWMMMMMMMMM
    WOc:::::oKMMMMMMMMMMMMMMMMMMMMKo:::::::::xWMMMMMMMMMMMMMMMMMMMMWkc:::::oXMMMNkc::::::::oKWMMMMMMMMMM
    WOc:::::l0WMMMMMMMMMMMMMMMMMMW0l:::::::::dNMMMMMMMMMMMMMMMMMMMMNx::::::dXMMNkl:::::::::cdKWMMMMMMMMM
    MKo::::::dXWMMMMMMMMMMMMMMMMWXd::::::::::cOWMMMMMMMMMMMMMMMMMMWOl:::::ckNWKd:::::::::::::lONWMMMMMMM
    MWOc:::::cdKWMMMMMMMMMMMMMMWKd::::::::::::lONMMMMMMMMMMMMMMMMNOl::::::oKXkl::::::clc::::::cdKWMMMMMM
    MMNkc::::::lkKWWMMMMMMMMMWKkl::::::::::::::cd0NWMMMMMMMMMMWN0dc::::::lO0d:::::::lOXKd:::::::lONMMMMM
    MMMNkl:::::::cdk0KXXXXK0kdc:::::::lkOd:::::::coxO0KKXXXXKOxoc:::::::okxl::::::cdKWMWNkl::::::cdKWMMM
    MMMMWKdc:::::::::ccllcc:::::::::cd0WWNkl::::::::::cccllc::::::::::lxOd:::::::lONMMMMMWKd:::::::lONMM
    MMMMMMN0dl::::::::::::::::::::ld0NMMMMWXkoc::::::::::::::::::::cokKKd::::::cdKWMMMMMMMMNkl::::::l0WM
    MMMMMMMMWXOxlc::::::::::::clxOXWMMMMMMMMWN0kdlc:::;:::::::::lok0NWWXx:::::lONMMMMMMMMMMMWKd:::::oKWM
    MMMMMMMMMMMWNK0OkxxddxxkO0KNWMMMMMMMMMMMMMMWWXKOkxxxdddxxkOKXWWMMMMWXOxdxOXWMMMMMMMMMMMMMWN0xdxkKWMM
    MMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMWWWMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   


### Json Web Token Authorization
This is a simple application to demonstrate the box api enterprise authorization.
The example logs into box with JWT Auth avoiding putting your
credentials in the code.

## Installation
Clone the repository and create a virtual environmet for your folder.
Run `pip install -r requirements.txt`
If you want to update all packages to the latest version
you can install pipdate via pip and run pipdate on the requirements.
`pip install pipdate`
`pipdata -rrequirements.txt`

## Usage

Download the application json file in your development console. Put the configuration in a 
`.box` folder and name it app_configuration.json.
If your configuration contains your private key you are all set. If your private key is external,
put it in the same `.box` folder and name it private_key.pem.

## Secureing your credentials

The example is not production ready. The keyring used is a simple plain textfile and
does not ahve any security. Keyring however gives you access to various secure methods
of storing your credentials.

## Python version
The example is only tested against python3. For python2 some types might have to be changed
but for newer developments python3 is anyway strongly recommened.
