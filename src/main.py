from zipfile import ZipFile
from os import write,read,listdir,path
from urllib.request import Request,urlopen, urlretrieve
from urllib.error import HTTPError

DEBUG = False

def fetch_mod():
    """Fetch jar mod from evolutions.johnymuffin.com/downloads/"""

    # try:
    #     req = Request(
    #         url="https://evolutions.johnymuffin.com/downloads/BetaEvolutionsFull-1.5.0.jar",
    #         data=None,
    #         headers={
    #             'User-Agent': 'Mozilla/5.0'
    #         }
    #     )
        

    # except HTTPError as e1:
    #     print(f"HTTP Error:\n{e1}")
    #     file = open("../files/BetaEvolutionsFull-1.5.0.jar", "r")
    file = urlretrieve(url="https://evolutions.johnymuffin.com/downloads/BetaEvolutionsFull-1.5.0.jar", filename="files/BetaEvolutionsFull-1.5.0.jar")
    return file

if __name__ == "__main__" and not DEBUG:
    print(
        """BetaEvo Installer\n
Beta Evolutions by JohnyMuffin (https://evolutions.johnymuffin.com)
Installer by Tabbi-Dev""")
    try:
        mc_path = input("Enter .minecraft/ path: ").strip()
        print(mc_path)
        if "prismlauncher" in mc_path.lower() or "multimc" in mc_path.lower():
            jar_path = f"{mc_path}{'/..'*3}/libraries/com/mojang/minecraft/b1.7.3/minecraft-b1.7.3-client.jar"
            print(jar_path)
        else:
            jar_path = f"{mc_path}/versions/b1.7.3/b1.7.3.jar"
            print(jar_path)

        if not path.exists(jar_path):
            raise FileNotFoundError("minecraft b1.7.3 client jar not found.")

        print(f"Found jar: {jar_path}")
        with ZipFile(jar_path, "a") as f:
            print(f.printdir())
            f.write("files/BetaEvolutionsFull-1.5.0.jar")

    except FileNotFoundError as e:   # This is a placeholder to make IDEA stfu about unclear excepts
        print(f"File does not exist:\n{e}")
    finally:
        pass

elif DEBUG:
    print("ball")
