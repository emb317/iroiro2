import System.Drawing
import System.Windows.Forms
import System
import System.IO
import System.IO.Path
import System.Collections
import clr

import re
import sys

from System.Drawing import *
from System.Windows.Forms import *
from System.Windows import *
from System.IO import *
from System.IO.Path import *
from System.Collections import *
from System import *
from System.Diagnostics import *

from System.ComponentModel import *
from clr import *

from Json import *
from Lib import *


def log(s):
	System.Diagnostics.Debug.WriteLine(s)

def log_except(s):
	log('<--------- Error ----------')
	for e in s:
		log(e)
	log('-------------------------->')

class MainForm(Form):
	def __init__(self):
		
		self.settingsJsonPath = Path.GetFullPath( 'settings.json' ).replace('\\', '/')
		
		self.InitializeComponent()
		
		self.config = {
			'Root':[ 'C:' ],
			'Ignore':[],
			'MaxFile':20,
			'MaxFolder':30,
			'Window': {
				'Left':100,
				'Top':100,
				'Width':800,
				'Height':600
			},
			'Cmd':'C:/Windows/System32/cmd.exe'
		}
		
		try:
			self.config.update( LoadJson(self.settingsJsonPath) )
		except:
			log_except(sys.exc_info())
			
			if File.Exists(self.settingsJsonPath):
				File.Copy(self.settingsJsonPath, self.settingsJsonPath + '.bak', True)
				MessageBox.Show(self.settingsJsonPath + ' の読み込みに失敗したため\n' + 
					self.settingsJsonPath + '.bak としてバックアップを取り、新規作成しました。',
					'Error',
					MessageBoxButtons.OK,
					MessageBoxIcon.Exclamation)
		
		rootList = self.config['Root']
		self.config['Root'] = ArrayList()
		self.config['Ignore'] = ArrayList(self.config['Ignore'])
		
		for i in rootList:
			self.AddRoot(i)
			
		for i in range( len(self.config['Ignore']) ):
			self.config['Ignore'][i] = CorrectPath(self.config['Ignore'][i])
			
		SaveJson(self.settingsJsonPath, self.config)

	def AddRoot(self, path):
		path = CorrectPath(path)

		if len(filter((lambda n : n.Text==path), self._treeView1.Nodes)) == 0:
			node = TreeNode(path)
			self._treeView1.Nodes.Add(node)
			self.add_dir(node, path, False)
		
		if not path in self.config['Root']:
			self.config['Root'].Add(path)
	
	def is_ignore_item(self, path):
		for s in self.config['Ignore']:
			if path.find(s) != -1:
				return True
		return False
		
	def add_dir(self, node, path, with_file):
		if path[-1] != '/':
			path = path + '/'
		if Directory.Exists(path):
			try:
				dir_cnt = 0
				for dir_path in Directory.GetDirectories(path):
					if not self.is_ignore_item(dir_path):
						dir_cnt += 1
						if dir_cnt >= self.config['MaxFolder']:
							if node.Nodes['*MaxFolder*'] == None:
								d_node = TreeNode('. . .', 1, 1)
								d_node.Name = '*MaxFolder*'
								node.Nodes.Add(d_node)
							break
						
						s = Path.GetFileName(dir_path)
						d_node = node.Nodes[s]
						
						if d_node == None:
							d_node = TreeNode(s)
							d_node.Name = s
							node.Nodes.Add(d_node)
					
				file_cnt = 0
				for file_path in Directory.GetFiles(path):
					if not self.is_ignore_item(file_path):
						file_cnt += 1
						if file_cnt >= self.config['MaxFile']:
							if node.Nodes['*MaxFile*'] == None:
								f_node = TreeNode('. . .', 1,1)
								f_node.Name = '*MaxFile*'
								node.Nodes.Add(f_node)
							break

						s = Path.GetFileName(file_path)
						f_node = node.Nodes[s]
						if f_node == None:
							f_node = TreeNode(s)
							
							img_key = file_path.replace('/', '')
							try:
								icon = System.Drawing.Icon.ExtractAssociatedIcon('' + file_path)
								self._imageList1.Images.Add(img_key, icon)
								f_node.ImageKey = f_node.SelectedImageKey = img_key
							except:
								f_node.ImageIndex = f_node.SelectedImageIndex = 2
							f_node.Name = s
							node.Nodes.Add(f_node)
						
			except:
				log_except(sys.exc_info())
		else:
			node.BackColor = Color.Gray

	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("FTree.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._treeView1 = System.Windows.Forms.TreeView()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._webBrowser1 = System.Windows.Forms.WebBrowser()
		self._imageList1 = System.Windows.Forms.ImageList(self._components)
		self._contextMenuStrip1 = System.Windows.Forms.ContextMenuStrip(self._components)
		self._ignoreItemToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._copyPathToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._copyFileNameToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripStatusLabel1 = System.Windows.Forms.ToolStripStatusLabel()
		self._addRootToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._selectRootToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripSeparator1 = System.Windows.Forms.ToolStripSeparator()
		self._openPromptToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._ignoreItemToolStripMenuItem1 = System.Windows.Forms.ToolStripMenuItem()
		self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._openSettingsjsonToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._addRootToolStripMenuItem1 = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripTextBox1 = System.Windows.Forms.ToolStripTextBox()
		self._toolStripSeparator2 = System.Windows.Forms.ToolStripSeparator()
		self._removeRootToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._statusStrip1.SuspendLayout()
		self._menuStrip1.SuspendLayout()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self._contextMenuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# statusStrip1
		# 
		self._statusStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._toolStripStatusLabel1]))
		self._statusStrip1.Location = System.Drawing.Point(0, 348)
		self._statusStrip1.Name = "statusStrip1"
		self._statusStrip1.Size = System.Drawing.Size(693, 22)
		self._statusStrip1.TabIndex = 1
		self._statusStrip1.Text = "statusStrip1"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._fileToolStripMenuItem,
			self._ignoreItemToolStripMenuItem1,
			self._addRootToolStripMenuItem1,
			self._toolStripTextBox1]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(693, 27)
		self._menuStrip1.TabIndex = 2
		self._menuStrip1.Text = "menuStrip1"
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 27)
		self._splitContainer1.Name = "splitContainer1"
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._treeView1)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._webBrowser1)
		self._splitContainer1.Panel2.Controls.Add(self._comboBox1)
		self._splitContainer1.Size = System.Drawing.Size(693, 321)
		self._splitContainer1.SplitterDistance = 231
		self._splitContainer1.TabIndex = 3
		# 
		# treeView1
		# 
		self._treeView1.AllowDrop = True
		self._treeView1.CheckBoxes = True
		self._treeView1.ContextMenuStrip = self._contextMenuStrip1
		self._treeView1.Dock = System.Windows.Forms.DockStyle.Fill
		self._treeView1.Font = System.Drawing.Font("MS UI Gothic", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 128)
		self._treeView1.FullRowSelect = True
		self._treeView1.ImageIndex = 0
		self._treeView1.ImageList = self._imageList1
		self._treeView1.ItemHeight = 16
		self._treeView1.Location = System.Drawing.Point(0, 0)
		self._treeView1.Name = "treeView1"
		self._treeView1.PathSeparator = "/"
		self._treeView1.SelectedImageIndex = 0
		self._treeView1.Size = System.Drawing.Size(231, 321)
		self._treeView1.TabIndex = 0
		self._treeView1.AfterSelect += self.TreeView1AfterSelect
		self._treeView1.NodeMouseClick += self.TreeView1NodeMouseClick
		self._treeView1.NodeMouseDoubleClick += self.TreeView1NodeMouseDoubleClick
		self._treeView1.KeyDown += self.TreeView1KeyDown
		# 
		# comboBox1
		# 
		self._comboBox1.Dock = System.Windows.Forms.DockStyle.Top
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(0, 0)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(458, 20)
		self._comboBox1.TabIndex = 0
		self._comboBox1.TextChanged += self.ComboBox1TextChanged
		# 
		# webBrowser1
		# 
		self._webBrowser1.Dock = System.Windows.Forms.DockStyle.Fill
		self._webBrowser1.Location = System.Drawing.Point(0, 20)
		self._webBrowser1.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser1.Name = "webBrowser1"
		self._webBrowser1.Size = System.Drawing.Size(458, 301)
		self._webBrowser1.TabIndex = 1
		# 
		# imageList1
		# 
		self._imageList1.ImageStream = resources.GetObject("imageList1.ImageStream")
		self._imageList1.TransparentColor = System.Drawing.Color.Black
		self._imageList1.Images.SetKeyName(0, "")
		self._imageList1.Images.SetKeyName(1, "")
		self._imageList1.Images.SetKeyName(2, "")
		# 
		# contextMenuStrip1
		# 
		self._contextMenuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._ignoreItemToolStripMenuItem,
			self._removeRootToolStripMenuItem,
			self._addRootToolStripMenuItem,
			self._toolStripSeparator2,
			self._copyPathToolStripMenuItem,
			self._copyFileNameToolStripMenuItem,
			self._openPromptToolStripMenuItem,
			self._toolStripSeparator1,
			self._selectRootToolStripMenuItem]))
		self._contextMenuStrip1.Name = "contextMenuStrip1"
		self._contextMenuStrip1.Size = System.Drawing.Size(153, 192)
		self._contextMenuStrip1.Opened += self.ContextMenuStrip1Opened
		# 
		# ignoreItemToolStripMenuItem
		# 
		self._ignoreItemToolStripMenuItem.Name = "ignoreItemToolStripMenuItem"
		self._ignoreItemToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._ignoreItemToolStripMenuItem.Text = "Ignore item"
		self._ignoreItemToolStripMenuItem.Click += self.IgnoreItemToolStripMenuItemClick
		# 
		# copyPathToolStripMenuItem
		# 
		self._copyPathToolStripMenuItem.Name = "copyPathToolStripMenuItem"
		self._copyPathToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._copyPathToolStripMenuItem.Text = "Copy path"
		self._copyPathToolStripMenuItem.Click += self.CopyPathToolStripMenuItemClick
		# 
		# copyFileNameToolStripMenuItem
		# 
		self._copyFileNameToolStripMenuItem.Name = "copyFileNameToolStripMenuItem"
		self._copyFileNameToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._copyFileNameToolStripMenuItem.Text = "Copy file name"
		self._copyFileNameToolStripMenuItem.Click += self.CopyFileNameToolStripMenuItemClick
		# 
		# toolStripStatusLabel1
		# 
		self._toolStripStatusLabel1.Name = "toolStripStatusLabel1"
		self._toolStripStatusLabel1.Size = System.Drawing.Size(0, 17)
		# 
		# addRootToolStripMenuItem
		# 
		self._addRootToolStripMenuItem.Name = "addRootToolStripMenuItem"
		self._addRootToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._addRootToolStripMenuItem.Text = "Add root"
		self._addRootToolStripMenuItem.Click += self.AddRootToolStripMenuItemClick
		# 
		# selectRootToolStripMenuItem
		# 
		self._selectRootToolStripMenuItem.Name = "selectRootToolStripMenuItem"
		self._selectRootToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._selectRootToolStripMenuItem.Text = "Select root"
		self._selectRootToolStripMenuItem.Click += self.SelectRootToolStripMenuItemClick
		# 
		# toolStripSeparator1
		# 
		self._toolStripSeparator1.Name = "toolStripSeparator1"
		self._toolStripSeparator1.Size = System.Drawing.Size(149, 6)
		# 
		# openPromptToolStripMenuItem
		# 
		self._openPromptToolStripMenuItem.Name = "openPromptToolStripMenuItem"
		self._openPromptToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._openPromptToolStripMenuItem.Text = "Open prompt"
		self._openPromptToolStripMenuItem.Click += self.OpenPromptToolStripMenuItemClick
		# 
		# ignoreItemToolStripMenuItem1
		# 
		self._ignoreItemToolStripMenuItem1.Name = "ignoreItemToolStripMenuItem1"
		self._ignoreItemToolStripMenuItem1.Size = System.Drawing.Size(79, 23)
		self._ignoreItemToolStripMenuItem1.Text = "Ignore item"
		self._ignoreItemToolStripMenuItem1.Click += self.IgnoreItemToolStripMenuItem1Click
		# 
		# fileToolStripMenuItem
		# 
		self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._openSettingsjsonToolStripMenuItem,
			self._exitToolStripMenuItem]))
		self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
		self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 23)
		self._fileToolStripMenuItem.Text = "File"
		# 
		# exitToolStripMenuItem
		# 
		self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
		self._exitToolStripMenuItem.Size = System.Drawing.Size(172, 22)
		self._exitToolStripMenuItem.Text = "Exit"
		# 
		# openSettingsjsonToolStripMenuItem
		# 
		self._openSettingsjsonToolStripMenuItem.Name = "openSettingsjsonToolStripMenuItem"
		self._openSettingsjsonToolStripMenuItem.Size = System.Drawing.Size(172, 22)
		self._openSettingsjsonToolStripMenuItem.Text = "Open settings.json"
		self._openSettingsjsonToolStripMenuItem.Click += self.OpenSettingsjsonToolStripMenuItemClick
		# 
		# addRootToolStripMenuItem1
		# 
		self._addRootToolStripMenuItem1.Name = "addRootToolStripMenuItem1"
		self._addRootToolStripMenuItem1.Size = System.Drawing.Size(66, 23)
		self._addRootToolStripMenuItem1.Text = "Add root"
		self._addRootToolStripMenuItem1.Click += self.AddRootToolStripMenuItem1Click
		# 
		# toolStripTextBox1
		# 
		self._toolStripTextBox1.Name = "toolStripTextBox1"
		self._toolStripTextBox1.Size = System.Drawing.Size(100, 23)
		self._toolStripTextBox1.KeyDown += self.ToolStripTextBox1KeyDown
		# 
		# toolStripSeparator2
		# 
		self._toolStripSeparator2.Name = "toolStripSeparator2"
		self._toolStripSeparator2.Size = System.Drawing.Size(149, 6)
		# 
		# removeRootToolStripMenuItem
		# 
		self._removeRootToolStripMenuItem.Name = "removeRootToolStripMenuItem"
		self._removeRootToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._removeRootToolStripMenuItem.Text = "Remove root"
		self._removeRootToolStripMenuItem.Click += self.RemoveRootToolStripMenuItemClick
		# 
		# MainForm
		# 
		self.AllowDrop = True
		self.ClientSize = System.Drawing.Size(693, 370)
		self.Controls.Add(self._splitContainer1)
		self.Controls.Add(self._statusStrip1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "FTree"
		self.FormClosed += self.MainFormFormClosed
		self.Load += self.MainFormLoad
		self._statusStrip1.ResumeLayout(False)
		self._statusStrip1.PerformLayout()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self._contextMenuStrip1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()

	def ComboBox1TextChanged(self, sender, e):
		if self._comboBox1.Focused:
			self.NabigateBrower( self._comboBox1.Text )

	def TreeView1AfterSelect(self, sender, e):
		self.NabigateBrower( e.Node.FullPath )
		if File.Exists(e.Node.FullPath):
			self._comboBox1.Text = Path.GetDirectoryName( e.Node.FullPath ).replace('\\', '/')
		elif Directory.Exists(e.Node.FullPath):
			self._comboBox1.Text = e.Node.FullPath
		
		self._ignoreItemToolStripMenuItem1.Visible = e.Node.Level > 0
		self._addRootToolStripMenuItem1.Visible = e.Node.Level > 0
	
	def NabigateBrower(self, path):
		path = CorrectPath(path)
		if File.Exists(path):
			self._toolStripStatusLabel1.Text = path
		else:
			if(Directory.Exists(path)):
				try:
					self._toolStripStatusLabel1.Text = path
					if path[:2] != '//':
						self._webBrowser1.Navigate(path + '/')
					else:
						self._webBrowser1.Navigate('file:' + path + '/')
				except:
					log_except(sys.exc_info())

	def TreeView1NodeMouseDoubleClick(self, sender, e):
		if File.Exists(e.Node.FullPath):
			System.Diagnostics.Process.Start(e.Node.FullPath)
		else:
			self.add_dir(e.Node, e.Node.FullPath, True)
		

	def TreeView1KeyDown(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			if File.Exists(node.FullPath):
				if e.KeyCode == Keys.Enter:
					System.Diagnostics.Process.Start(node.FullPath)
			else:
				if e.KeyCode == Keys.Enter or e.KeyCode == Keys.Right:
					self.add_dir(node, node.FullPath, True)
	

	def TreeView1NodeMouseClick(self, sender, e):
		if e.Button == MouseButtons.Right:
			self._treeView1.SelectedNode = e.Node

	def MainFormFormClosed(self, sender, e):
		self.config['Window']['Left'] = self.Left
		self.config['Window']['Top'] = self.Top
		self.config['Window']['Width'] = self.Width
		self.config['Window']['Height'] = self.Height
		SaveJson(self.settingsJsonPath, self.config)

	def MainFormLoad(self, sender, e):
		self.Left = self.config['Window']['Left']
		self.Top = self.config['Window']['Top']
		self.Width = self.config['Window']['Width']
		self.Height = self.config['Window']['Height']

	def IgnoreItemToolStripMenuItemClick(self, sender, e):
		if self._treeView1.SelectedNode != None:
			self.config['Ignore'].Add( self._treeView1.SelectedNode.FullPath )
			self._treeView1.SelectedNode.Remove()

	def CopyPathToolStripMenuItemClick(self, sender, e):
		if self._treeView1.SelectedNode != None:
			Clipboard.SetText(self._treeView1.SelectedNode.FullPath)

	def CopyFileNameToolStripMenuItemClick(self, sender, e):
		if self._treeView1.SelectedNode != None:
			Clipboard.SetText(self._treeView1.SelectedNode.Text)
	
	def AddRootToolStripMenuItemClick(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			if(Directory.Exists(node.FullPath)):
				self.AddRoot(node.FullPath)
				
	def SelectRootToolStripMenuItemClick(self, sender, e):
		fbd = FolderBrowserDialog()
		fbd.Description = 'フォルダを指定してください。'
		fbd.RootFolder = Environment.SpecialFolder.Desktop
		fbd.ShowNewFolderButton = True
		
		if (fbd.ShowDialog(self) == DialogResult.OK):
			self.AddRoot(fbd.SelectedPath)
		
	def OpenPromptToolStripMenuItemClick(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			if node.FullPath[:2]!='//' and Directory.Exists(node.FullPath):
				cd = System.Environment.CurrentDirectory
				System.Environment.CurrentDirectory = node.FullPath
				Process.Start(self.config['Cmd'])
				System.Environment.CurrentDirectory = cd
	

	def ContextMenuStrip1Opened(self, sender, e):
		sender.Items['ignoreItemToolStripMenuItem'].Visible = False
		sender.Items['openPromptToolStripMenuItem'].Visible = False
		sender.Items['addRootToolStripMenuItem'].Visible = False
		sender.Items['removeRootToolStripMenuItem'].Visible = False
		node = self._treeView1.SelectedNode
		if node != None:
			if node.Level > 0:
				sender.Items['ignoreItemToolStripMenuItem'].Visible = True
				
			if node.FullPath[:2]!='//' and Directory.Exists(node.FullPath):
				sender.Items['openPromptToolStripMenuItem'].Visible = True
				
			if Directory.Exists(node.FullPath) and node.Level > 0:
				sender.Items['addRootToolStripMenuItem'].Visible = True
			
			if node.Level == 0:
				sender.Items['removeRootToolStripMenuItem'].Visible = True
				

	def ToolStripTextBox1KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			path = CorrectPath(self._toolStripTextBox1.Text)
			if Directory.Exists(path):
				self.AddRoot(path)
				self._toolStripTextBox1.Text = path
		

	def RemoveRootToolStripMenuItemClick(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			path = node.FullPath
			if path in self.config['Root']:
				node.Remove()
				self.config['Root'].Remove(path)

	def OpenSettingsjsonToolStripMenuItemClick(self, sender, e):
		System.Diagnostics.Process.Start(self.settingsJsonPath)

	def IgnoreItemToolStripMenuItem1Click(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			self.config['Ignore'].Add( node.FullPath )
			node.Remove()

	def AddRootToolStripMenuItem1Click(self, sender, e):
		node = self._treeView1.SelectedNode
		if node != None:
			if(Directory.Exists(node.FullPath)):
				self.AddRoot(node.FullPath)