
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Diagnostics;

namespace EditorTestCS
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
		void TabPage3DragDrop(object sender, DragEventArgs e)
		{
			System.Diagnostics.Debug.WriteLine("aaa");
		}
		
		void TabPage3DragEnter(object sender, DragEventArgs e)
		{
			
			System.Diagnostics.Debug.WriteLine("bbb");
		}
		
		void TabPage3DragOver(object sender, DragEventArgs e)
		{
		
			System.Diagnostics.Debug.WriteLine("ccc");	
		}
		
		void TabPage3MouseClick(object sender, MouseEventArgs e)
		{
			
			System.Diagnostics.Debug.WriteLine("ddd");	
		}
		
		void TabPage3MouseMove(object sender, MouseEventArgs e)
		{
//			System.Diagnostics.Debug.WriteLine("eee:" + e.Location);	
		}
		
		void MainFormDragEnter(object sender, DragEventArgs e)
		{
			System.Diagnostics.Debug.WriteLine("fff");	
		}
	}
}
