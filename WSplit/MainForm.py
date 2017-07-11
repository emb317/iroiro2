import System.Drawing
import System.Windows.Forms

import re

from System.Drawing import *
from System.Windows.Forms import *
from System import *
from System.IO import *
from System.Text import *

def log(s):
	System.Diagnostics.Debug.WriteLine(s)

def CorrectPath(path):
	path = path.strip()
	path = path.replace('\\', '/')
	path = re.sub('/+$', '', path)
	if len(path) >= 2 and path[1]==':':
		path = path[0].upper() + path[1:]
	return path

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._webBrowser1 = System.Windows.Forms.WebBrowser()
		self._webBrowser2 = System.Windows.Forms.WebBrowser()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self.SuspendLayout()
		# 
		# statusStrip1
		# 
		self._statusStrip1.Location = System.Drawing.Point(0, 275)
		self._statusStrip1.Name = "statusStrip1"
		self._statusStrip1.Size = System.Drawing.Size(592, 22)
		self._statusStrip1.TabIndex = 0
		self._statusStrip1.Text = "statusStrip1"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(592, 24)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 24)
		self._splitContainer1.Name = "splitContainer1"
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._webBrowser1)
		self._splitContainer1.Panel1.Controls.Add(self._comboBox1)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._webBrowser2)
		self._splitContainer1.Panel2.Controls.Add(self._comboBox2)
		self._splitContainer1.Size = System.Drawing.Size(592, 251)
		self._splitContainer1.SplitterDistance = 197
		self._splitContainer1.TabIndex = 2
		# 
		# comboBox1
		# 
		self._comboBox1.Dock = System.Windows.Forms.DockStyle.Top
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(0, 0)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(197, 20)
		self._comboBox1.TabIndex = 0
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		self._comboBox1.KeyDown += self.ComboBox1KeyDown
		# 
		# comboBox2
		# 
		self._comboBox2.Dock = System.Windows.Forms.DockStyle.Top
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Location = System.Drawing.Point(0, 0)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(391, 20)
		self._comboBox2.TabIndex = 0
		self._comboBox2.SelectedIndexChanged += self.ComboBox2SelectedIndexChanged
		self._comboBox2.KeyDown += self.ComboBox2KeyDown
		# 
		# webBrowser1
		# 
		self._webBrowser1.Dock = System.Windows.Forms.DockStyle.Fill
		self._webBrowser1.Location = System.Drawing.Point(0, 20)
		self._webBrowser1.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser1.Name = "webBrowser1"
		self._webBrowser1.Size = System.Drawing.Size(197, 231)
		self._webBrowser1.TabIndex = 1
		# 
		# webBrowser2
		# 
		self._webBrowser2.Dock = System.Windows.Forms.DockStyle.Fill
		self._webBrowser2.Location = System.Drawing.Point(0, 20)
		self._webBrowser2.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser2.Name = "webBrowser2"
		self._webBrowser2.Size = System.Drawing.Size(391, 231)
		self._webBrowser2.TabIndex = 1
		self._webBrowser2.DocumentCompleted += self.WebBrowser2DocumentCompleted
		self._webBrowser2.Navigated += self.WebBrowser2Navigated
		self._webBrowser2.Navigating += self.WebBrowser2Navigating
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(592, 297)
		self.Controls.Add(self._splitContainer1)
		self.Controls.Add(self._statusStrip1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "WSplit"
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def ComboBox1SelectedIndexChanged(self, sender, e):
		pass

	def ComboBox2SelectedIndexChanged(self, sender, e):
		pass

	def ComboBox1KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			self.Navigate(sender, self._webBrowser1)

	def ComboBox2KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			self.Navigate(sender, self._webBrowser2)
	
	def Navigate(self, comboBox, webBrowser):
		if Directory.Exists(comboBox.Text):
			comboBox.Text = CorrectPath(comboBox.Text)
			if comboBox.Text[:2]!='//':
				webBrowser.Navigate(comboBox.Text + '/')
			else:
				webBrowser.Navigate('file:' + comboBox.Text + '/')
		else:
			if len(comboBox.Text) == 0:
				webBrowser.Navigate('https://www.google.co.jp')
			elif len(comboBox.Text)==1:
				webBrowser.Navigate('https://www.google.co.jp/search?q=' + comboBox.Text)
			elif comboBox.Text[1]!=':' and comboBox.Text[:2]!='//' and comboBox.Text[:2]!='\\\\':
				webBrowser.Navigate('https://www.google.co.jp/search?q=' + comboBox.Text)
		
				

	def WebBrowser2Navigated(self, sender, e):
		#WebBrowserNavigatingEventArgs
		log('WebBrowser2Navigated' + str(e))

	def WebBrowser2Navigating(self, sender, e):
		#WebBrowserNavigatedEventArgs
		log('WebBrowser2Navigating' + str(e))

	def WebBrowser2DocumentCompleted(self, sender, e):
		#WebBrowserDocumentCompletedEventArgs
		log('WebBrowser2DocumentCompleted' + str(e))
		