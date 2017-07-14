import System.Drawing
import System.Windows.Forms

import re

from System.Drawing import *
from System.Windows.Forms import *
from System import *
from System.IO import *
from System.Text import *

from Json import *

jsonPath = 'settings.json'

def log(s):
	System.Diagnostics.Debug.WriteLine(s)

def log_except(s):
	log('<--------- Error ----------')
	for e in s:
		log(e)
	log('-------------------------->')

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
		
		self.config = {
			'Orientation':'Vertical',
			'History':[],
			'Window':{
				'Left':100,
				'Top':100,
				'Width':800,
				'Height':600
			},
			'Url1':'C:',
			'Url2':'C:'
		}
		
		try:
			if File.Exists(jsonPath):
				File.Copy(jsonPath, jsonPath + '.bak', True)
			self.config.update(LoadJson(jsonPath))
		except:
			log_except(sys.exc_info())
		
		self._comboBox1.Text = self.config['Url1']
		self._comboBox2.Text = self.config['Url2']
		self.Navigate(self._comboBox1, self._webBrowser1)
		self.Navigate(self._comboBox2, self._webBrowser2)
		
		self._comboBox1.Items.Clear()
		self._comboBox1.Items.AddRange(self.config['History'])
		while self._comboBox1.Items.Count > 20:
			self._comboBox1.Items.RemoveAt(0)
		self._comboBox2.Items.Clear()
		self._comboBox2.Items.AddRange(self.config['History'])
		while self._comboBox2.Items.Count > 20:
			self._comboBox2.Items.RemoveAt(0)
		
		if self.config['Orientation']=='Vertical':
			self._splitContainer1.Orientation = Orientation.Vertical
		else:
			self.config['Orientation'] = 'Horizontal'
			self._splitContainer1.Orientation = Orientation.Horizontal
		
		SaveJson(jsonPath, self.config)
		

	def MainFormLoad(self, sender, e):
		self.Left   = self.config['Window']['Left']
		self.Top    = self.config['Window']['Top']
		self.Width  = self.config['Window']['Width']
		self.Height = self.config['Window']['Height']

	def MainFormFormClosed(self, sender, e):
		self.config['History'] = self._comboBox1.Items

		if self._splitContainer1.Orientation == Orientation.Vertical:
			self.config['Orientation'] = 'Vertical'
		else:
			self.config['Orientation'] = 'Horizontal'
			
		self.config['Window']['Left']   = self.Left
		self.config['Window']['Top']    = self.Top
		self.config['Window']['Width']  = self.Width
		self.config['Window']['Height'] = self.Height
		
		self.config['Url2'] = self._comboBox2.Text

	def WebBrowser1DocumentCompleted(self, sender, e):
		self.config['Url1'] = self._comboBox1.Text

		SaveJson(jsonPath, self.config)
	
	def InitializeComponent(self):
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._webBrowser1 = System.Windows.Forms.WebBrowser()
		self._webBrowser2 = System.Windows.Forms.WebBrowser()
		self._verticalToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._horizonalToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._menuStrip1.SuspendLayout()
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
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._verticalToolStripMenuItem,
			self._horizonalToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(592, 26)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# splitContainer1
		# 
		self._splitContainer1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 26)
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
		self._splitContainer1.Size = System.Drawing.Size(592, 249)
		self._splitContainer1.SplitterDistance = 197
		self._splitContainer1.SplitterWidth = 8
		self._splitContainer1.TabIndex = 2
		# 
		# comboBox1
		# 
		self._comboBox1.Dock = System.Windows.Forms.DockStyle.Top
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(0, 0)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(193, 20)
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
		self._comboBox2.Size = System.Drawing.Size(383, 20)
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
		self._webBrowser1.Size = System.Drawing.Size(193, 225)
		self._webBrowser1.TabIndex = 1
		self._webBrowser1.DocumentCompleted += self.WebBrowser1DocumentCompleted
		self._webBrowser1.Navigating += self.WebBrowser1Navigating
		self._webBrowser1.PreviewKeyDown += self.WebBrowserPreviewKeyDown
		# 
		# webBrowser2
		# 
		self._webBrowser2.Dock = System.Windows.Forms.DockStyle.Fill
		self._webBrowser2.Location = System.Drawing.Point(0, 20)
		self._webBrowser2.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser2.Name = "webBrowser2"
		self._webBrowser2.Size = System.Drawing.Size(383, 225)
		self._webBrowser2.TabIndex = 1
		self._webBrowser2.DocumentCompleted += self.WebBrowser2DocumentCompleted
		self._webBrowser2.Navigating += self.WebBrowser2Navigating
		self._webBrowser2.PreviewKeyDown += self.WebBrowserPreviewKeyDown
		# 
		# verticalToolStripMenuItem
		# 
		self._verticalToolStripMenuItem.Name = "verticalToolStripMenuItem"
		self._verticalToolStripMenuItem.Size = System.Drawing.Size(63, 22)
		self._verticalToolStripMenuItem.Text = "Vertical"
		self._verticalToolStripMenuItem.Click += self.VerticalToolStripMenuItemClick
		# 
		# horizonalToolStripMenuItem
		# 
		self._horizonalToolStripMenuItem.Name = "horizonalToolStripMenuItem"
		self._horizonalToolStripMenuItem.Size = System.Drawing.Size(79, 22)
		self._horizonalToolStripMenuItem.Text = "Horizontal"
		self._horizonalToolStripMenuItem.Click += self.HorizonalToolStripMenuItemClick
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
		self.FormClosed += self.MainFormFormClosed
		self.Load += self.MainFormLoad
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def ComboBox1SelectedIndexChanged(self, sender, e):
		self.Navigate(sender, self._webBrowser1)

	def ComboBox2SelectedIndexChanged(self, sender, e):
		self.Navigate(sender, self._webBrowser2)

	def ComboBox1KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			self.Navigate(sender, self._webBrowser1)

	def ComboBox2KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			self.Navigate(sender, self._webBrowser2)
	
	def Navigate(self, comboBox, webBrowser):
		if Directory.Exists(comboBox.Text):
			comboBox.Text = CorrectPath(comboBox.Text)
			if comboBox.Items.Contains(comboBox.Text) == False:
				self._comboBox1.Items.Add(comboBox.Text)
				while self._comboBox1.Items.Count > 20:
					self._comboBox1.Items.RemoveAt(0)
				self._comboBox2.Items.Add(comboBox.Text)
				while self._comboBox2.Items.Count > 20:
					self._comboBox2.Items.RemoveAt(0)
			if comboBox.Text[:2]!='//':
				webBrowser.Navigate(comboBox.Text + '/')
			else:
				webBrowser.Navigate('file:' + comboBox.Text + '/')
		else:
			if len(comboBox.Text) >= 4 and comboBox.Text[:4]=='http':
				webBrowser.Navigate(comboBox.Text)
			elif len(comboBox.Text) == 0:
				webBrowser.Navigate('https://www.google.co.jp')
			elif len(comboBox.Text)==1:
				webBrowser.Navigate('https://www.google.co.jp/search?q=' + comboBox.Text)
			elif comboBox.Text[1]!=':' and comboBox.Text[:2]!='//' and comboBox.Text[:2]!='\\\\':
				webBrowser.Navigate('https://www.google.co.jp/search?q=' + comboBox.Text)
		
	def CorrectUrl(self, path):
		if len(path) >= 5 and path[:5]=='file:':
			path = path[5:]
		return path[3:] if (len(path)>=3 and path[:3]=='///') else path
	
	def WebBrowser2Navigating(self, sender, e):
		self._comboBox2.Text = self.CorrectUrl(str(e.Url))
	def WebBrowser2DocumentCompleted(self, sender, e):
		self._comboBox2.Text = self.CorrectUrl(str(e.Url))

	def WebBrowser1DocumentCompleted(self, sender, e):
		self._comboBox1.Text = self.CorrectUrl(str(e.Url))
	def WebBrowser1Navigating(self, sender, e):
		self._comboBox1.Text = self.CorrectUrl(str(e.Url))

	def HorizonalToolStripMenuItemClick(self, sender, e):
		self._splitContainer1.Orientation = Orientation.Horizontal

	def VerticalToolStripMenuItemClick(self, sender, e):
		self._splitContainer1.Orientation = Orientation.Vertical

	def WebBrowserPreviewKeyDown(self, sender, e):
		if e.KeyCode == Keys.Back:
			path = str(sender.Url)

			if len(path) >= 5 and path[:5]=='file:':
				path = path[5:]
			if len(path) >= 3 and path[:3]=='///':
				path = path[3:]

			log(path)
			
			if Directory.Exists(path):
				if path.rfind('/') > 0:
					sender.Navigate(path[:path.rfind('/')] + '/')
					log('Exists')
			else:
				sender.GoBack()
			