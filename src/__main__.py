
"""
(Yüşa Gülgör)


"""

from modules import *
# * Modules


# * GEHUB Modules

pPath = "" # ? Ex
rPath = ""
bName = "main"
commitMessage = "first commit"

# readmeText = """ """


git = Gethub( pPath, rPath, bName, commitMessage)
doc = Decker(build=False)
ghub = GEHUB(git, doc)

# * WEB Modules
# param = [("/","Testhome.html"),("/about","Testabout.html")]
# webM = WebM("test",param)
# web = RWebDev("myWeb",Colour.GREEN,Colour.RED,["hi","sad","hola"],["hi Homun","sad,Doorun","hola Evin"])
# readyWeb = ReadyWebs("readyWeb",YourReadyWebModels.LoginRegister,web)

# * Automation Modules


if __name__ == "__main__":

    # * Usage
    
    ghub.pushRepo()
    # webM.run()
    # web.run()
    # readyWeb.run()
    # print(dif)
