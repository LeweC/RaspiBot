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

namespace RaspiBot
{
    public partial class Form1 : Form
    {
        string direction = "empty";
        string moved = "start";

        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (direction != moved || direction == "empty")
            {
                webSocket(direction);
            }

        }

        private void webSocket(string test)
        {
            using (var ws = new WebSocket("ws://31.16.67.247:8001"))
            {
                ws.OnOpen += (sender, e) => {
                    lbl_connection.Text = "Connected to RaspiBot";
                    lbl_connection.ForeColor = Color.LightGreen;
                };
                ws.Connect();
                ws.Send(test);
                //ws.Close();
                moved = test;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            direction = "Standing";
            webSocket(direction);
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
            btn_arrow.Focus();
        }
    }
}
