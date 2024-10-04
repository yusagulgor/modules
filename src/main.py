
"""
(Yüşa Gülgör)
2024y05m01d


"""

from modules import *
# * Modules

# * GEHUB Modules

pPath = ""
rPath = "https://github.com/yusagulgor/Unknow.git"
bName = "main"
commitMessage = "first commit"

readmeText = """ """


git = Gethub("Unknown", pPath, rPath, bName, commitMessage, dwReMD=False)
doc = Decker(build=False)
ghub = GEHUB(git, doc)


# * WEB Modules
# param = [("/","Testhome.html"),("/about","Testabout.html")]
# webM = WebM("test",param)
# web = RWebDev("myWeb",Colour.GREEN,Colour.RED,["hi","sad","hola"],["hi Homun","sad,Doorun","hola Evin"])
# readyWeb = ReadyWebs("readyWeb",YourReadyWebModels.BasicCustom,web)

# * Automation Modules

# * AI Modules 

# deep = DeepLM()
# Rdeep = RDeepLM()
# ydeep = YDeepModels("aliye")

# machineModels = MachineLM()


if __name__ == "__main__":

    # * Usage
    
    ghub.pushRepo()
    # webM.run(debug=True)
    # web.run(debug=True)
    # readyWeb.run(debug=True)
    # web.run(debug=True)
