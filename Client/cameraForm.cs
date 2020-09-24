using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using CefSharp;
using CefSharp.WinForms;

namespace RaspiBot
{
    public partial class cameraForm : Form
    {
        public cameraForm()
        {
            InitializeComponent();
        }

        public ChromiumWebBrowser browser;

        private void cameraForm_Load(object sender, EventArgs e)
        {
            browser = new ChromiumWebBrowser("http://192.168.0.43:8081/");
            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;
        }

        public void exit()
        {
            this.Close();
        }
    }
}
