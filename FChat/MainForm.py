import System.Drawing
import System.Windows.Forms

from System import *
from System.Drawing import *
from System.Windows.Forms import *
from System.IO import *
from System.Text import *

def log(s):
	System.Diagnostics.Debug.WriteLine(s)

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		
		self._fileSystemWatcher1.Path = '//itsnavi4/850AUTOSAR$/001_T-19電子PF/99. users/GT/amiyake'
		path = self._fileSystemWatcher1.Path + '/fchat.txt'
		self.Read(path)
	
	def InitializeComponent(self):
		self._fileSystemWatcher1 = System.IO.FileSystemWatcher()
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._tabControl1 = System.Windows.Forms.TabControl()
		self._tabPage1 = System.Windows.Forms.TabPage()
		self._tabPage2 = System.Windows.Forms.TabPage()
		self._panel1 = System.Windows.Forms.Panel()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._fileSystemWatcher1.BeginInit()
		self._menuStrip1.SuspendLayout()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self._tabControl1.SuspendLayout()
		self._tabPage1.SuspendLayout()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# fileSystemWatcher1
		# 
		self._fileSystemWatcher1.EnableRaisingEvents = True
		self._fileSystemWatcher1.Filter = "*.txt"
		self._fileSystemWatcher1.NotifyFilter = System.IO.NotifyFilters.LastWrite
		self._fileSystemWatcher1.SynchronizingObject = self
		self._fileSystemWatcher1.Changed += self.FileSystemWatcher1Changed
		# 
		# statusStrip1
		# 
		self._statusStrip1.Location = System.Drawing.Point(0, 331)
		self._statusStrip1.Name = "statusStrip1"
		self._statusStrip1.Size = System.Drawing.Size(311, 22)
		self._statusStrip1.TabIndex = 0
		self._statusStrip1.Text = "statusStrip1"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._fileToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(311, 26)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# fileToolStripMenuItem
		# 
		self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
		self._fileToolStripMenuItem.Size = System.Drawing.Size(40, 22)
		self._fileToolStripMenuItem.Text = "File"
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 26)
		self._splitContainer1.Name = "splitContainer1"
		self._splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._tabControl1)
		self._splitContainer1.Panel1.Controls.Add(self._textBox3)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._textBox1)
		self._splitContainer1.Panel2.Controls.Add(self._panel1)
		self._splitContainer1.Size = System.Drawing.Size(311, 305)
		self._splitContainer1.SplitterDistance = 199
		self._splitContainer1.TabIndex = 2
		# 
		# textBox1
		# 
		self._textBox1.Dock = System.Windows.Forms.DockStyle.Fill
		self._textBox1.Location = System.Drawing.Point(0, 30)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both
		self._textBox1.Size = System.Drawing.Size(311, 72)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.Window
		self._textBox2.Dock = System.Windows.Forms.DockStyle.Fill
		self._textBox2.Location = System.Drawing.Point(3, 3)
		self._textBox2.MaxLength = 10000000
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.ReadOnly = True
		self._textBox2.ScrollBars = System.Windows.Forms.ScrollBars.Both
		self._textBox2.Size = System.Drawing.Size(297, 148)
		self._textBox2.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(4, 4)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Write"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# tabControl1
		# 
		self._tabControl1.Controls.Add(self._tabPage1)
		self._tabControl1.Controls.Add(self._tabPage2)
		self._tabControl1.Dock = System.Windows.Forms.DockStyle.Fill
		self._tabControl1.Location = System.Drawing.Point(0, 19)
		self._tabControl1.Name = "tabControl1"
		self._tabControl1.SelectedIndex = 0
		self._tabControl1.Size = System.Drawing.Size(311, 180)
		self._tabControl1.TabIndex = 1
		# 
		# tabPage1
		# 
		self._tabPage1.Controls.Add(self._textBox2)
		self._tabPage1.Location = System.Drawing.Point(4, 22)
		self._tabPage1.Name = "tabPage1"
		self._tabPage1.Padding = System.Windows.Forms.Padding(3)
		self._tabPage1.Size = System.Drawing.Size(303, 154)
		self._tabPage1.TabIndex = 0
		self._tabPage1.Text = "tabPage1"
		self._tabPage1.UseVisualStyleBackColor = True
		# 
		# tabPage2
		# 
		self._tabPage2.Location = System.Drawing.Point(4, 22)
		self._tabPage2.Name = "tabPage2"
		self._tabPage2.Padding = System.Windows.Forms.Padding(3)
		self._tabPage2.Size = System.Drawing.Size(303, 154)
		self._tabPage2.TabIndex = 1
		self._tabPage2.Text = "tabPage2"
		self._tabPage2.UseVisualStyleBackColor = True
		# 
		# panel1
		# 
		self._panel1.AutoSize = True
		self._panel1.Controls.Add(self._button1)
		self._panel1.Dock = System.Windows.Forms.DockStyle.Top
		self._panel1.Location = System.Drawing.Point(0, 0)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(311, 30)
		self._panel1.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.Dock = System.Windows.Forms.DockStyle.Top
		self._textBox3.Location = System.Drawing.Point(0, 0)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(311, 19)
		self._textBox3.TabIndex = 2
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(311, 353)
		self.Controls.Add(self._splitContainer1)
		self.Controls.Add(self._statusStrip1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "FChat"
		self._fileSystemWatcher1.EndInit()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel1.PerformLayout()
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.Panel2.PerformLayout()
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self._tabControl1.ResumeLayout(False)
		self._tabPage1.ResumeLayout(False)
		self._tabPage1.PerformLayout()
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def FileSystemWatcher1Changed(self, sender, e):
		#log(e.FullPath)
		self.Read(e.FullPath)

	def Button1Click(self, sender, e):
		if self._textBox1.Text != '':
			path = self._fileSystemWatcher1.Path + '/fchat.txt'
			
			self.Read(path)
			
			sw = StreamWriter(path, False, Encoding.GetEncoding("UTF-8"))
			sw.Write(self._textBox2.Text)
			sw.Write('\r\n--- miyake ' + str(DateTime.Now) + ' ---\r\n')
			sw.Write(self._textBox1.Text + '\r\n')
			sw.Close()
			
		self._textBox1.Text = ''
	
	def Read(self, path):
		sr = StreamReader(path, Encoding.GetEncoding("UTF-8"));
		self._textBox2.Text = ''
		self._textBox2.Focus()
		self._textBox2.AppendText( sr.ReadToEnd() )
		sr.Close();
		