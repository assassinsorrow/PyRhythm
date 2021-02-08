import path
import json
import sys

try:
    from Paths import AppDataDir, AppDataConfigDir
except ImportError:
    from .Paths import AppDataDir, AppDataConfigDir
try:
    from Logger import Logger
except ImportError:
    from .Logger import Logger
try:
    from DefualtConfigs import (
        Defualt_Config_Osu4K,
        Defualt_Config_Quaver4K,
        Defualt_Settings,
    )
except ImportError:
    from .DefualtConfigs import (
        Defualt_Config_Osu4K,
        Defualt_Config_Quaver4Kl,
        Defualt_Settings,
    )

# Creates Config Files
def CreateConfigFiles(self):
    # writes settings
    if path.exists(AppDataConfigDir + "Settings.json") == False:
        try:
            with open(AppDataConfigDir + "Settings.json", "w+") as json_file:
                json.dump(Defualt_Settings, json_file, indent=4)
                self.logger.info("created Settings.json")
        except Exception:
            self.logger.exception("Failed to create Settings.json\n")
            sys.exit()

    # writes defualt Osu config
    if path.exists(AppDataConfigDir + "Osu4K.json") == False:
        try:
            with open(AppDataConfigDir + "Osu4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Osu4K, json_file, indent=4)
                self.logger.info("created Osu4K.json")
        except Exception:
            self.logger.exception("Failded to create Osu4K.json\n")
            sys.exit()

    # writes defualt quaver config
    if path.exists(AppDataConfigDir + "Quaver4K.json") == False:
        try:
            with open(AppDataConfigDir + "Quaver4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Quaver4K, json_file, indent=4)
                self.logger.info("created Quaver4K.json")
        except Exception:
            self.logger.exception("Failed to create Quaver4K.json")
            sys.exit()