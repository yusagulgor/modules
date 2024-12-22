from modules import *

# * Test Page
testRouteLink = Text(TextT.LINK,
                     Colors.GREEN,"test")
testRouteLink2 = Text(TextT.LINK,
                      Colors.GREEN,"test2")

testL = Text(TextT.LINK,
             Colors.GREEN,
             "link")

testP = Text(TextT.PARAGRAPH,
             Colors.GREEN,
             "hi")

testT = Text(TextT.TITLE,
             Colors.GREEN,
             "Title")

# * CARDS -------------------------------------
testCardList1 = [testP]
testCardList2 = [testP,testL,testP,testL]

testCard = Card(RCards.STATE,
                wh=[200,100],border_radius=25,
                bgColor=Colors.BLACK,texts=testCardList1)
# print(testCard.to_dict())

testCard2 = Card(RCards.STATE,
                wh=[300,200],border_radius=25,
                bgColor=Colors.RED,texts=testCardList2)

# ! FYT not yet supported

# testCardFYT = Card(RCards.CUSTOM, "border-radius:25,width:200,height:300,background-color:red,metinLen:2,metin1:Hi,metin2:Hii")

# print(testCardFYT.fyt)

# * COMPONENTS -------------------------------------

testNavbarList = [testRouteLink,testRouteLink2]
testNavbar = Navbar(Colors.BLUE,testNavbarList)
testFooter = Footer(Colors.GRAY,testP)
# print(testNavbar)
# print(testFooter.to_dict())

# * PAGES -------------------------------------

testPageHEList1 = [testCard,testP]
testPageHEList2 = [testCard2]

testPage1 = Page("test",testPageHEList1)
testPage2 = Page("test2",testPageHEList2)
testPageList = [testPage1,testPage2]

testWD = WD("test",testNavbar,testFooter,testPageList)
# print(testPage1.to_dict())

testWD.run()


# ? -----------------------------------------------------

# # * Proje Page

# proje= Page("proje")

# # * Home Page

# home = Page("home")

# -----------------------------------------------------

# click = Text()

# card = Card()

# footerText = Text(TextT.PARAGRAPH,Colors.WHITE,"owned")
# navbar = Navbar(Colors.BLUE)
# footer = Footer(Colors.WHITE)s

# pageList = list[home]
# WD("firstTry",navbar,footer,)