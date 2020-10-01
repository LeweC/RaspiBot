using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WebSocketSharp;
using CefSharp;
using CefSharp.WinForms;

namespace RaspiBot
{
    public partial class Form1 : Form
    {
        string direction = "empty";
        string USS = "50";
        string camera = "off";
        string[] moved = new string[3];

        public Form1()
        {
            InitializeComponent();
            moved[0] = direction;
            moved[1] = USS;
            moved[2] = camera;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            USS = trackBar_USS.Value.ToString();
            if (moved[0] != direction || direction == "empty" || moved[1] != USS || moved[2] != camera)
            {
                webSocket(direction, USS, camera);
            }

        }

        private void webSocket(string direction, string camera, string USS = "0")
        {
            using (var ws = new WebSocket("ws://192.168.0.43:80"))
            {
                ws.OnOpen += (sender, e) =>
                {
                lbl_connection.Text = "Connected to RaspiBot";
                lbl_connection.ForeColor = Color.LightGreen;
                };
                ws.Connect();
                ws.Send(direction);
                ws.Send(USS);
                ws.Send(camera);
                //ws.Close();
                moved[0] = direction;
                moved[1] = USS;
                moved[2] = camera;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            direction = "Standing";
            webSocket(direction, USS, camera);
            Cef.Shutdown();
        }

        private void btn_forward_Click(object sender, EventArgs e)
        {
            direction = "Forward";
        }

        private void btn_stand_Click(object sender, EventArgs e)
        {
            direction = "Standing";
        }

        private void btn_left_Click(object sender, EventArgs e)
        {
            direction = "Left";
        }

        private void btn_right_Click(object sender, EventArgs e)
        {
            direction = "Right";
        }

        private void btn_backwards_Click(object sender, EventArgs e)
        {
            direction = "Backwards";

        }

        private void btn_auto_Click(object sender, EventArgs e)
        {
            if (btn_auto.Text == "Enable Auto")
            {
                btn_auto.Text = "Disable Auto";
                btn_forward.Enabled = false;
                btn_left.Enabled = false;
                btn_right.Enabled = false;
                btn_backwards.Enabled = false;
                btn_stand.Enabled = false;
                direction = "Auto";
            }
            else
            {
                btn_auto.Text = "Enable Auto";
                if (btn_arrow.Text == "Arrow control")
                {
                    btn_forward.Enabled = true;
                    btn_left.Enabled = true;
                    btn_right.Enabled = true;
                    btn_backwards.Enabled = true;
                    btn_stand.Enabled = true;
                }
                
                direction = "Standing";
                btn_arrow.Focus();
            }
            
        }

        private void btn_arrow_Click(object sender, EventArgs e)
        {
            if (btn_arrow.Text == "Arrow control")
            {
                btn_arrow.Text = "Button control";
                btn_forward.Enabled = false;
                btn_left.Enabled = false;
                btn_right.Enabled = false;
                btn_backwards.Enabled = false;
                btn_stand.Enabled = false;
            }
            else
            {
                btn_arrow.Text = "Arrow control";
                btn_forward.Enabled = true;
                btn_left.Enabled = true;
                btn_right.Enabled = true;
                btn_backwards.Enabled = true;
                btn_stand.Enabled = true;
            }
        }

        private void btn_arrow_KeyDown(object sender, KeyEventArgs e)
        {
            if (btn_arrow.Text == "Button control")
            {
                if (e.KeyCode == Keys.W)
                {
                    direction = "Forward";
                }

                if (e.KeyCode == Keys.S)
                {
                    direction = "Backward";
                }

                if (e.KeyCode == Keys.A)
                {
                    direction = "Left";
                }

                if (e.KeyCode == Keys.D)
                {
                    direction = "Right";
                }

                if (e.KeyCode == Keys.X)
                {
                    direction = "Standing";
                }
            }
            
        }

        private void btn_camera_Click(object sender, EventArgs e)
        {
            try
            {
                Cef.Initialize(new CefSettings());
            }
            catch
            {

            }
            cameraForm cameraForm = new cameraForm();
            if (btn_camera.Text == "Enable Camera")
            {
                btn_camera.Text = "Disable Camera";

                
                cameraForm.Show();
                cameraForm.Visible = true;
            }
            else
            {
                btn_camera.Text = "Enable Camera";
                cameraForm.Visible = false;
                if (System.Windows.Forms.Application.OpenForms["cameraForm"] != null)
                {
                    (System.Windows.Forms.Application.OpenForms["cameraForm"] as cameraForm).exit();
                }

            }
            btn_arrow.Focus();
        }
    }
}
