import wx
class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(500, 450))
        panel = wx.Panel(self, -1)
        menubar=wx.MenuBar()
#Menu section
pehla=wx.Menu()
doosra=wx.Menu()  #So there will be two drop down menu
#Menu Bar Items
menu_1=menubar.Append(pehla,"File")    #Naming of Menu items
menu_2=menubar.Append(doosra,"Edit")
self.SetMenuBar(menubar)
#Menu Items
        
item1_1=pehla.Append(wx.ID_OPEN,"Add","This is add files") #Sub-Items of First menu pull down list
        
item1_2=pehla.Append(wx.ID_EXIT,"Exit","This will exit app") #The last comment will show on status bar when mouse is on that option
self.Bind(wx.EVT_MENU, self.OnFileOpen,item1_1)
        #multiLabel = wx.StaticText(panel, -1, "Multi-line")
self.Bind(wx.EVT_MENU, self.OnFileExit,item1_2)
#Text boxes
Search_Text = wx.TextCtrl(panel, -1,"Enter search string",pos=(5,5),size=(350,30), style=wx.ALIGN_LEFT)
Search_Text.SetInsertionPoint(0)
mytext="\n"
self.Files_List = wx.TextCtrl(panel, -1,mytext,size=wx.Size(400,100),pos=(5,40),style=wx.TE_READONLY)
Search_Text.SetInsertionPoint(0)
#Seacrh Button
        
btn_Process = wx.Button(panel,-1,label='Search',pos=(360,5))
self.Bind(wx.EVT_BUTTON, self.Process, btn_Process)
#Function Definations
        
def OnFileOpen(self, e):
    """ File|Open event - Open dialog box. """
    self.dirname = ''
    dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.xls*")
    if (dlg.ShowModal() == wx.ID_OK):
            
        self.fileName = dlg.GetFilename()
        self.dirName = dlg.GetDirectory()
        text1=str(self.fileName)
                       
        self.Files_List.AppendText(text1+"\n")            
            
def OnFileExit(self, e):
    """ File|Exit event """
    self.Close(True)
def Process(self,event):
    print ("This is a test")
app = wx.PySimpleApp()
frame = TextFrame()
frame.Show()
app.MainLoop()
