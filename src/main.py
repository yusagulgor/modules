
"""
(Yüşa Gülgör)
2024y05m05d


"""

from modules import *
# * Modules

# * WEB Modules
# param = [("/","Testhome.html"),("/about","Testabout.html")]
# webM = WebM("test",param)
web = RWebDev("myWeb",Color.WHITE,Color.GREEN,["Home","Door","Ev"],["Merhaba Homun","Hoşgeldin Doorun","hg Ev"])
readyWeb = ReadyWeb("readyWeb",YourReadyWebModels.LoginRegister,web)

# * Automation Modules

# * AI Modules

# deep = DeepLM()
# Rdeep = RDeepLM()
# ydeep = YDeepModels("aliye")

# machineModels = MachineLM()


# * Usage
# webM.run(debug=True)
# web.run(debug=True)
readyWeb.run(debug=True)